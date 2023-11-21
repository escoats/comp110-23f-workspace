"""Courses."""

__author__ = "730659395"


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def __init__(self, init_name, init_level, init_prereqs):
        self.name = init_name
        self.level = init_level
        self.prerequisites = init_prereqs
    
    def is_valid_self(self, prereq: str) -> bool:
        if (self.level >= 400) and (prereq in self.prerequisites):
            return True
        else:
            return False


def find_courses(catalog: list[Course], prereq: str) -> list[str]:
    names: list[Course] = []
    for course in catalog:
        if (course.level > 400) and (prereq in course.prerequisites):
            names.append(course.name)

