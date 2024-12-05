# Change the number of birthdays to purely appending the people who have that birthday if it already exists
import random
numOfPeople = 23
birthdays = []
for i in range(numOfPeople):
    birthdays.append(random.randint(1, 365))
duplicateBirthdays = []
for i in range(numOfPeople):
    repeat = 0
    for j in range(len(duplicateBirthdays)):
        if birthdays[i] == duplicateBirthdays[j][0]:
            duplicateBirthdays[j][1].append((i+1))
    if repeat == 0:
        duplicateBirthdays.append([birthdays[i], [(i+1)]])
        
birthdaysString = "" 
for i in range(numOfPeople):
    birthdaysString += f"Person {i+1}: {birthdays[i]}\n"
print(birthdaysString)


# Add varying capitalization, no semi colon, and a space one the statements depending if its first last, or before last.
# Add the exact day rather than just the number of the year the person was born on. (like January 1st rather than 1)
duplicateBirthdaysString = ""
for i in range(len(duplicateBirthdays)):
    if len(duplicateBirthdays[i][1]) > 1:
        for j in range(len(duplicateBirthdays[i][1])):
            duplicateBirthdaysString += (f"person {str(duplicateBirthdays[i][1][j])}, ")
        duplicateBirthdaysString += (f"have birthdays on {str(duplicateBirthdays[i][0])}. ")
        


print(duplicateBirthdays)
print(duplicateBirthdaysString)
