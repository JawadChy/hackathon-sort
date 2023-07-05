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

# List of hackathons
hackathons = [hackathon1, hackathon2, hackathon3, hackathon4, hackathon5]

print("How would you like to sort the hackathons? Alphabetically or by date?")
print("Enter '1' for alphabetical or '2' for date : ")

userInput = input()

while userInput != "1" and userInput != "2":
    print("Unrecognized input. Please enter '1' for alphabetical or '2' for date : ")
    userInput =input()

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