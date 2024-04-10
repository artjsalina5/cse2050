class Animal:
    """Represents a non-specific animal"""
    def __init__(self, name="It"):
        """Instantiates a new animal with a name"""
        self.name = name

    def speak(self):
        """Allows for an error to be caught if speak is not defined elsewhere"""
        raise NotImplementedError("Subclasses must implement this method")

    def reply(self):
        """Calls the speak method"""
        return self.speak()

class Mammal(Animal):
    """Represents a Mammal in animal kingdom"""
    def speak(self):
        return f"{self.name} says HuH!"


class Primate(Mammal):
    """Represents subclass of Mammals that are Primates"""
    def speak(self):
        return f"{self.name} says EE-EE-OOH-OOH"

class ComputerScientist(Primate):
    """"Represents a subclass of Primates that are Computer Scientists"""
    # speak is inherited from primate
    pass

class Cat(Mammal):
    """Represents a subclass of Mammals that are Cats."""
    def speak(self):
        return f"{self.name} says Meow!"
    
# Test Cat Initialization and speak method
cat = Cat("Wilbur")
assert cat.name == "Wilbur", "Cat name initialization failed"
assert cat.speak() == "Wilbur says Meow!", "Cat speak method failed with the name Wilbur"

# Test Animal reply method
assert cat.reply() == "Wilbur says Meow!", "Animal reply method failed using Cat instance with the name Wilbur"

# Testing Mammal class
mammal = Mammal("Brittney")
assert mammal.name == "Brittney", "Mammal name initialization failed"
assert mammal.speak() == "Brittney says HuH!", "Mammal speak method failed"

# Testing Primate class
primate = Primate("George")
assert primate.name == "George", "Primate name initialization failed"
assert primate.speak() == "George says EE-EE-OOH-OOH", "Primate speak method failed"

# Testing ComputerScientist class
cs = ComputerScientist("Alice")
assert cs.name == "Alice", "ComputerScientist name initialization failed"
assert cs.speak() == "Alice says EE-EE-OOH-OOH", "ComputerScientist speak method failed"

