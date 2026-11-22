def calculate_discount(price: float, customer_type: str) -> float:
    """
    Calculate the final price after applying a customer discount.
    
    Discounts:
    - Silver customers get 10% off for purchases of $100 or more.
    - Gold customers get 20% off for purchases of $100 or more.
    
    If the price does not meet the threshold or the customer type is unrecognized,
    the original price is returned.
    """
    # Apply discount for silver customers when price is at least 100
    if customer_type == "silver" and price >= 100:
        return price * 0.90

    # Apply discount for gold customers when price is at least 100
    if customer_type == "gold" and price >= 100:
        return price * 0.80

    # No discount applies
    return price
