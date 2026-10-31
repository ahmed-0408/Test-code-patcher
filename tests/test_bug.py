import pytest
from repo.discount import calculate_discount

def test_silver_no_discount_at_100():
    assert calculate_discount(100, "silver") == 100

def test_gold_no_discount_at_100():
    assert calculate_discount(100, "gold") == 100

def test_silver_discount_above_100():
    assert calculate_discount(150, "silver") == 150 * 0.90

def test_gold_discount_above_100():
    assert calculate_discount(200, "gold") == 200 * 0.80
