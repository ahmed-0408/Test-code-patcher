import pytest
from repo.discount import calculate_discount

def test_no_discount_at_exact_100_silver():
    assert calculate_discount(100, "silver") == 100

def test_no_discount_at_exact_100_gold():
    assert calculate_discount(100, "gold") == 100

def test_discount_above_100_silver():
    price = 150
    expected = price * 0.90
    assert calculate_discount(price, "silver") == expected

def test_discount_above_100_gold():
    price = 200
    expected = price * 0.80
    assert calculate_discount(price, "gold") == expected
