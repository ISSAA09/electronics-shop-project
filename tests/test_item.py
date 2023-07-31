"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, FileDamaged , InstantiateCSVError
import pytest


@pytest.fixture
def testing_data():
    exp_1 = Item("Смартфон", 10000, 20)
    return exp_1


def test_calculate_total_price(testing_data):
    assert testing_data.calculate_total_price() == 200000


def test_apply_discount(testing_data):
    assert 10000 * Item.pay_rate == testing_data.price
    testing_data.pay_rate = 0.8
    testing_data.apply_discount()
    assert testing_data.price == 8000.0


def test_name(testing_data):
    testing_data.name = 'Планшет'
    assert testing_data.name == 'Планшет'
    testing_data.name = 'СуперСмартфон'
    assert testing_data.name == "СуперСмарт"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(testing_data):
    assert repr(testing_data) == "Item('Смартфон', 10000, 20)"


def test_rpr(testing_data):
    assert str(testing_data) == 'Смартфон'


def test_instantiate_from_csv():
    """ Тест на соответствие содержания файла данным из списка"""
    Item.instantiate_from_csv()
    item1 = Item.all[1]
    item2 = Item.all[4]
    assert item1.name == 'Ноутбук'
    assert item2.price == 75
    assert item1.quantity == 3
    assert len(Item.all) == 5


def test_items_addition():
    exp_1 = Item("Смартфон", 10000, 20)
    exp_2 = Item("Ноутбук", 120_000, 5)
    assert exp_1 + exp_2 == 25
    assert exp_1 + exp_1 == 40


def test_add_method_with_invalid_type():
    item_1 = Item("Смартфон", 10000, 20)
    with pytest.raises(ValueError):
        item_1 + 5


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError,):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_damaged():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
