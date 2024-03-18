class QueueViaStacks:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def enqueue(self, value):
        self.stack_push.append(value)

    def dequeue(self):
        if not self.stack_pop:
            if not self.stack_push:
                return None
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop() if self.stack_pop else None

# Example usage:
queue = QueueViaStacks()

queue.enqueue(6)
queue.enqueue(3)
queue.enqueue(7)

print(queue.dequeue()) 
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  
