import pytest
from src.keyboard import Keyboard


def test_init():
    """ Тест на проверку корректности инициализации экземпляра класса Keyboard """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == "Dark Project KD87A"
    assert kb.language == 'EN'


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
