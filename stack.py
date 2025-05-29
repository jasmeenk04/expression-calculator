#Jasmeen Kaur, stack.py

class Stack:
    
    def __init__(self):#list created
        self.stack_items = []

    def isEmpty(self): #checks if it is empty
        return self.stack_items == []

    def push(self, item):
      self.stack_items.append(item)

    def pop(self):
        if len(self.stack_items) == 0:
            return None
        return self.stack_items.pop()
    
    def peek(self):
        if len(self.stack_items) > 0:
            return self.stack_items[-1]
        else:
            return None

    def size(self):
        return len(self.stack_items)

# a driver program for class Stack
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None