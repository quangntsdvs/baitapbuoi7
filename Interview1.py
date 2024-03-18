class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (3 * stack_size)
        self.pointers = [0, stack_size, 2 * stack_size]

    def push(self, stack_num, value):
        if self.pointers[stack_num] < (stack_num + 1) * self.stack_size:
            self.array[self.pointers[stack_num]] = value
            self.pointers[stack_num] += 1
        else:
            print("Stack Overflow")

    def pop(self, stack_num):
        if self.pointers[stack_num] > stack_num * self.stack_size:
            self.pointers[stack_num] -= 1
            value = self.array[self.pointers[stack_num]]
            self.array[self.pointers[stack_num]] = None
            return value
        else:
            print("Stack Underflow")
            return None

    def peek(self, stack_num):
        if self.pointers[stack_num] > stack_num * self.stack_size:
            return self.array[self.pointers[stack_num] - 1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self, stack_num):
        return self.pointers[stack_num] == stack_num * self.stack_size

# Example usage:
stacks = ThreeStacks(3)

stacks.push(0, 1)
stacks.push(0, 2)
stacks.push(1, 5)
stacks.push(2, 9)

print(stacks.pop(0))  
print(stacks.pop(1))  
print(stacks.pop(2))  

print(stacks.peek(0))  
print(stacks.peek(1))  
print(stacks.peek(2))  

print(stacks.is_empty(0))  
print(stacks.is_empty(1)) 
print(stacks.is_empty(2)) 
