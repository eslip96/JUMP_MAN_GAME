class DataCol:
    def __init__(self):
        self.elements = []

    def add(self, item):
        self.elements.append(item)

    def pop(self):
        return None

    def size(self):
        return len(self.elements)


class Stack(DataCol):
    def __init__(self):
        super().__init__()

    def pop(self):
        if self.size() > 0:
            return self.elements.pop()
        else:
            return None


class Queue(DataCol):
    def __init__(self):
        super().__init__()

    def pop(self):
        if self.size() > 0:
            return self.elements.pop(0)
        else:
            return None


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.elements)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = Queue()
queue.add('a')
queue.add('b')
queue.add('c')
print(queue.elements)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
