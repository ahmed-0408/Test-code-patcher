import pytest
from repo.discount import calculate_discount

def test_silver_discount_at_boundary():
    # Price exactly at the threshold should receive a 10% discount for silver customers
    final_price = calculate_discount(100.0, "silver")
    assert final_price == 90.0, "Silver discount not applied correctly at price 100"

def test_gold_discount_at_boundary():
    # Price exactly at the threshold should receive a 20% discount for gold customers
    final_price = calculate_discount(100.0, "gold")
    assert final_price == 80.0, "Gold discount not applied correctly at price 100"
