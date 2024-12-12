# Add most amount of people who share a singular birthday

import random

def getDate(_birthday):
    _birthdate = ["month", "day"]
    if _birthday <= 31:
        _birthdate[0] = "January"
        _birthdate[1] = _birthday
    elif _birthday <= 59:
        _birthdate[0] = "Februrary"
        _birthdate[1] = _birthday-31
    elif _birthday <= 90:
        _birthdate[0] = "March"
        _birthdate[1] = _birthday-59
    elif _birthday <= 120:
        _birthdate[0] = "April"
        _birthdate[1] = _birthday-90
    elif _birthday <= 151:
        _birthdate[0] = "May"
        _birthdate[1] = _birthday-120
    elif _birthday <= 181:
        _birthdate[0] = "June"
        _birthdate[1] = _birthday-151
    elif _birthday <= 212:
        _birthdate[0] = "July"
        _birthdate[1] = _birthday-181
    elif _birthday <= 243:
        _birthdate[0] = "August"
        _birthdate[1] = _birthday-212
    elif _birthday <= 273:
        _birthdate[0] = "September"
        _birthdate[1] = _birthday-243
    elif _birthday <= 304:
        _birthdate[0] = "October"
        _birthdate[1] = _birthday-273
    elif _birthday <= 334:
        _birthdate[0] = "November"
        _birthdate[1] = _birthday-304
    elif _birthday <= 365:
        _birthdate[0] = "December"
        _birthdate[1] = _birthday-334
    if _birthdate[1] == 1 or _birthdate[1] == 21 or _birthdate[1] == 31:
        _birthdate[1] = str(_birthdate[1]) + "st"
    elif _birthdate[1] == 2 or _birthdate[1] == 22:
        _birthdate[1] = str(_birthdate[1]) + "nd"
    elif _birthdate[1] == 3 or _birthdate[1] == 23:
        _birthdate[1] = str(_birthdate[1]) + "rd"
    else:
        _birthdate[1] = str(_birthdate[1]) + "th"
    return _birthdate

print("This program simulates a room of random people with random birthdays (not inluding leapyears), and displays the shared birthdays between them.")

numOfPeople = ""
while numOfPeople == "":
    try:
        numOfPeople = abs(int(input("Enter the number of people in the room: ")))
    except:
        print("That is an invalid input!\n")

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
    currentPersonBirthDate = getDate(birthdays[i])
    
    birthdaysString += f"Person {i+1} was born on {currentPersonBirthDate[0]} {currentPersonBirthDate[1]}. \n"
print(birthdaysString)

duplicateBirthdaysString = ""
duplicateBirthdayCount = 0
for i in range(len(duplicateBirthdays)):
    if len(duplicateBirthdays[i][1]) > 1:
        duplicateBirthdayCount += 1
        currentBirthday = duplicateBirthdays[i][0]
        currentBirthDate = getDate(currentBirthday)
        duplicateBirthdaysString += f"There were {len(duplicateBirthdays[i][1])} people who shared a birthday of {currentBirthDate[0]} {currentBirthDate[1]}: "
        for j in range(len(duplicateBirthdays[i][1])):
            currentPerson = duplicateBirthdays[i][1][j]
            if j == (len(duplicateBirthdays[i][1])-2):
                duplicateBirthdaysString += (f"person {str(currentPerson)}, and ")
            elif j == (len(duplicateBirthdays[i][1])-1):
                duplicateBirthdaysString += (f"person {str(currentPerson)}.")
            else:
                duplicateBirthdaysString += (f"person {str(currentPerson)}, ")
            
        duplicateBirthdaysString += ("\n")
if duplicateBirthdayCount == 0:
    print("There are no shared birthdays.")
elif duplicateBirthdayCount == 1:
    print(f"There is 1 shared birthday:")
else:
    print(f"There are {duplicateBirthdayCount} shared birthdays:")

print(duplicateBirthdaysString)
