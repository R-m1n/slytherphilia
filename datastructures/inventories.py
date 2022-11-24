from array import array, typecodes
from typing import Any, List


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

    def contains(self, item: Any) -> bool:
        return self.index(item) != -1

    def empty(self):
        return self.size == 0

    def tolist(self) -> List[Any]:
        list = []

        if self.empty():
            return list

        current = self.first
        for i in range(self.size):
            list.append(current.value)
            current = current.next

        return list

    def reverse(self) -> None:
        temp = self.last
        for i in range(self.size):
            second_to_last = self.last.previous
            self.last.next = second_to_last
            self.last = second_to_last

        self.first = temp

    def middle(self) -> List[Any]:
        if self.size < 3:
            return self.tolist()

        n1 = self.first
        n2 = self.first.next

        counter = 2
        while True:
            n1 = n1.next

            for i in range(counter):
                n2 = n2.next

            if n2 == None:
                return [n1.value]

            elif n2.next == None:
                return [n1.value, n1.next.value]

    def __str__(self):
        return f"LinkedList({self.tolist()})"

    def __repr__(self):
        return f"{self.tolist()}"

    def __len__(self):
        return self.size


class Stack():
    def __init__(self, typecode: str) -> None:
        if not (typecode in typecodes):
            raise ValueError(f"'{typecode}' is not a valid typecode.")

        self.array = array(typecode)

    def push(self, item: Any) -> None:
        self.array.append(item)

    def pop(self) -> Any:
        return self.array.pop()

    def peek(self) -> Any:
        return self.array[-1]

    def empty(self) -> bool:
        return len(self.array) == 0


class Queue():
    def __init__(self, typecode: str) -> None:
        if not (typecode in typecodes):
            raise ValueError(f"'{typecode}' is not a valid typecode.")

        self.array = array(typecode)

    def enqueue(self, item: Any) -> None:
        self.array.append(item)

    def dequeue(self) -> Any:
        return self.array.pop(0)

    def peek(self) -> Any:
        return self.array[0]

    def empty(self) -> bool:
        return len(self.array) == 0


class PriorityQueue():
    def __init__(self, typecode: str) -> None:
        if not (typecode in typecodes):
            raise ValueError(f"'{typecode}' is not a valid typecode.")

        self.array = array(typecode)

    def add(self, item: Any) -> None:
        self.array.append(item)
        self.__bubble_up(item, len(self.array) - 1)

    def remove(self) -> Any:
        return self.array.pop(0)

    def peek(self) -> Any:
        return self.array[0]

    def empty(self) -> bool:
        return len(self.array) == 0

    def __bubble_up(self, item, index):
        if index == 0 or item <= self.array[index - 1]:
            return

        if item > self.array[index - 1]:
            self.__swap(index, index - 1)

        self.__bubble_up(item, index - 1)

    def __swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def __repr__(self) -> str:
        return f"{self.array.tolist()}"
