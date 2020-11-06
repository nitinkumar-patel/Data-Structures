class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if not self.length:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        self.length += 1
        return self

    def pop(self):
        if not self.top:
          return None
        if self.top == self.bottom:
          self.bottom = None
        holding_pointer = self.top
        self.top = self.top.next
        self.length -= 1
        return holding_pointer.value

    def print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print('\n')


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('google')
    my_stack.push('udemy')
    my_stack.push('discord')
    my_stack.push('youtube')
    my_stack.push('facebook')
    my_stack.peek()
    my_stack.print_stack()
    my_stack.pop()
    my_stack.print_stack()
    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
