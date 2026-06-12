from database.deals import Deals
from database.deals import db

class DealService:
    @staticmethod
    def create_deal(data):
        """    
        creating deal 

        Args: The dictionary containing the validated travel deal payload.

        Returns:SQLAlchemy database model instance.
        """

        deal = Deals(
            destination=data["destination"],
            price=data["price"],
            platform=data["platform"],
            rating=data["rating"],
            travel_type=data["travel_type"]
        )

        db.session.add(deal)
        db.session.commit()
        return deal


