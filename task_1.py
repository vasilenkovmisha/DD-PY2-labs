class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError(f"Неверный номер страницы: {pages!r}")
        else:
            raise ValueError("Номер страницы должен быть числом")

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц {self.pages}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}. Количество страниц {self.pages}'


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise ValueError(f'Длительность аудио книги неверная: {duration!r}')
        else:
            raise ValueError('Не указана длительность')

    def __str__(self):
        back_str = super().__str__()
        return f'{back_str}. Длительность {self.duration}'

    def __repr__(self):
        back_rep = super().__repr__()
        return f'{back_rep}. Длительность {self.duration}'


if __name__ == "__main__":
    book = PaperBook("Пост", "Дмитрий Глуховский", 432)
    print(book)
    book_1 = AudioBook("Мастер и Маргарита", "Михаил Афанасьевич Булгаков", 2.35)
    print(book_1)
