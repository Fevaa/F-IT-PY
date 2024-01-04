class Transport:
"""Базовый класс для всех транспортных средств."""
    def __init__(self, model: str, year_v: int):
        self.model = model # Приватный атрибут для инкапсуляции
        self.year_v = year_v

    def __str__(self) -> str:
    """Возвращает строковое представление транспортного средства."""
        return f"Транспортное средство: {self.model}, Год выпуска: {self.year_v}"

    def __repr__(self) -> str:
    """Возвращает представление для отладки."""
        return f"{self.__class__.__name__}(модель={self.model!r}, год_выпуска={self.year_v!r})"



class PassengerCar(Transport):
"""Дочерний класс для легковых автомобилей."""
    def __init__(self, model: str, year_v: int, number_of_seats: int):
        super().__init__(model, year_v)
        self.number_of_seats = number_of_seats # Приватный атрибут для инкапсуляции

    def transportation_of_passengers(self) -> str:
    """Возвращает строку с информацией о перевозке пассажиров."""
        return f"{self.model} перевозит пассажиров"

    def __str__(self) -> str:
    """Возвращает строковое представление легкового автомобиля."""
        return f"Легковой автомобиль: {self.model}, Год выпуска: {self.year_v}, Количество мест: {self.number_of_seats}"



class Truck(Transport):
"""Дочерний класс для грузовиков."""
    def __init__(self, model: str, year_v: int, lifting_capacity: float):
        super().__init__(model, year_v)
        self.lifting_capacity = lifting_capacity # Приватный атрибут для инкапсуляции

    def transportation_of_cargo(self) -> str:
    """Возвращает строку с информацией о перевозке груза."""
        return f"{self.model} перевозит груз весом до {self.lifting_capacity} тонн"

    def __str__(self) -> str:
    """Возвращает строковое представление грузовика."""
        return f"Грузовик: {self.model}, Год выпуска: {self.year_v}, Грузоподъемность: {self.lifting_capacity} тонн"
