class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def enqueue(self, value):
        if self.isEmpty:
            self.start = Node(value)
        else:
            new_end = Node(value)
            self.end.next = new_end
            self.end = new_end

    def isEmpty(self):
        if self.start == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            value = self.start
            self.start = self.start.next
            return value

    def peek(self):
        if not self.isEmpty():
            return self.start.value
        
fronta = Queue()