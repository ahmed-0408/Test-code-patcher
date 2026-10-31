def calculate_discount(price: float, customer_type: str) -> float:
    """
    Calculate the final price after applying a customer discount.
    """
    # Apply discount for silver customers when the price is at least 100
    if customer_type == "silver" and price >= 100:
        return price * 0.90

    # Apply discount for gold customers when the price is at least 100
    if customer_type == "gold" and price >= 100:
        return price * 0.80

    # No discount applies
    return price