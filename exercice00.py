# Function to print out the seven days of the week, with the corresponding messages
def calendar():
    semaines = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    index = 0
    for jour in semaines:
        index += 1
        if index <= 4:
            print(f"{jour}: Au travail")

# Resolution
calendar()