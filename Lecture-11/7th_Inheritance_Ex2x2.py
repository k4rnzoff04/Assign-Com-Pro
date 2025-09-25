class Dog:
    species = 'Mammal'

    def calAge(self, age):
        print(f"Dog age is {age*3}")

class SomeBread(Dog):
    pass

class SomeOtherBread(Dog):
    species = 'Reptile'
    def calAge(self, age):
        print(f"Dog Age is {age*4}")

frank = SomeBread()
print(frank.species)
frank.calAge(5)

beans = SomeOtherBread()
print(beans.species)
beans.calAge(5)
        