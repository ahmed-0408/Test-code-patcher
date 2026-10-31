import pytest
from repo.discount import calculate_discount

def test_silver_discount_at_boundary():
    # Price exactly 100 should receive 10% discount for silver customers
    assert calculate_discount(100, "silver") == 90

def test_gold_discount_at_boundary():
    # Price exactly 100 should receive 20% discount for gold customers
    assert calculate_discount(100, "gold") == 80
