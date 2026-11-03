import pytest
from repo.discount import calculate_discount

def test_case_insensitive_customer_type():
    # Uppercase customer types should be handled correctly
    assert calculate_discount(100.0, "Silver") == 90.0
    assert calculate_discount(100.0, "GOLD") == 80.0
    # Mixed case
    assert calculate_discount(150.0, "SiLvEr") == 135.0
    assert calculate_discount(150.0, "GoLd") == 120.0

def test_no_discount_below_threshold():
    # Prices below 100 should not receive discount regardless of type
    assert calculate_discount(99.99, "silver") == 99.99
    assert calculate_discount(50, "gold") == 50
