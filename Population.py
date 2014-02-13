import random
from path import Path

class Population:
    def __init__(self, elements, path_finder, max_child):
        self.elements = elements
        self.path_finder = path_finder
        self.max_child = 0

    def crossing(self, element1, element2):
        sub_path_1 = element1[:self.divide_point(len(element1))]
        sub_path_2 = element2[len(element2) - self.divide_point(len(element2)):]
        child_path = Path(sub_path_1 + self.path_finder.find_path(sub_path_1[-1], sub_path_2[0]) + sub_path_2)
        child_path.remove_cycles()
        self.add_element(child_path)

    def divide_point(self, max):
        "determine divide point of mutate routes"
        r = random.uniform(1 / (max + 1), 1)
        return int(1 / r - 1)

    def add_element(self, new_element):
        self.elements += new_element
        self.elements.sort()



