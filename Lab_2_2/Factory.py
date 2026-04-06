class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def __init__(self):
        # Alustame ID-ga 0
        self.next_id = 0

    def create_person(self, name):
        # Loome uue Person objekti kasutades praegust ID-d
        person = Person(self.next_id, name)

        # Suurendame ID-d järgmise korra jaoks
        self.next_id += 1

        return person


# Kontrollimine
factory = PersonFactory()

p1 = factory.create_person("Anna")
p2 = factory.create_person("Mark")

print(f"{p1.id} {p1.name}")
print(f"{p2.id} {p2.name}")