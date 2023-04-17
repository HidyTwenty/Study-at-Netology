class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = 0
        self.current_element = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_list < len(self.list_of_list):
            if self.current_element < len(self.list_of_list[self.current_list]):
                item = self.list_of_list[self.current_list][self.current_element]
                self.current_element += 1
                return item
            else:
                self.current_list += 1
                self.current_element = 0
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()