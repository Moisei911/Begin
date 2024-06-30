class Cats:
    name = None
    age = None
    ishappy = None

    def set_data(self, name, age, ishappy):
        self.name = name
        self.age = age
        self.ishappy = ishappy

    def get_data(self):
        print("Name:", self.name, "Age:", self.age, "Happiness:", self.ishappy)


cat1 = Cats()
cat1.set_data("barsik.", 3, False)

cat2 = Cats()
cat2.set_data("vasyan.", 5, True)

cat1.get_data()
cat2.get_data()
input()