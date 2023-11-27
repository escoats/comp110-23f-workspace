"""Courses."""

__author__ = "730659395"


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    '''
    def __init__(self, init_name, init_level, init_prereqs):
        self.name = init_name
        self.level = init_level
        self.prerequisites = init_prereqs
    
        '''
    def is_valid_course(self, prereq: str) -> bool:
        if (self.level >= 400) and (prereq in self.prerequisites):
            return True
        else:
            return False


def find_courses(catalog: list[Course], prereq: str) -> list[str]:
    names: list[Course] = []
    for c in catalog:
        if (c.level > 400) and (prereq in c.prerequisites):
            names.append(c.name)
    return names

bio: Course = Course()
bio.prerequisites = ["chem"]
bio.level = 500
bio.name = "biology"

print(bio.is_valid_course("chem"))
find_courses([bio], "chem")