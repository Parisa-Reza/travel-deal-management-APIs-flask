import enum
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy object
db = SQLAlchemy()

class TravelType(enum.Enum):
    """
    enum represents provided travel types the assignment
    """

    Budget = "Budget"
    Luxury = "Luxury"
    Adventure = "Adventure"
    Family = "Family"

class Deals(db.Model):
    """
    deals table
    """

    __tablename__ = "deals"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    destination = db.Column(
        db.String(100),
        nullable= False
    )

    price= db.Column(
        db.Float,
        nullable = False
    )

    platform = db.Column(
        db.String(100),
        nullable= False
    )

    rating= db.Column(
        db.Float,
        nullable = False
    )

    travel_type= db.Column(
        db.Enum(TravelType),
        nullable = False
    )


    def to_dict(self):
        """
        coneverting model into python dictionary
        Returns:The key-value representation of the travel deal (dictionary)

        """

        return{
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "platform": self.platform,
            "rating": self.rating,
            "travel_type" : self.travel_type.value if self.travel_type else None
        }


    