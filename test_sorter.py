import pytest
from sorter import sort

def test_neither():
    assert sort(50, 50, 50, 10) == "Neither"

def test_bulky_by_volume():
    assert sort(100, 100, 100, 10) == "Bulky"  # volume = 1,000,000

def test_bulky_by_dimension():
    assert sort(150, 20, 20, 5) == "Bulky"

def test_heavy():
    assert sort(20, 20, 20, 20) == "Heavy"

def test_both():
    assert sort(200, 200, 200, 25) == "Both"

def test_edge_cases():
    assert sort(150, 149, 149, 19) == "Bulky"
    assert sort(149, 149, 149, 20) == "Heavy"
    assert sort(100, 100, 100, 19) == "Bulky"  # volume = 1,000,000
