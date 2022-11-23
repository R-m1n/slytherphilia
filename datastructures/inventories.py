from array import array, typecodes
from typing import Any


class Array():
    def __init__(self, typecode: str) -> None:
        if not (typecode in typecodes):
            raise ValueError(f"'{typecode}' is not a valid typecode.")

        self.typecode = typecode
        self.array = array(typecode)

    def append(self, item: Any) -> None:
        self.array.append(item)

    def remove(self, item: Any = None, index: int = None) -> None:
        if item != None and index != None:
            return

        elif item != None:
            temp = array(self.typecode)
            for i in self.array:
                if i != item:
                    temp.append(i)

            self.array = temp

        elif index != None:
            if abs(index) > len(self):
                raise IndexError("index out of range!")

            if index < 0:
                index += len(self)

            temp = array(self.typecode)
            for i in range(len(self)):
                if i != index:
                    temp.append(self.array[i])

            self.array = temp

    def insert(self, index: int, item: Any) -> None:
        self.array.insert(index, item)

    def empty(self) -> bool:
        return len(self) == 0

    def index(self, item: Any) -> int:
        return self.array.index(item)

    def range(self, start: int, end: int) -> Any:
        temp = Array(self.typecode)
        for i in self.array.tolist()[start: end]:
            temp.append(i)

        return temp

    def reverse(self) -> Any:
        temp = array(self.typecode)
        for i in self.array.tolist()[::-1]:
            temp.append(i)

        self.array = temp

    def __str__(self) -> str:
        return f"Array('{self.typecode}', {self.array.tolist()})"

    def __repr__(self) -> str:
        return f"{self.array.tolist()}"

    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, index: int) -> int:
        return self.array[index]

    def __contains__(self, item: Any) -> bool:
        return item in self.array


class LinkedList():
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.add_last(item)

    def add_first(self, item: Any) -> None:
        node = self.Node(item)

        if self.empty():
            self.first = self.last = node
            self.size += 1
            return

        node.next = self.first
        self.first.previous = node
        self.first = node
        self.size += 1

    def add_last(self, item: Any) -> None:
        node = self.Node(item)

        if self.empty():
            self.first = self.last = node
            self.size += 1
            return

        self.last.next = node
        node.previous = self.last
        self.last = node
        self.size += 1

    def remove_first(self) -> None:
        if self.empty():
            return

        second = self.first.next
        del second.previous
        self.first = second
        self.size -= 1

    def remove_last(self) -> None:
        if self.empty():
            return

        second_to_last = self.last.previous
        del second_to_last.next
        self.last = second_to_last
        self.size -= 1

    def get_first(self) -> Any:
        return self.first.value

    def get_last(self) -> Any:
        return self.last.value

    def get(self, index: int) -> Any:
        if index >= self.size:
            raise IndexError("index out of range!")

        if index >= 0:
            current = self.first
            for i in range(index):
                current = current.next

        else:
            current = self.last
            for i in range(abs(index) - 2):
                current = current.previous

        return current.value

    def index(self, item: Any) -> int:
        index = 0
        current = self.first
        while current != None:
            if current.value == item:
                return index

            current = current.next
            index += 1

        return -1

    def empty(self):
        return self.size == 0

    def __repr__(self):
        list = []

        current = self.first
        while current != self.last:
            list.append(current.value)
            current = current.next

        list.append(self.last.value)
        return f"{list}"

    def __len__(self):
        return self.size


ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)
ll.add_first(4)
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)

print(ll.get(-1))
