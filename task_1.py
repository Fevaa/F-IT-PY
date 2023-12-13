# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Pail:
    def __init__(self, fullness: int, volume: int):
        """
        Создание и подготовка к работе объекта "Бак"

        :param fullness: Наполненность бака
        :param volume: Объем бака

        """
        if not isinstance(fullness, (int)):
            raise TypeError("Объем бака должен быть типа int")
        if fullness <= 0:
            raise ValueError("Объем бака должен быть положительным числом")
        self.fullness = fullness

        if not isinstance(volume, (int)):
            raise TypeError("Объем бака должен быть int")
        if volume < 0:
            raise ValueError("Объем бака не может быть отрицательным числом")
        self.volume = volume

        def fullness_pail(self) -> bool:
            """
            Функция которая проверяет является ли бак пустым

            Примеры:
            >>> pail = Pail(460, 60)
            >>> pail.fullness_pail()
            """
            ...

        def remove_garbage_from_pail(self, garbage_pail: int) -> None:
            """
            Извлечение мусора из бака.

            :param garbage_pail: Объем извлекаемого мусора
            :raise ValueError: Если количество извлекаемого мусора превышает объем мусора в баке, то возвращается ошибка.

            :return: Объем извлеченного мусора

            Примеры:
            >>> pail = Pail(200, 350)
            >>> pail.remove_garbage_from_pail(100)
            """
            ...


class Door:
    def __init__(self, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Дверь"

        :param color: Цвет двери
        :param material: Материал двери

        """
        if not isinstance(color, (str)):
            raise TypeError("Цвет двери должен быть типа str")

        if not isinstance(material, (str)):
            raise TypeError("Материал двери должен быть str")

        def color_door(self) -> bool:
            """
            Функция которая проверяет цвет двери
            """
            ...

        def material_door(self) -> bool:
            """
            Функция которая проверяет материаол двери.

            """
            ...

class Wardrobe:
    def __init__(self, fullness: int, height: int):
        """
        Создание и подготовка к работе объекта "Гардероб"

        :param fullness: Количество вещей в гардеробе
        :param height: Высота гардероба

        """
        if not isinstance(fullness, (int)):
            raise TypeError("Количество вещей в гардеробе должно быть типа int")
        if fullness <= 0:
            raise ValueError("Количество вещей в гардеробе должно быть положительным числом")
        self.fullness = fullness

        if not isinstance(height, (int)):
            raise TypeError("Высота гардероба должна быть int")
        if volume < 0:
            raise ValueError("Высота гардероба не может быть отрицательным числом")
        self.volume = volume

        def fullness_wardrobe(self) -> bool:
            """
            Функция которая проверяет есть ли в гардеробе вещи

            """
            ...

        def heihgt_wardrobe(self) -> bool:
            """
            Функция которая проверяет высоту гардероба.

            """
            ...
        




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
