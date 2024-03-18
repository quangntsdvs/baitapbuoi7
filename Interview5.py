class AnimalShelter:
    def __init__(self):
        self.cat_queue = []
        self.dog_queue = []
        self.order = 0

    def enqueue(self, animal, species):
        self.order += 1
        if species == 'cat':
            self.cat_queue.append((animal, self.order))
        elif species == 'dog':
            self.dog_queue.append((animal, self.order))
        else:
            raise ValueError("Invalid species")

    def dequeueAny(self):
        if not self.cat_queue and not self.dog_queue:
            return None
        elif not self.cat_queue:
            return self.dog_queue.pop(0)[0]
        elif not self.dog_queue:
            return self.cat_queue.pop(0)[0]

        cat_order, _ = self.cat_queue[0]
        dog_order, _ = self.dog_queue[0]

        if cat_order < dog_order:
            return self.cat_queue.pop(0)[0]
        else:
            return self.dog_queue.pop(0)[0]

    def dequeueDog(self):
        if not self.dog_queue:
            return None
        return self.dog_queue.pop(0)[0]

    def dequeueCat(self):
        if not self.cat_queue:
            return None
        return self.cat_queue.pop(0)[0]

# Example 
animal_shelter = AnimalShelter()

animal_shelter.enqueue("cat1", "cat")
animal_shelter.enqueue("dog1", "dog")
animal_shelter.enqueue("cat2", "cat")
animal_shelter.enqueue("cat3", "cat")
animal_shelter.enqueue("dog2", "dog")
animal_shelter.enqueue("any1", "any")
animal_shelter.enqueue("dog3", "dog")
animal_shelter.enqueue("any2", "any")
animal_shelter.enqueue("any3", "any")

print(animal_shelter.dequeueAny())  
print(animal_shelter.dequeueDog())  
print(animal_shelter.dequeueCat()) 
