"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

exmp_1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert exmp_1.calculate_total_price() == 200000


def test_apply_discount():
    assert 10000 * Item.pay_rate == exmp_1.price
    exmp_1.pay_rate = 0.8
    exmp_1.apply_discount()
    assert exmp_1.price == 8000.0


def test_name():
    assert exmp_1.name == "Смартфон"
    exmp_1.name = 'СуперСмартфон'
    assert exmp_1.name == "СуперСмарт"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

