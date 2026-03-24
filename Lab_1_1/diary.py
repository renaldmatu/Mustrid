class Diary:
    def __init__(self):
        self.entries = []
        self.counter = 0

    def add_entry(self, text):
        self.counter += 1
        entry = f"{str(self.counter)}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        if 0 < index < len(self.entries):
            del self.entries[index]
        else:
            print("Vigane tekst")

    def save(self, filename):
        with open(filename, "w") as file:
            for entry in self.entries:
                file.write(entry + "\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.entries = [line.strip() for line in file]

        self.counter = len(self.entries)

    def print_statistics(self):
        count = len(self.entries)
        print("Sissekannete arv:", count)

        if count == 0:
            print("Keskmine tähemärkide arv sissekandes: 0")
        else:
            average = sum(len(entry) for entry in self.entries) / count
            print("Keskmine tähemärkide arv sissekandes:", average)

    def __str__(self):
        return "\n".join(self.entries)
