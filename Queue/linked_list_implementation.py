class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first is None:
            return None
        return self.first.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            print("Queue is empty")
        else:
            self.first = self.first.next
            self.length -= 1
            if self.length == 0:
                self.last = None

    def print_queue(self):
        if self.first is None:
            print("Queue is empty")
        else:
            current_pointer = self.first
            while current_pointer is not None:
                print(current_pointer.data, end=' ')
                current_pointer = current_pointer.next
            print('\n')


if __name__ == '__main__':
    my_stack = Queue()
    my_stack.enqueue('google')
    my_stack.enqueue('udemy')
    my_stack.enqueue('discord')
    my_stack.enqueue('youtube')
    my_stack.enqueue('facebook')
    my_stack.peek()
    my_stack.print_queue()  # google udemy discord youtube facebook
    my_stack.dequeue()
    my_stack.print_queue()  # udemy discord youtube facebook
    my_stack.dequeue()
    my_stack.dequeue()
    my_stack.print_queue()  # youtube facebook
