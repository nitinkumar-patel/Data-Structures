class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1] if self.array else None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i], end=' ')
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
