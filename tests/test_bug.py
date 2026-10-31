import pytest
from repo.discount import calculate_discount

def test_silver_discount_at_100():
    # Silver customers should get 10% discount even when price is exactly 100
    assert calculate_discount(100, "silver") == pytest.approx(90.0)

def test_gold_discount_at_100():
    # Gold customers should get 20% discount even when price is exactly 100
    assert calculate_discount(100, "gold") == pytest.approx(80.0)
