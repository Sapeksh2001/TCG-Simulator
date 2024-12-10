global null, normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy

normal=  {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":0.5,"Ghost":0,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}
fire=    {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":1, "Grass":2, "Ice":2,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":2,"Rock":0.5,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":2,"Fairy":1}
water=   {"Normal":1, "Fire":2, "Water":0.5, "Electric":1, "Grass":0.5, "Ice":1,"Fighting":1, "Poison":1, "Ground":2,"Flying":1,"Psychic":1,"Bug":1,"Rock":2,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":1,"Fairy":1}
electric={"Normal":1, "Fire":1, "Water":2, "Electric":0.5, "Grass":0.5, "Ice":1,"Fighting":1, "Poison":1, "Ground":0,"Flying":2,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":1,"Fairy":1}
grass=   {"Normal":1, "Fire":0.5, "Water":2, "Electric":1, "Grass":0.5, "Ice":1,"Fighting":1, "Poison":0.5, "Ground":2,"Flying":0.5,"Psychic":1,"Bug":0.5,"Rock":2,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":0.5,"Fairy":1}
ice=     {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":1, "Grass":2, "Ice":0.5,"Fighting":1, "Poison":1, "Ground":2,"Flying":2,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":1,"Steel":0.5,"Fairy":1}
fighting={"Normal":2, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":2,"Fighting":1, "Poison":0.5, "Ground":1,"Flying":0.5,"Psychic":0.5,"Bug":0.5,"Rock":2,"Ghost":0,"Dragon":1,"Dark":2,"Steel":2,"Fairy":0.5}
poison=  {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":2, "Ice":1,"Fighting":1, "Poison":0.5, "Ground":0.5,"Flying":1,"Psychic":1,"Bug":1,"Rock":0.5,"Ghost":0.5,"Dragon":1,"Dark":1,"Steel":0,"Fairy":2}
ground=  {"Normal":1, "Fire":2, "Water":1, "Electric":2, "Grass":0.5, "Ice":1,"Fighting":1, "Poison":2, "Ground":1,"Flying":0,"Psychic":1,"Bug":0.5,"Rock":2,"Ghost":1,"Dragon":1,"Dark":1,"Steel":2,"Fairy":1}
flying=  {"Normal":1, "Fire":1, "Water":1, "Electric":0.5, "Grass":2, "Ice":1,"Fighting":2, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":2,"Rock":0.5,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}
psychic= {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":2, "Poison":2, "Ground":1,"Flying":1,"Psychic":0.5,"Bug":1,"Rock":1,"Ghost":1,"Dragon":1,"Dark":0,"Steel":0.5,"Fairy":1}
bug=     {"Normal":1, "Fire":0.5, "Water":1, "Electric":1, "Grass":2, "Ice":1,"Fighting":0.5, "Poison":0.5, "Ground":1,"Flying":0.5,"Psychic":2,"Bug":1,"Rock":1,"Ghost":0.5,"Dragon":1,"Dark":2,"Steel":0.5,"Fairy":0.5}
rock=    {"Normal":1, "Fire":2, "Water":1, "Electric":1, "Grass":1, "Ice":2,"Fighting":0.5, "Poison":1, "Ground":0.5,"Flying":2,"Psychic":1,"Bug":2,"Rock":1,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}
ghost=   {"Normal":0, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":2,"Bug":1,"Rock":1,"Ghost":2,"Dragon":1,"Dark":0.5,"Steel":1,"Fairy":1}
dragon=  {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":1,"Steel":0.5,"Fairy":0}
dark=    {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":0.5, "Poison":1, "Ground":1,"Flying":1,"Psychic":2,"Bug":1,"Rock":1,"Ghost":2,"Dragon":1,"Dark":0.5,"Steel":1,"Fairy":0.5}
steel=   {"Normal":1, "Fire":0.5, "Water":0.5, "Electric":0.5, "Grass":1, "Ice":2,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":2,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":2}
fairy=   {"Normal":1, "Fire":0.5, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":2, "Poison":0.5, "Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":2,"Steel":0.5,"Fairy":1}
null=    {"Normal":1, "Fire":1, "Water":1, "Electric":1, "Grass":1, "Ice":1,"Fighting":1, "Poison":1, "Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":1,"Dark":1,"Steel":1,"Fairy":1}

def typeeffect(first, second={}):
    global normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy
    if second == {}:
        second = null
    elif second == "Normal":
        second = normal
    elif second == "Fighting":
        second = fighting
    elif second == "Flying":
        second = flying
    elif second == "Poison":
        second = poison
    elif second == "Ground":
        second = ground
    elif second == "Rock":
        second = rock
    elif second == "Bug":
        second = bug
    elif second == "Ghost":
        second = ghost
    elif second == "Steel":
        second = steel
    elif second == "Fire":
        second = fire
    elif second == "Water":
        second = water
    elif second == "Grass":
        second = grass
    elif second == "Electric":
        second = electric
    elif second == "Psychic":
        second = psychic
    elif second == "Ice":
        second = ice
    elif second == "Dragon":
        second = dragon
    elif second == "Dark":
        second = dark
    elif second == "Fairy":
        second = fairy
    elif second == "Null":
        second = null
    else:
        print("Invalid Entry; type does not exist. Please try again.")
        return 0

    if first == "Normal":
        first = normal
    elif first == "Fighting":
        first = fighting
    elif first == "Flying":
        first = flying
    elif first == "Poison":
        first = poison
    elif first == "Ground":
        first = ground
    elif first == "Rock":
        first = rock
    elif first == "Bug":
        first = bug
    elif first == "Ghost":
        first = ghost
    elif first == "Steel":
        first = steel
    elif first == "Fire":
        first = fire
    elif first == "Water":
        first = water
    elif first == "Grass":
        first = grass
    elif first == "Electric":
        first = electric
    elif first == "Psychic":
        first = psychic
    elif first == "Ice":
        first = ice
    elif first == "Dragon":
        first = dragon
    elif first == "Dark":
        first = dark
    elif first == "Fairy":
        first = fairy
    elif first == "Null":
        first = null
    else:
        print("Invalid Entry; type does not exist. Please try again.")
        return 0

    timesone = []
    timestwo = []
    timeshalf = []
    timesquart = []
    timesfour = []
    timeszero = []

    for typing in first:
        effectiveness = (first[typing] * 10) * (second[typing] * 10)
        if effectiveness == 400:
            timesfour.append(typing)
        elif effectiveness == 200:
            timestwo.append(typing)
        elif effectiveness == 100:
            timesone.append(typing)
        elif effectiveness == 50:
            timeshalf.append(typing)
        elif effectiveness == 25:
            timesquart.append(typing)
        elif effectiveness == 0:
            timeszero.append(typing)
        else:
            print("An error occured. Please try again.")
            return 0

    print("\nx4:")
    if len(timesfour) == 0:
        print("None")
    else:
        for four in timesfour:
            print(four)

    print("\nx2:")
    if len(timestwo) == 0:
        print("None")
    else:
        for two in timestwo:
            print(two)
            
    print("\nx1:")
    if len(timesone) == 0:
        print("None")
    else:
        for one in timesone:
            print(one)

    print("\nx0.5:")
    if len(timeshalf) == 0:
        print("None")
    else:
        for half in timeshalf:
            print(half)
    print("\nx0.25:")
    if len(timesquart) == 0:
        print("None")
    else:
        for quart in timesquart:
            print(quart)
    print("\nx0:")
    if len(timeszero) == 0:
        print("None")
    else:
        for zero in timeszero:
            print(zero)
    return 1
    
types = input("Enter types:   ").split()
if len(types) == 0:
    print("Invalid Entry. Please try again.")
elif len(types) == 1:
    typeeffect(types[0])
else:
    typeeffect(types[0], types[1])
