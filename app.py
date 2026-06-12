import logging
from flask import Flask
from config import Config
from database.deals import db
from routes.deals import (
    travel_deals_bp
)



def create_app():

    """
    initialization and configuration of flask application 
    Returns: fully configured Flask application instance.
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

        Returns: A health check status confirmation message as a dict
        
        """

        return {
            "message":
            "Travel deals api running"
        }

    @app.errorhandler(Exception)
    def handle_exception(error):
        """
        Globally catches unhandled exceptions and returns a structured error response.
        Args:  exception instance.
        Returns: z JSON error message and an HTTP 500 status code.
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