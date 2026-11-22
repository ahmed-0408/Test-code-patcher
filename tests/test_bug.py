import pytest
from repo.discount import calculate_discount

def test_silver_discount_at_100():
    # price exactly 100 should get 10% discount for silver
    assert calculate_discount(100, "silver") == 90

def test_gold_discount_at_100():
    # price exactly 100 should get 20% discount for gold
    assert calculate_discount(100, "gold") == 80
