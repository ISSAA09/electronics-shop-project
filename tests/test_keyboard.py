import pytest
from src.keyboard import Keyboard


@pytest.fixture
def testing_data():
    """ Определяем тестовые данные экземпляра класса Phone """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_init(testing_data):
    """ Тест на проверку корректности инициализации экземпляра класса Phone """
    assert testing_data.name == "Dark Project KD87A"
    assert testing_data.language == 'EN'


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_object_has_no_setter():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'
    assert "property 'language' of 'Keyboard' object has no setter"
