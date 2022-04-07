class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def printAnimals(self):
        if len(self.cats) == 0 or len(self.dogs) == 0:
            print("There is no animal in the Shelter")
        else:
            for i in self.cats:
                print(i, end = " ")
            for i in self.dogs:
                print(i, end = " ")

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        elif type == 'Dog':
            self.dogs.append(animal)
        else:
            return "Invalid input"

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
            return result
        else:
            result = self.cats.pop(0)
            return result

customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
customQueue.printAnimals()

print()

print(customQueue.dequeueDog())
print(customQueue.dequeueAny())

print()
customQueue.printAnimals()