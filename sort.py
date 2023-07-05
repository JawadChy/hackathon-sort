# This challenge never provided a list of hackathons to sort.
# I am using this made up list of hackathons to sort

from datetime import date, datetime

class Hackathon:
    def __init__(self, name, date):
        self.name = name
        self.date = date

def sortAlphabetically(someList):
    someList.sort(key=lambda hackathon: hackathon.name)

def sortByDate(someList):
    someList.sort(key=lambda hackathon: hackathon.date)
    

# Default set of hackathons. I made these up on the sport
# date(yyyy, mm, dd)
hackathon1 = Hackathon("Jawad's Ultimate Hackathon!", date(2023,8, 2))
hackathon2 = Hackathon("Microsoft New Year Hackathon", date(2024, 1, 6))
hackathon3 = Hackathon("Bing's Spring Hackathon", date(2023, 5, 1))
hackathon4 = Hackathon("Alex's Birthday Hackathon", date(2024, 1, 1))
hackathon5 = Hackathon("Pancake Hacks", date(2023, 9, 26))
hackathon6 = Hackathon("ChrisTM Hackathon", date(2023, 5, 31))

# Default list of hackathons
defaultHackathons = [hackathon1, hackathon2, hackathon3, hackathon4, hackathon5]
newHackathons = []


print("How would you like to sort the hackathons? Alphabetically or by date?")
print("Enter '1' for alphabetical or '2' for date : ")

userInput = input()

while userInput != "1" and userInput != "2":
    print("Unrecognized input. Please enter '1' for alphabetical or '2' for date : ")
    userInput = input()

print()
print("type '1' if you want to work with the default hackathon list, and type '2' if you want to work with a new list : ")

userInput2 = input()

while userInput2 != "1" and userInput != "2":
    print("Unrecognized input. Please enter '1' for default list sorting or '2' for new list sorting : ")
    userInput2 = input()

if userInput2 == "1":
    hackathons = defaultHackathons
else:
    hackathons = newHackathons

addMoreHackathons = False

print()
print("Type 'y' if you want to add more hackathons to the current list, or type 'n' to continue to sorting : ")
userInput3 = input()

while userInput3 != "y" and userInput != "n":
    print("Unrecognized input. Please enter 'y' to add a value to the list, or type 'n' to continue with adding a new value : ")
    userInput3 = input()
    if userInput3 == "y":
        # Taking in values of new hackathon to add
        hackathonName = input("Enter the name of the hackathon to add : ")
        hackathonYear = int(input("Enter the year the hackathon occurs : "))
        hackathonMonth = int(input("Enter the month the hackathon occurs : "))
        hackathonDay = int(input("Enter the day the hackathon occurs : "))
        hackathonDate = date(hackathonYear, hackathonMonth, hackathonDay)
        # Make a hackathon object with this given information
        hackathonToAdd = Hackathon(hackathonName, hackathonDate)
        # Actually append to hackathons list
        hackathons.append(hackathonToAdd)
        print()
        print("Hackathon added to list.")
        print("Type 'y' if you want to add more hackathons to the current list, or type 'n' to continue to sorting : ")

if userInput == "1":
    sortAlphabetically(hackathons)
    print()
    print("LIST OF HACKATHONS SORTED ALPHABETICALLY (Hackathon Name and Date yyyy-mm-dd)")
    for hackathon in hackathons:
        print(f"{hackathon.name} is occuring in {hackathon.date}")
else:
    sortByDate(hackathons)
    print()
    print("LIST OF HACKATHONS SORTED BY DATE (Hackathon Name and Date yyyy-mm-dd)")
    for hackathon in hackathons:
        print(f"{hackathon.name} is occuring in {hackathon.date}")