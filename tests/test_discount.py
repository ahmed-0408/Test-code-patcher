import pytest
from discount import calculate_discount

def test_silver_discount_at_100():
    assert calculate_discount(100, "silver") == 90

def test_gold_discount_at_100():
    assert calculate_discount(100, "gold") == 80
