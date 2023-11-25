import random
from person import Person


class GiftsDrawApp:
    def __init__(self):
        self.people = self.get_people_from_user()
        self.occupied = []

        for person in self.people:
            person.result = self.draw_gift_recipient(person)
        self.save_results()

    def get_people_from_user(self):
        people_names = input("Wprowadz imiona(odzielone przecinkiem - imie,imie2,imie3...)): ").split(',')
        people = [Person(name.strip()) for name in people_names]
        self.get_exclusions_from_user(people)
        return people

    def get_exclusions_from_user(self, people):
        for person in people:
            exclusion_input = input(f"Wprowadz osoby zakaznane dla {person}, oddzielone przecinkiem").split(',')
            person.exclude_list = [excludedPerson.strip() for excludedPerson in exclusion_input]

    def draw_gift_recipient(self, person):
        available_choices = [participant.name for participant in self.people if participant != person and participant.name not in self.occupied and participant.name not in participant.exclude_list]
        recipient = random.choice(available_choices)
        self.occupied.append(recipient)
        return recipient

    def save_results(self):
        for person in self.people:
            file_path = f"data/{person.name}_losowanie.txt"
            with open(file_path, "w") as file:
                file.write("wylosowalas/es:"+str(person.result))
