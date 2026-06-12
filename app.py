import logging
from flask import Flask
from config import Config
from database.deals import db
from routes.deals import (
    travel_deals_bp
)



def create_app():

    """
    application 
    """
    app= Flask(__name__)

    # config loading
    app.config.from_object(Config)

    # Logging 

    logging.basicConfig(
        level = logging.INFO,
        format =
            "%(asctime)s"
            "%(levelname)s"
            "%(message)s"
        
    )

    # database initialization
    db.init_app(app)

    # blueprint register

    app.register_blueprint(
        travel_deals_bp,
        url_prefix= "/deals"
    )

    @app.route("/")
    def health_check():
        """
        health checking api
        """

        return {
            "message":
            "Travel deals api running"
        }

    @app.errorhandler(Exception)
    def handle_exception(error):
        """
        globally error handling
        """

        return (
            {
                "messsage": str(error)
            }, 500
        )

        # table creation

    with app.app_context():
        db.create_all()

    return app
    
app= create_app()

if __name__ == "__main__":
        app.run()