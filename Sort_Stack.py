"""
The function takes a single argument, a stack object.
The function should sort the elements in the stack in ascending order (the lowest value will
be at the top of the stack) using only one additional stack
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(stack_input):
    sorted_s = Stack()

    while  not stack_input.is_empty():
        temp =stack_input.pop()        # Pop the top element from the input stack and store it
        while not sorted_s.is_empty() and sorted_s.peek()>temp:
            stack_input.push(sorted_s.pop())
        sorted_s.push(temp)

    while not sorted_s.is_empty():
        stack_input.push(sorted_s.pop())

    return stack_input


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()
