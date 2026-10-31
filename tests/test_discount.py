import pytest
from repo.discount import calculate_discount

def test_silver_no_discount_at_boundary():
    # Price exactly at the threshold should NOT receive a discount for silver customers
    final_price = calculate_discount(100.0, "silver")
    assert final_price == 100.0, "Silver discount incorrectly applied at price 100"

def test_gold_no_discount_at_boundary():
    # Price exactly at the threshold should NOT receive a discount for gold customers
    final_price = calculate_discount(100.0, "gold")
    assert final_price == 100.0, "Gold discount incorrectly applied at price 100"
