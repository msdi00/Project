class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        s = self.__dict__
        a = (': '.join((i[0], str(i[1]))) for i in filter(lambda x: x[0] != '_id', self.__dict__.items()))
        c = '\n'.join(a)
        return c


class ShopUserView:
    def __str__(self):
        a = (': '.join((i[0], str(i[1]))) for i in self.__dict__.items())
        c = '\n'.join(a)
        return c


class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


if __name__ == '__main__':

    # class Book(ShopItem, ShopGenericView): ...
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
    # на экране увидим строчки:
    # _id: 1
    # _title: Python ООП
    # _author: Балакирев
    # _year: 2022


    # class Book(ShopItem, ShopUserView): ...
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
    # на экране увидим строчки:
    # _title: Python ООП
    # _author: Балакирев
    # _year: 2022