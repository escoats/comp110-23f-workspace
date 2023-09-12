'''testing conditionals with low card example'''

'''
low_card: int = 5
current_card: int = 2

if current_card < low_card:
    low_card = current_card
else: 
    print(str(current_card), "is not the low card")

print("the low card is", low_card)
'''

'''
# if statements
my_number_string: str = input('guess a number: ')
my_number: int = int(my_number_string)

if my_number == 10:
    print('correct')
else: 
    print('incorrect')
'''

# 9/12/2023  - elifs (behave in same way)
name: str = input('Name? ')
if len(name) > 6:
    print("Do you have a nickname?")
elif name == "Alyssa":
        print("I love COMP110!")
else: print("Nice to meet you,", name)

'''
else:
    if name == "Alyssa":
        print("I love COMP110!")
    else: 
        print("Nice to meet you,", name)'''