def calculate_discount(price: float, customer_type: str) -> float:
    """
    Calculate the final price after applying a customer discount.
    The discount rules are:
    - Silver customers get a 10% discount for purchases of $100 or more.
    - Gold customers get a 20% discount for purchases of $100 or more.
    The ``customer_type`` argument is case‑insensitive.
    """
    # Normalize the customer type to handle case‑insensitive input
    normalized_type = customer_type.strip().lower() if isinstance(customer_type, str) else ""

    if normalized_type == "silver" and price >= 100:
        return price * 0.90

    if normalized_type == "gold" and price >= 100:
        return price * 0.80

    # No discount applies
    return price
