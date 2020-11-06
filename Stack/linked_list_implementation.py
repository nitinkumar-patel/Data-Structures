class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.top is None:  # If the stack is empty, we make the top and bottom pointer both point to the new node
            self.top = new_node
            self.bottom = new_node
        else:  # Otherwise, we make the next of the new node, which was pointing to None, point to the present top and then update the top pointer
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:  # If the stack is empty, we print an appropriate message
            print("Stack empty")
        else:  # Else we make the top pointer point to the next of the top pointer and decrease the length by 1, effectively deleting the top element.
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:  # We make the bottom pointer None if there was only 1 element in the stack and that gets popped
                self.bottom = None

    def print_stack(self):
        if self.top is None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.data, end=' ')
                current_pointer = current_pointer.next
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
