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
