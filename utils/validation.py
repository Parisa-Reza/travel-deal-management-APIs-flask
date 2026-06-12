from database.deals import TravelType

def validate_deal_data(data):
    """
    Validates incoming JSON data for creating a travel deal 
    Arg: user resquest data in json format
    Return:
    bool: True if all fields are valid, False otherwise.
    str or None: A string error message if validation fails or None if validation is completely successful.
    """
     

    # checking for missing required fields 
    required_fields = ["destination", "price", "platform", "rating", "travel_type"]
    for field in required_fields:
        if field not in data:
            return False, f"'{field}' is a required field."



    # destination validation (cannot be empty)
    if not isinstance(data["destination"], str) or not data["destination"].strip():
        return False, "destination cannot be empty."



    # price validation (+ve)
    try:
        price = float(data["price"])
        if price <= 0:
            return False, "price must be positive."
    except (ValueError, TypeError):
        return False, "price must be a valid number."



    #  rating validation (from 1-5)
    try:
        rating = float(data["rating"])
        if not (1 <= rating <= 5):
            return False, "rating must be between 1-5."
    except (ValueError, TypeError):
        return False, "rating must be a valid number."



    #  travel_type validation (matching with enum values)
    allowed_types = [t.value for t in TravelType] 
    if data["travel_type"] not in allowed_types:
        return False, f"travel_type must be one of: {', '.join(allowed_types)}."

    return True, None