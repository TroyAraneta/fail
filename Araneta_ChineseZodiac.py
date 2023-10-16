InputCZS = int(input("Enter a year and know its Chinese Zodiac Sign: "))

CZSigns = ["Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit",
           "Dragon", "Snake", "Horse", "Goat", "Monkey"]

if InputCZS < 0:
    print("Year can't be a negative value.")
elif InputCZS > 9999:
    print("Year can only be 4 digits or less.")
else:
    i = (InputCZS - 1) % 12
    print("Your Year's Chinese Zodiac Sign is", CZSigns[i])
