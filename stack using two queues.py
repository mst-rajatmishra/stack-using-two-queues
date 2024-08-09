from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def top(self):
        if self.q1.empty():
            return -1
        # Move elements to q2 except the last one
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        topEle = self.q1.get()
        self.q2.put(topEle)
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return topEle

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        if self.q1.empty():
            return None
        # Move elements to q2 except the last one
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        last = self.q1.get()
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return last

    def is_empty(self):
        return self.q1.empty()

s = Stack()

print('Menu')
print('push <value>')
print('pop')
print('top')
print('exit')

while True:
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'top':
        x = s.top()
        if x == -1:
            print("Stack is empty.")
        else:
            print("Top element is", x)
    elif operation == 'exit':
        break
    else:
        print("Invalid operation. Please try again.")
