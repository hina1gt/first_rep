class Car:

    def __init__(self, model, passenger, tyre):
        self.model = model
        self.passenger = passenger
        self.tyre = tyre

    def move(self):
        return f'{self.model} - {self.passenger} - {self.tyre}'

mercedes = Car('mercedes', 5, 5)
print(mercedes.move())

traktor = Car('traktor', 2, 3)
print(traktor.move())