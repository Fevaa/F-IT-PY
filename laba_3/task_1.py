class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.name}. Author: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer")
        if value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        return f"PaperBook: {self.name}. Author: {self.author}. Pages: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration must be a number")
        if value <= 0:
            raise ValueError("Duration must be a positive number")
        self._duration = value

    def __str__(self):
        return f"AudioBook: {self.name}. Author: {self.author}. Duration: {self.duration}"