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

    @staticmethod

    def get_all():
        
        """
        Retrieves all travel deals from the database.
        Returns: A list of all Deals model instances.
        """
    

        return Deals.query.all()

    
    @staticmethod

    def get_deal_by_id(id):
        """
         Handles GET requests to retrieve a single travel deal by ID
         args : deal ID
         return: single Deals model instance 
        """

        return Deals.query.get(id)


