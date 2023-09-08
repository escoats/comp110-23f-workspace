"""Second Memory Diagram"""

val: int = 1
val2: int = val + 3
print(val + 1)
print(val2)

'''
STACK
------                                  OUTPUT
Globals         val | 2                  "2"
                val2 | 4                "4"
'''


"""Example environment diagram problem"""

age: int = 20
year: int = 2023
age_in_2043: int = 2043 - year + age
print("In 2043, you'll be " + str(age_in_2043))

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))