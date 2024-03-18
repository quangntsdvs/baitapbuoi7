class SetOfStacks:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            return None
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return value

# Example
stacks = SetOfStacks(3)

stacks.push(1)
stacks.push(2)
stacks.push(3)

stacks.push(4)

stacks.push(5)
stacks.push(6)
stacks.push(7)

print(stacks.pop())  
print(stacks.pop_at(0))  
