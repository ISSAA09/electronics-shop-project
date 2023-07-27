from src.item import Item


class Phone(Item):
    """ Класс товара категории Телефон """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self._number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Реализация операции сложения для экземпляров класса Phone и Item.
        Сложение происходит по количеству товара в магазине.
        """
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Нельзя складывать Phone с другими типами кроме себя и Item")
        return self.quantity + other.quantity

    def __repr__(self):
        """
         Возвращает строку для отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value

