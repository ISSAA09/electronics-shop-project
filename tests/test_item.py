"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

exmp_1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert exmp_1.calculate_total_price() == 200000


def test_apply_discount():
    assert 10000*Item.pay_rate == exmp_1.price
    exmp_1.pay_rate = 0.8
    exmp_1.apply_discount()
    assert exmp_1.price == 8000.0
