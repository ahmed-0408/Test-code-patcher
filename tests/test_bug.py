import pytest
from repo.discount import calculate_discount

def test_no_discount_at_exact_100_silver():
    assert calculate_discount(100, "silver") == 100

def test_no_discount_at_exact_100_gold():
    assert calculate_discount(100, "gold") == 100

def test_discount_above_100_silver():
    result = calculate_discount(101, "silver")
    assert pytest.approx(result, 0.0001) == 101 * 0.90

def test_discount_above_100_gold():
    result = calculate_discount(101, "gold")
    assert pytest.approx(result, 0.0001) == 101 * 0.80

def test_no_discount_below_100():
    assert calculate_discount(99, "silver") == 99
    assert calculate_discount(99, "gold") == 99
