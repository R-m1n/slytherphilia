from array import array, typecodes
from pprint import pprint
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

    def __str__(self):
        return f"Stack({self.array.tolist()})"

    def __repr__(self):
        return f"{self.array.tolist()}"

    def __len__(self):
        return len(self.array)


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

    def __str__(self):
        return f"Queue({self.array.tolist()})"

    def __repr__(self):
        return f"{self.array.tolist()}"

    def __len__(self):
        return len(self.array)


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

    def __str__(self):
        return f"PriorityQueue({self.array.tolist()})"

    def __repr__(self) -> str:
        return f"{self.array.tolist()}"

    def __len__(self):
        return len(self.array)


class HashChain():
    class Entry():
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value

        def __eq__(self, __o: object) -> bool:
            return self.key == __o.key

    def __init__(self, chains: int = 5) -> None:
        self.__table = [[] for i in range(chains)]
        self.__keys = set()

    def put(self, key: Any, value: Any) -> None:
        index = self.__table_index(key)

        if key in self.__keys:
            self.remove(key)

        self.__table[index].append(self.Entry(key, value))
        self.__keys.add(key)

    def get(self, key: Any, default: Any = None) -> Any:
        if key not in self.__keys:
            return default

        index = self.__table_index(key)
        for entry in self.__table[index]:
            if entry.key == key:
                return entry.value

    def remove(self, key: Any) -> None:
        index = self.__table_index(key)
        self.__table[index].remove(self.Entry(key, None))
        self.__keys.remove(key)

    def keys(self) -> List[Any]:
        return list(self.__keys)

    def items(self) -> List[Any]:
        items = []
        for list in self.__table:
            for entry in list:
                items.append((entry.key, entry.value))

        return items

    def __table_index(self, key):
        return hash(key) % len(self.__table)

    def __repr__(self) -> str:
        return f"{self.items()}"

    def __str__(self) -> str:
        return f"HashChain({self.items()})"

    def __contains__(self, key: Any) -> bool:
        return key in self.__keys


class HashMap():
    class Entry():
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value

        def __eq__(self, __o: object) -> bool:
            return self.key == __o.key

    def __init__(self, capacity: int = 100) -> None:
        self.PRIME = 47
        self.__table = [self.Entry(None, None) for i in range(capacity)]
        self.__keys = set()

    def get_table(self):
        return self.__table

    def put(self, key: Any, value: Any) -> None:
        if key in self.__keys:
            self.__probe(key).value = value

        else:
            index = self.__double_hash(key)
            self.__table[index] = self.Entry(key, value)
            self.__keys.add(key)

    def get(self, key: Any, default: Any = None) -> Any:
        if key not in self.__keys:
            return default

        return self.__probe(key).value

    def remove(self, key: Any) -> None:
        self.__table.remove(self.Entry(key, None))
        self.__keys.remove(key)

    def keys(self) -> List[Any]:
        return list(self.__keys)

    def items(self) -> List[Any]:
        items = []
        for key in self.__keys:
            entry = self.__probe(key)
            items.append((entry.key, entry.value))

        return items

    def __double_hash(self, key):
        hash2 = self.PRIME - (hash(key) % self.PRIME)
        i = 1
        while i < len(self.__table):
            index = (hash(key) + (hash2 * i)) % len(self.__table)
            if self.__table[index] == self.Entry(None, None):
                return index

            index += 1

    def __probe(self, key):
        hash2 = self.PRIME - (hash(key) % self.PRIME)
        i = 1
        while i < len(self.__table):
            index = (hash(key) + (hash2 * i)) % len(self.__table)
            if self.__table[index].key == key:
                return self.__table[index]

            index += 1

    def __repr__(self) -> str:
        items = "{ "
        for key in self.__keys:
            entry = self.__probe(key)
            items += f"{entry.key}: {entry.value}, "

        return f"{items[:-2]}" + " }"

    def __str__(self) -> str:
        return f"HashChain({self.items()})"

    def __contains__(self, key: Any) -> bool:
        return key in self.__keys


class BinaryTree():
    class Node():
        def __init__(self, value: int) -> None:
            self.value = value
            self.right = None
            self.left = None

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        self.__check_value(value)

        if self.root == None:
            self.root = self.Node(value)
            return

        self.__insert(self.root, value)

    def contains(self, value: int) -> bool:
        self.__check_value(value)

        return self.__contains(self.root, value)

    def size(self) -> int:
        return self.__size(self.root)

    def isleaf(self, value: int) -> bool:
        if self.contains(value):
            node = self.__find(self.root, value)
            return node.left == None and node.right == None

    def height(self) -> int:
        return self.__height(self.root)

    def depth(self, value: int) -> int:
        if self.contains(value):
            return self.__depth(self.root, value)

    def empty(self) -> bool:
        return self.root == None

    def max(self) -> int:
        if self.empty():
            return

        current = self.root
        while current.right != None:
            current = current.right

        return current.value

    def min(self) -> int:
        if self.empty():
            return

        current = self.root
        while current.left != None:
            current = current.left

        return current.value

    def sum(self) -> int:
        return self.__sum(self.root)

    def __insert(self, root: Node, value: int):
        if root == None:
            return

        if root.value > value:
            if root.left == None:
                root.left = self.Node(value)

            self.__insert(root.left, value)

        elif root.value < value:
            if root.right == None:
                root.right = self.Node(value)

            self.__insert(root.right, value)

    def __contains(self, root: Node, value: int):
        if root == None:
            return False

        if root.value == value:
            return True

        return self.__contains(root.left, value) or self.__contains(root.right, value)

    def __size(self, root: Node):
        if root == None:
            return 0

        return 1 + self.__size(root.left) + self.__size(root.right)

    def __find(self, root: Node, value: int):
        if root == None:
            return

        if root.value == value:
            return root

        if root.value > value:
            return self.__find(root.left, value)

        if root.value < value:
            return self.__find(root.right, value)

    def __height(self, root: Node):
        if root == None:
            return -1

        return 1 + max(self.__height(root.left), self.__height(root.right))

    def __depth(self, root: Node, value: int):
        if root == None:
            return 0

        if root.value == value:
            return 0

        if root.value > value:
            return 1 + self.__depth(root.left, value)

        if root.value < value:
            return 1 + self.__depth(root.right, value)

    def __sum(self, root: Node):
        if root == None:
            return 0

        return root.value + self.__sum(root.left) + self.__sum(root.right)

    def __check_value(self, value):
        if not isinstance(value, int):
            raise ValueError("this Tree only accepts integer.")


bt = BinaryTree()
bt.insert(8)
bt.insert(2)
bt.insert(9)
bt.insert(12)
bt.insert(4)

print(bt.sum())
