# Function to print out the seven days of the week, with the corresponding messages
def calendar():
    semaines = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    index = 0
    for jour in semaines:
        index += 1
        if index <= 4:
            print(f"{jour}: Au travail")
        elif index == 5:
            print(f"{jour}: Chouette c'est vendredi")
        elif index == 6 or 7:
            print(f"{jour}: Repos ce week-end")

# Resolution
calendar()