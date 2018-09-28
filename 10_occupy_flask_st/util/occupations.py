import random

def dictFile(filename):
    try:
        # tries to open the file name
        f= open(filename,'r')
    except:
        # if it cannot open it
        print("File does not exist")
        return 0

    fText = f.read() # readable text
    lines = fText.split('\n')[1:] # list of each row

    lines = lines[:len(lines)-2]

    allOcc = [] # list of all occupations with percentages

    for each in lines:
        # if there is a double quote
        if "\"" in each:
            # split on double quotes
            # occ[0] is the occupation
            # occ[1] is the percentage
            occ = each.split("\"")[1:]

            # turns the percentage of occupation into a float
            occ[1] = float(occ[1][1:])

        else:
            # regularly split on comma
            occ = each.split(',')

            # turns the percentage of occupation into a float
            occ[1] = float(occ[1])

        allOcc.append(occ)


    return dict(allOcc) # create the dictionary of occupations matched with their percentages

#occDict = dictFile("../data/occupations.csv")

def occChooser(occDict):
    occChosen = False # has an occupation been chosen by the algorithm
    summ = 0 # collects the sum of the percentages throughout the algorithm
    pointer = random.randint(0, 999) # out of total = 98.0

    for key in occDict:
        summ += occDict[key] * 10

        if pointer < summ:
            return(key + ".")
            occChosen = True

    if occChosen == False:
        return("nothing. You're jobless.")
