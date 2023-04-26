# Function to print out the seven days of the week, with the corresponding messages
def calendar():
    semaines = ["lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche"]
    index = 0
    for jour in semaines:
        if index >= 1 or index <= 4:
            print(jour[index], "Au travail")
        elif index == 5:
            print(jour[index], "Chouette c'est vendredi")
        elif index == 6:
            print(jour[index], "Repos ce week-end")
        index += 1

# Resolution
calendar()