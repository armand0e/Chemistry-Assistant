#!/usr/bin/env python3
import periodictable
from periodictable import Element
from periodictable import Category
from periodictable import Phase

AtmDict = {
    'H':1,       'He':2,      'Li':3,      'Be':4,      'B':5,       'C':6,
    'N':7,       'O':8,       'F':9,       'Ne':10,     'Na':11,     'Mg':12,     'Al':13,     'Si':14,\
    'P':15,      'S':16,      'Cl':17,     'Ar':18,     'K':19,      'Ca':20,     'Sc':21,     'Ti':22,\
    'V':23,      'Cr':24,     'Mn':25,     'Fe':26,     'Co':27,     'Ni':28,     'Cu':29,     'Zn':30,\
    'Ga':31,     'Ge':32,     'As':33,     'Se':34,     'Br':35,     'Kr':36,     'Rb':37,     'Sr':38,\
    'Y':39,      'Zr':40,     'Nb':41,     'Mo':42,     'Tc':43,     'Ru':44,     'Rh':45,     'Pd':46,\
    'Ag':47,     'Cd':48,     'In':49,     'Sn':50,     'Sb':51,     'Te':52,     'I':53,      'Xe':54,\
    'Cs':55,     'Ba':56,     'La':57,     'Ce':58,     'Pr':59,     'Nd':60,     'Pm':61,     'Sm':62,\
    'Eu':63,     'Gd':64,     'Tb':65,     'Dy':66,     'Ho':67,     'Er':68,     'Tm':69,     'Yb':70,\
    'Lu':71,     'Hf':72,     'Ta':73,     'W':74,      'Re':75,     'Os':76,     'Ir':77,     'Pt':78,\
    'Au':79,     'Hg':80,     'Tl':81,     'Pb':82,     'Bi':83,     'Po':84,     'At':85,     'Rn':86,\
    'Fr':87,     'Ra':88,     'Ac':89,     'Th':90,     'Pa':91,     'U':92,      'Np':93,     'Pu':94,\
    'Am':95,     'Cm':96,     'Bk':97,     'Cf':98,     'Es':99,     'Fm':100,    'Md':101,    'No':102,\
    'Lr':103,    'Rf':104,    'Db':105,    'Sg':106,    'Bh':107,    'Hs':108,    'Mt':109,    'Ds':110,\
    'Rg':111,    'Cn':112,    'Nh':113,    'Fl':114,    'Mc':115,    'Lv':116,    'Ts':117,    'Og':118
}
Categories = {
    0:'UNKNOWN',
    1:'DIATOMIC_NONMETAL',
    2:'ALKALI_METAL',
    3:'ALKALINE_EARTH_METAL',
    4:'TRANSITION_METAL',
    5:'LANTHANIDE',
    6:'ACTINIDE',
    7:'POST_TRANSITION_METAL',
    8:'METALLOID',
    9:'NONMETAL',
    10:'NOBLE_GAS',
    11:'SYNTHETIC',
}

Phases = {
    0:'GAS',
    1:'LIQUID',
    2:'SOLID'
}
validinput = False
programrun = True
summary = ''
while programrun:
    while not validinput:
        print('           MENU           ')
        print('--------------------------')
        print('1. Element Info')
        print('2. Compound Mass Calculator')
        print('3. Electron Configuration')
        print('4. Quit\n')
        menuoption = input("Please choose an option: ")
        try:
            menuoption = int(menuoption)
            if menuoption > 4:
                print("\nError. Chosen option: UNDEFINED")
                validinput = False
            elif menuoption <= 0:
                print("\nError. Chosen option: UNDEFINED")
                validinput = False
            else:
                validinput = True
        except TypeError:
            print("\nPlease select an integer displayed on the menu.")


    if menuoption == 1:
        element = input("\nPlease input any element's symbol or type 'q' to quit: ")
        while element != 'q':
            AtomNum = AtmDict[element]
            info = periodictable.ELEMENTS_DATA[AtomNum]
            print(f"{element}:")
            for j in info:
                cat = str(j)
                ans = info[cat]
                if cat == 'appearance':
                    continue
                elif cat == 'summary':
                    continue
                elif cat == 'density':
                    continue
                elif cat == 'named-by':
                    continue
                elif cat == 'phase':
                    try:
                        summary += f"\n  PHASE: {Phases[ans]}"
                    except KeyError:
                        summary += "\n  PHASE: UNKNOWN"
                elif cat == 'category':
                    try:
                        summary += f"\n  CATEGORY: {Categories[ans]}"
                    except KeyError:
                        summary += "\n  CATEGORY: UNKOWN"
                elif cat == 'molar-heat':
                    continue
                elif cat == 'boil':
                    continue
                elif cat == 'number':
                    summary += f"\n  ATOMIC NUMBER: {ans}"
                elif cat == 'symbol':
                    continue
                elif cat == 'x':
                    continue
                elif cat == 'discovered-by':
                    continue
                elif cat == 'melt':
                    continue
                elif cat == 'y':
                    continue
                elif cat == 'source':
                    continue
                elif cat == 'atomic-mass':
                    summary += f"\n  ATOMIC MASS: {ans}"
                else:
                   summary += f"\n  {cat.upper()}: {ans}"
            print(summary)
            summary = ''
            element = input("\nPlease input any element's symbol or type 'q' to quit: ")
            print(" ")
        validinput = False


    elif menuoption == 2:
                # Dictionary of all elements matched with their atomic masses.
        atomic_mass_dict = {'H' : 1.008,'HE' : 4.003, 'LI' : 6.941, 'BE' : 9.012,\
                        'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.9994,\
                        'F' : 18.998, 'NE' : 20.180, 'NA' : 22.990, 'MG' : 24.305,\
                        'AL' : 26.982, 'SI' : 28.086, 'P' : 30.974, 'S' : 32.066,\
                        'CL' : 35.453, 'AR' : 39.948, 'K' : 39.098, 'CA' : 40.078,\
                        'SC' : 44.956, 'TI' : 47.867, 'V' : 50.942, 'CR' : 51.996,\
                        'MN' : 54.938, 'FE' : 55.845, 'CO' : 58.933, 'NI' : 58.693,\
                        'CU' : 63.546, 'ZN' : 65.38, 'GA' : 69.723, 'GE' : 72.631,\
                        'AS' : 74.922, 'SE' : 78.971, 'BR' : 79.904, 'KR' : 84.798,\
                        'RB' : 84.468, 'SR' : 87.62, 'Y' : 88.906, 'ZR' : 91.224,\
                        'NB' : 92.906, 'MO' : 95.95, 'TC' : 98.907, 'RU' : 101.07,\
                        'RH' : 102.906, 'PD' : 106.42, 'AG' : 107.868, 'CD' : 112.414,\
                        'IN' : 114.818, 'SN' : 118.711, 'SB' : 121.760, 'TE' : 126.7,\
                        'I' : 126.904, 'XE' : 131.294, 'CS' : 132.905, 'BA' : 137.328,\
                        'LA' : 138.905, 'CE' : 140.116, 'PR' : 140.908, 'ND' : 144.243,\
                        'PM' : 144.913, 'SM' : 150.36, 'EU' : 151.964, 'GD' : 157.25,\
                        'TB' : 158.925, 'DY': 162.500, 'HO' : 164.930, 'ER' : 167.259,\
                        'TM' : 168.934, 'YB' : 173.055, 'LU' : 174.967, 'HF' : 178.49,\
                        'TA' : 180.948, 'W' : 183.84, 'RE' : 186.207, 'OS' : 190.23,\
                        'IR' : 192.217, 'PT' : 195.085, 'AU' : 196.967, 'HG' : 200.592,\
                        'TL' : 204.383, 'PB' : 207.2, 'BI' : 208.980, 'PO' : 208.982,\
                        'AT' : 209.987, 'RN' : 222.081, 'FR' : 223.020, 'RA' : 226.025,\
                        'AC' : 227.028, 'TH' : 232.038, 'PA' : 231.036, 'U' : 238.029,\
                        'NP' : 237, 'PU' : 244, 'AM' : 243, 'CM' : 247, 'BK' : 247,\
                        'CT' : 251, 'ES' : 252, 'FM' : 257, 'MD' : 258, 'NO' : 259,\
                        'LR' : 262, 'RF' : 261, 'DB' : 262, 'SG' : 266, 'BH' : 264,\
                        'HS' : 269, 'MT' : 268, 'DS' : 271, 'RG' : 272, 'CN' : 285,\
                        'NH' : 284, 'FL' : 289, 'MC' : 288, 'LV' : 292, 'TS' : 294,\
                        'OG' : 294}

        # List of all elements to allow for easy inclusion testing.
        elements_list = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA',\
                        'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC', 'TI',\
                        'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE',\
                        'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO',\
                        'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE',\
                        'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM',\
                        'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF',\
                        'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB',\
                        'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U',\
                        'NP', 'PU', 'AM', 'CM', 'BK', 'CT', 'ES', 'FM', 'MD', 'NO',\
                        'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN',\
                        'NH', 'FL', 'MC', 'LV', 'TS', 'OG']

        print("Enter the formula for the substance by seperating the atomic symbols\
        from their subscripts. ie. C 6 H 12 O 6.")

        # Get the substance's formula from user.
        formula = input("Enter a formula or type 'q' to quit: ").upper().split()
        print()

        # Continue to ask for a new formula until the user inputs a "q" for quit.
        while formula != ["Q"]:
            
            # Set the conditons for a new loop.
            atomic_mass_float = 0.0
            invalid_input = False
            coefficient = 1
            
            # Loop through each index in the formula.
            for i, ch in enumerate(formula):
                # If the character is an element, check if the next character in the
                # formula is an integer.
                if ch in elements_list:
                    element_mass = atomic_mass_dict.get(ch)
                    # If the next character is an integer, multiply the element's mass 
                    # by that integer and add it to the running sum.
                    if formula[i + 1].isdigit() == True:
                        atomic_mass_float += element_mass * int(formula[i + 1])
                    # If not, just add that element's mass to the sum.
                    else:
                        atomic_mass_float += element_mass
                # If the charcter is an integer
                elif ch.isdigit() == True:
                    # If the first index is an integer, assume that that is a
                    # coefficient for the formula and multiply the formula by that
                    # number
                    if i == 0:
                        coefficient = int(ch)
                    # Make sure the previous index wasn't an integer as well
                    # (the integer needs an element to multiply), if it was, let the
                    # program know that there is an error.
                    elif formula[i - 1].isalpha() == False:
                        invalid_input = True
                    else:
                        pass
                # If the only character in the formula is an integer, let the program
                # know that there is an error.
                elif ch.isdigit() == True and len(formula) == 1:
                    invalid_input = True
                # If a character is not an element or an integer, let the program know
                # that there is an error.
                else:
                    invalid_input = True
            
            # Muliply the entire atomic mass by the coefficient.
            atomic_mass_float *= coefficient
            
            # If there was an error in the program, display the appropriate error.
            if invalid_input == True:
                # Error for if there is only an integer entered.
                if ch.isdigit() == True and len(formula) == 1:
                    print("You must enter at least one element for every integer\
        subscript.")
                    print()
                # Error for if there is a float or non-elemnt entered.
                else:
                    print("Please enter only the atomic symbols of elements or an integer\
        subscript.")
                    print()
            
            # If there was no error, then print the claculated atomic mass
            else:
                print("Atomic Mass: ", round(atomic_mass_float, 3))
                print()
            
            # Ask for another formula.
            formula = input("Enter a formula or type 'q' to quit: ").upper().split()
            print()            
        validinput = False


    elif menuoption == 3:
                # this function ensures the user can input  "atomic number" or "element name" with capital and lower case letters, and
        # as many spaces as they wish
        def formatInput(textline):
            textline = textline.lower().strip()
            wordlist = textline.split()
            textline = " ".join(wordlist)
            return textline


        # this function is for determining the noble gas given the atomic number for use in the condensed electron configuration
        def nobleGases(valenceE):
            if valenceE >= 118: return "[Og]"
            if valenceE >= 86: return "[Rn]"
            if valenceE >= 54: return "[Xe]"
            if valenceE >= 36: return "[Kr]"
            if valenceE >= 18: return "[Ar]"
            if valenceE >= 10: return "[Ne]"
            if valenceE >= 2: return "[He]"
            return ""


        # this function is for rounding the input down to the lowest noble gas for use in the condensed electron configuration
        def atomicRounder(valenceE):
            if valenceE >= 118: return 118
            if valenceE >= 86: return 86
            if valenceE >= 54: return 54
            if valenceE >= 36: return 36
            if valenceE >= 18: return 18
            if valenceE >= 10: return 10
            if valenceE >= 2: return 2


        # so that charge is defined later on
        global charge
        # a lot of long lists with each individual electron, element symbol, and name. There should be a way to condense and
        # these lists
        electronList = ["1s^1", "1s^2", "2s^1", "2s^2", "2p^1", "2p^2", "2p^3", "2p^4", "2p^5", "2p^6", "3s^1", "3s^2",
                        "3p^1", "3p^2", "3p^3", "3p^4", "3p^5", "3p^6", "4s^1", "4s^2", "3d^1", "3d^2", "3d^3", "3d^4",
                        "3d^5", "3d^6", "3d^7", "3d^8", "3d^9", "3d^10", "4p^1", "4p^2", "4p^3", "4p^4", "4p^5", "4p^6",
                        "5s^1", "5s^2", "4d^1", "4d^2", "4d^3", "4d^4", "4d^5", "4d^6", "4d^7", "4d^8", "4d^9", "4d^10",
                        "5p^1", "5p^2", "5p^3", "5p^4", "5p^5", "5p^6", "6s^1", "6s^2", "4f^1", "4f^2", "4f^3", "4f^4",
                        "4f^5", "4f^6", "4f^7", "4f^8", "4f^9", "4f^10", "4f^11", "4f^12", "4f^13", "4f^14", "5d^1", "5d^2",
                        "5d^3", "5d^4", "5d^5", "5d^6","5d^7", "5d^8", "5d^9", "5d^10", "6p^1", "6p^2", "6p^3", "6p^4", "6p^5",
                        "6p^6", "7s^1", "7s^2","5f^1", "5f^2", "5f^3", "5f^4", "5f^5", "5f^6", "5f^7", "5f^8", "5f^9", "5f^10",
                        "5f^11", "5f^12", "5f^13", "5f^14", "6d^1", "6d^2", "6d^3", "6d^4", "6d^5", "6d^6", "6d^7", "6d^8",
                        "6d^9", "6d^10", "7p^1", "7p^2", "7p^3", "7p^4", "7p^5","7p^6"]
        elementsAb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
                    "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
                    "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
                    "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
                    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs",
                    "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
        elementsFull = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
                        "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorous", "Sulfur", "Chloride", "Argon", "Potassium",
                        "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickle",
                        "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
                        "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver",
                        "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
                        "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
                        "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten",
                        "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium",
                        "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
                        "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
                        "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium"]
        # defines the atomic number before starting the main function. looping boolean to ensure that while loops loop
        atomicNumber = 0
        looping = True

        # commented out attempts at a dictionary
        # elementsDict = [("H", "Hydrogen"),("He", "Helium"), ("Li","Lithium"), ("Be", "Beryllium"), ("B", "Boron"), ("C", "Carbon"),
        #                ("N", "Nitrogen"), ("O", "Oxygen"), ("F", "Fluorine"), ("Ne", "Neon"), ("Na", "Sodium"), ("Mg", "Magnesium"),
        #                ("Al", "Aluminium"), ("Si", "Silicon"), ("P", "Phosphorous"), ("S", "Sulfur"), ("Cl", "Chloride"), ("Ar", "Argon")]

        # actual main body of the code computes the atomic number given the atomic number or element name. this atomic number is
        # then used to index the electronList, and the list is printed from 0 to the calculated atomic number. This in short provides
        # the electron configuration
        while looping:
            print('\nWelcome to the electron config calculator!')
            print('------------------------------------------')
            print('1. Enter an atomic number')
            print('2. Enter an element name or symbol')
            print('3. Quit\n')
            choice = int(input('Please choose an option: '))

            if choice == 1:
                atomicNumber = input("Please input the atomic number of your element: ")
        # validates that the input is a positive integer value
                while not atomicNumber.isnumeric() or atomicNumber == "0":
                    atomicNumber = input("Invalid input. Please enter a positive integer value: ")
                atomicNumber = int(atomicNumber)
                break
            elif choice == 2:
                elementName = input("Please input the name of your element (abbreviated or full): ").capitalize()
        # validates the input is a valid element name
                while elementName not in elementsAb and elementName not in elementsFull:
                    elementName = input("Element name not recognized. Please try again.").capitalize()
        # checks that elementName is in the lists of elementsAb or elementsFull. If it is, then the index of the element in that list
        # is used as the atomicNumber
                try:
                    atomicNumber = elementsAb.index(elementName)
                except ValueError:
                    atomicNumber = elementsFull.index(elementName)
        # you must add 1 to the atomic number as the index starts at 0, but the atomic number starts at 1
                atomicNumber = atomicNumber + 1
                break
            elif choice == 3:
                validinput = False
                looping = False
            else:
                input("Invalid input. Please type an integer between 1 and 3. Press any button to continue")

        # asks for the charge. currently only works for p and s block elements.
        while looping:
            charge = input("Now that you have entered your element, please enter its change. (use + or -, or enter 0 if it has no charge): ")
            if not charge.lstrip("+-").isnumeric():
                charge = input("You have entered an invalid charge. Please input a valid charge: ")
            charge = int(charge)
            #if not 20 < atomicNumber <= 30 or 38 < atomicNumber < 48 or 88 < atomicNumber < 98:
            #if charge > 0:
            #    if 20 < atomicNumber <= 30:
            #        for i in range(2):
            #            n = 20
            #            electronList.pop(n)
            #            n -= 1
            #            if n == 18: break
            atomicNumber = atomicNumber - charge
            break
        improperconfig = electronList[0:atomicNumber]
        properconfig = []
        iterations = 0
        for i in range(len(improperconfig)):
            current = improperconfig[i]
            prefix = current[:2]
            if i > 0:
                iterations += 1
                previous = improperconfig[i-1]
                prevprefix = previous[:2]
                if prefix == prevprefix:
                    properconfig.pop()
                    properconfig.append(current)

                elif prefix != prevprefix:
                    properconfig.append(current)
            else:
                properconfig.append(current)
                iterations = 1
            
        '''for i in range(len(improperconfig)):
            current = improperconfig[i]
            properconfig.append(current)
            if i > 0:
                previous = improperconfig[i-1]
                if current[:2] == previous[:2]:
                    improperconfig.pop(i-1)
        print(improperconfig)'''
        # prints the name of the element you have calculated, its electron configuration, and the condensed electron configuration
        print("\nThe name of your element is:\n" + '  ' + elementsFull[atomicNumber + charge - 1])
        print("Your full electron configuration is: \n" + '  ' + ' '.join(map(str, properconfig)))
        print(("Your condensed electron configuration is: \n"+ '  ' + nobleGases(len(electronList[0:atomicNumber])) + " " +
            ' '.join(map(str, electronList[atomicRounder(atomicNumber):atomicNumber]))).strip())

    elif menuoption == 4:
        print('Thanks, have a great day!')
        programrun = False
        break
