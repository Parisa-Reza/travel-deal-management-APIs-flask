import logging
from flask import Blueprint, jsonify, request
from services.deals import DealService
from utils.validation import validate_deal_data


# deals blueprint

travel_deals_bp = Blueprint(
    "deals",
    __name__
)

logger = logging.getLogger(
    __name__
)

@travel_deals_bp.route(
    "/",
    methods=["POST"]
)

def create_deal():
    """

    Handles POST requests to create and store a new travel deal.

    Returns:A JSON response and an HTTP status code (201 for success, client or server errro).
    """

    # extract request data
    data = request.get_json()
    
    # validation
    is_valid, error_message = validate_deal_data(data)


    if not is_valid:
        return jsonify({"message": error_message}), 400 
    try:
        # service layer calling
        deal = DealService.create_deal(data)
        
        logger.info(
         f"deal created at travel destination : { deal.destination}"
        )
        # Return proper JSON response with 201 Created status
        return jsonify(deal.to_dict()), 201
        
    except Exception as e:
        logger.error(f"Error during deal creation: {str(e)}")
        return jsonify({"message": "An error occurred while creating the deal."}), 500




@travel_deals_bp.route("/", methods=["GET"])
def get_all_deals():
    """
    Handles GET requests to retrieve all travel deals.
    Returns: A JSON list of all deals and an HTTP 200 status code.
    """
    try:
        # service layer calling
        deals = DealService.get_all()
        
        # Convert every SQLAlchemy object in the list into pyhton dictionary
        dict_deals = [deal.to_dict() for deal in deals]
        
        # here from the database instances -> python dictionary -> json
        return jsonify(dict_deals), 200
        
    except Exception as e:
        logger.error(f"Error while fetching deals: {str(e)}")
        return jsonify({"message": "An error occurred while retrieving deals."}), 500




@travel_deals_bp.route("/<int:id>", methods=["GET"])

def get_deal(id):
    """
    Fetch a travel deal by its unique database ID.
    arg : The unique integer ID of the deal.
    return: A JSON response containing the deal data or a 404 error message.
    """

    one_deal = (DealService.get_deal_by_id(id))

    if not one_deal:
        return (
            jsonify(
                {
                    "mesaage" : "deal not found in the database"
                }
            ),404
        )

  # single db instance -> python dict -> jsonify
  
    return jsonify(one_deal.to_dict()),200