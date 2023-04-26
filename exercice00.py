semaines = ["lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche"]

def calendar():
    index = 0
    for jour in semaines:
        index += 1
    if index >= 1 or index <= 4:
        print(jour, "Au travail")
    elif index == 5:
        print(jour, "Chouette c'est vendredi")
    else:
        print(jour, "Repos ce week-end")

print(calendar())