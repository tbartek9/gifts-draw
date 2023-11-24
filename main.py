class Person:
    def __init__(self, name):
        self.name = name
        self.exclude_list = []

    def add_exclusion(self, excluded_person):
        self.exclude_list.add(excluded_person)
        
