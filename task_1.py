# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Pail:
    def __int__(self, fullness: int, volume: int):
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




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()