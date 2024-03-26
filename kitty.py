class Cat:
    def __init__(self, name):
        self.name = name

    def meo(self):
        print(self.name, "meo meo meo meo meo meo")


cat = Cat("cucumber:")
cat.meo()