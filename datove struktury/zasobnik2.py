class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return None
        elif self.top.next == None:
            value = self.top.value
            self.top = None
            return value
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        if not self.isEmpty():
            return self.top.value


zasobnik = Stack()
print(zasobnik.isEmpty())
zasobnik.push(1)
zasobnik.push(2)
print(zasobnik.peek())