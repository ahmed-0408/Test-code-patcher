import pytest
from repo.discount import calculate_discount

def test_no_discount_at_exact_100_silver():
    assert calculate_discount(100, "silver") == 100

def test_no_discount_at_exact_100_gold():
    assert calculate_discount(100, "gold") == 100

def test_discount_applies_above_100_silver():
    assert calculate_discount(101, "silver") == pytest.approx(101 * 0.90)

def test_discount_applies_above_100_gold():
    assert calculate_discount(150, "gold") == pytest.approx(150 * 0.80)
