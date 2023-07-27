import pytest
from src.phone import Phone
from src.phone import Item


@pytest.fixture
def testing_data():
    """ Определяем тестовые данные экземпляра класса Phone """
    phone1 = Phone("Apple", 150000, 10, 2)
    return phone1


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Phone """
    assert testing_data.name == "Apple"
    assert testing_data.price == 150000
    assert testing_data.quantity == 10
    assert testing_data.number_of_sim == 2


def test_str(testing_data):
    """
    Тест проверяет корректность вывода метода str
    в формате 'object_name'
    """
    assert str(testing_data) == 'Apple'


def test_repr(testing_data):
    """
        Тест проверяет корректность вывода строки для отладки в формате
        "ClassName('object_name', object_price, object_quantity, object_num_of_sim)"
        """
    assert repr(testing_data) == "Phone('Apple', 150000, 10, 2)"


def test_number_of_sim(testing_data):
    """ Тест на неотрицательное целое число сим-карт в телефоне """
    with pytest.raises(ValueError):
        testing_data.number_of_sim = -1
        testing_data.number_of_sim = 0
        testing_data.number_of_sim = 1.2


def test_item_and_phone_addition():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14 Pro Max", 120_000, 5, 2)
    assert item1 + phone1 == 25


def test_phone_and_phone_addition():
    phone1 = Phone("iPhone 14", 180_000, 6, 1)
    phone2 = Phone("Samsung Galaxy S23", 90_000, 6, 8)
    assert phone1 + phone2 == 12


def test_add_method_with_invalid_type():
    phone1 = Phone("iPhone 14 Pro Max", 120000, 7, 1)
    with pytest.raises(TypeError):
        phone1 + "test"

