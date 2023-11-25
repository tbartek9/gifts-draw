class Person:
    def __init__(self, name):
        self.name = name
        self.exclude_list = []
        self.result = ''

    def add_exclusion(self, excluded_person):
        self.exclude_list.add(excluded_person)

    def __str__(self):
        return self.name

