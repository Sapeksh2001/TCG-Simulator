import pandas as pd
import os
from tkinter import *
#array in order: normal, fighting, flying, poison, ground, 
#rock, bug, ghost, steel, fire, water, grass, electric
#psychic, ice, dragon, dark, fairy

#----------types to be listed in terms of defensive capabilities----------
normal =   [1,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
fighting = [1,1,2,1,1,0.5,0.5,1,1,1,1,1,1,2,1,1,0.5,2]
flying =   [1,0.5,1,1,0,2,0.5,1,1,1,1,0.5,2,1,2,1,1,1,1]
poison =   [1,0.5,1,0.5,2,1,0.5,1,1,1,1,0.5,1,2,1,1,1,0.5]
ground=    [1,1,1,0.5,1,0.5,1,1,1,1,2,2,0,1,2,1,1,1]
rock=      [0.5,2,0.5,0.5,2,1,1,1,2,0.5,2,2,1,1,1,1,1,1]
bug=       [1,0.5,2,1,0.5,2,1,1,1,2,1,0.5,1,1,1,1,1,1]
ghost=     [0,0,1,0.5,1,1,0.5,2,1,1,1,1,1,1,1,1,2,1]
steel =    [0.5,2,0.5,0,2,0.5,0.5,1,0.5,2,1,0.5,1,0.5,0.5,0.5,1,0.5]
fire=      [1,1,1,1,2,2,0.5,1,0.5,0.5,2,0.5,1,1,0.5,1,1,0.5]
water=     [1,1,1,1,1,1,1,1,0.5,0.5,0.5,2,2,1,0.5,1,1,1]
grass=     [1,1,2,2,0.5,1,2,1,1,2,0.5,0.5,0.5,1,2,1,1,1]
electric=  [1,1,0.5,1,2,1,1,1,0.5,1,1,1,0.5,1,1,1,1,1]
psychic=   [1,0.5,1,1,1,1,2,2,1,1,1,1,1,0.5,1,1,2,1]
ice=       [1,2,1,1,1,2,1,1,2,2,1,1,1,1,0.5,1,1,1]
dragon=    [1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,1,2,2,1,2]
dark =     [1,2,1,1,1,1,2,0.5,1,1,1,1,1,0,1,1,0.5,2]
fairy=     [1,0.5,1,2,1,1,0.5,1,2,1,1,1,1,1,1,0,0.5,1]
nil =      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


typesdict={'normal':normal,'fighting':fighting,'flying':flying,'poison':poison,'ground':ground,'rock':rock,'bug':bug,'ghost':ghost, 'steel':steel,'fire':fire,'water':water,'grass':grass,'electric':electric,'psychic':psychic,'ice':ice,'dragon':dragon,'dark':dark, 'fairy':fairy,'nil':nil}
#--------------------------------------------------------------------------
#empty lists to record down the specific pokemon's type effectiveness, used for pandas
pdnormal = []
pdfighting = []
pdflying = []
pdpoison = []
pdground = []
pdrock = []
pdbug = []
pdghost = []
pdsteel = []
pdfire = []
pdwater = []
pdgrass = []
pdelectric = []
pdpsychic = []
pdice = []
pddragon = []
pddark = []
pdfairy = []
totaltypelist = [pdnormal,pdfighting,pdflying,pdpoison,pdground,pdrock,pdbug,pdghost,pdsteel,pdfire,pdwater,pdgrass,pdelectric,pdpsychic,pdice,pddragon,pddark,pdfairy] #a list to hold the type vulnerability of each type of each pokemon
#--------------------------------------------------------------------------
#function for type effectiveness calculation
def typecalculation():
#function to determine what type it is based on user's input
    def typeinput():
        while True:
            typestring = input("Enter type "+typenostring+' (type "nil" if there is no type):')
            if(typestring.lower() in typesdict):
                pokemontype = typesdict[typestring.lower()]
            else:
                print("Invalid type. Enter again.")
                continue
            #repeat the loop until a valid condition is met
            break
        if(typeno == 0):
            type1list.append(typestring) #append to list of type 1
        elif(typeno == 1):
            type2list.append(typestring) #append to list of type 2
        return pokemontype
#--------------------------------------------------------------------------
    typelist =[]#raw data for collecting the 2 types

    #collect 2 types
    for typeno in range(2):
        typenostring = str(typeno+1)
        pokemontype = typeinput()
        typelist.append(pokemontype)

    #assign the list to their respective types
    type1 = typelist[0]
    type2 = typelist[1]
    
    #total type effectiveness of the pokemon
    typetotal = []
    for num1,num2 in zip(type1,type2):
        typetotal.append(num1*num2)
    return(typetotal)
#--------------------------------------------------------------------------
# Function to handle button click event
def submit():
    # Get the number of Pokémon from the entry widget
    num_pokemon = int(entry_num_pokemon.get())
    
    # Destroy the input window
    input_window.destroy()
    
    # Create a new window to display the results
    result_window = Tk()
    result_window.title("Pokémon Type Effectiveness")
    
    # Create a label to display the results
    result_label = Label(result_window, text="Type Effectiveness")
    result_label.pack()
    
    # Create a DataFrame to hold the results
    result_data = {'Types': typenamelist}
    
    # Loop through each Pokémon and calculate type effectiveness
    for i in range(num_pokemon):
        # Get the Pokémon's name and type effectiveness
        pokemon_name = entry_pokemon_names[i].get()
        type_effectiveness = type_calculation()
        
        # Add the type effectiveness data to the result DataFrame
        result_data[pokemon_name] = type_effectiveness
    
    # Create a pandas DataFrame from the result data
    df_result = pd.DataFrame(result_data)
    
    # Create a tkinter Text widget to display the DataFrame
    result_text = Text(result_window)
    result_text.insert(END, df_result.to_string(index=False))
    result_text.pack()
    
    # Run the tkinter event loop
    result_window.mainloop()

# Create the input window
input_window = Tk()
input_window.title("Pokémon Type Effectiveness")

# Create a label and entry widget to input the number of Pokémon
label_num_pokemon = Label(input_window, text="Number of Pokémon:")
label_num_pokemon.pack()
entry_num_pokemon = Entry(input_window)
entry_num_pokemon.pack()

# Create a list to hold the entry widgets for Pokémon names
entry_pokemon_names = []

# Function to handle submit button click event
def add_pokemon():
    # Get the number of Pokémon from the entry widget
    num_pokemon = int(entry_num_pokemon.get())
    
    # Create a label and entry widget to input the Pokémon's name
    label_pokemon_name = Label(input_window, text="Pokémon Name:")
    label_pokemon_name.pack()
    entry_pokemon_name = Entry(input_window)
    entry_pokemon_name.pack()
    
    # Add the entry widget to the list
    entry_pokemon_names.append(entry_pokemon_name)
    
    # Create a new window to display the Pokémon types
    type_window = Tk()
    type_window.title("Pokémon Type Effectiveness")
    
    # Create a label for the type selection
    label_type = Label(type_window, text="Select Pokémon Type:")
    label_type.pack()
    
    # Create a list to hold the type option menus
    type_menus = []
    
    # Loop through the types and create option menus
    for i in range(2):
        # Create a label for the type number
        label_type_no = Label(type_window, text="Type {}".format(i + 1))
        label_type_no.pack()
        
        # Create an option menu with the Pokémon types
        type_menu = OptionMenu(type_window, StringVar(), *typesdict.keys())
        type_menu.pack()
        
        # Add the option menu to the list
        type_menus.append(type_menu)
    
    # Function to handle the type submit button click event
    def submit_types():
    # Get the selected types from the option menus
        types = []
    for type_menu in type_menus:
        selected_type = type_menu.cget("text")
        if selected_type:
            types.append(typesdict[selected_type.lower()])

    # Calculate the type effectiveness and store the result
    type_effectiveness = type_calculation(types[0], types[1])
    type_effectiveness_data.append(type_effectiveness)

    # Destroy the type window
    type_window.destroy()

    # Check if all Pokémon types have been entered
    if len(type_effectiveness_data) == num_pokemon:
        # Enable the submit button
        submit_button.config(state=NORMAL)


    
    # Create a button to submit the Pokémon types
    submit_types_button = Button(type_window, text="Submit", command=submit_types)
    submit_types_button.pack()

# Create a button to add Pokémon
add_button = Button(input_window, text="Add Pokémon", command=add_pokemon)
add_button.pack()

# Create a submit button
submit_button = Button(input_window, text="Submit", state=DISABLED, command=submit)
submit_button.pack()

# Run the tkinter event loop
input_window.mainloop()