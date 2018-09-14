# Neeerds - Dennis Chen && T. Fabiha
# SoftDev1 pd6
# K06: StI/O: Divine your Destiny!
# 2018-09-14

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

def main():
    occDict = dictFile("occupations.csv") # dictionary of all occupations with percentages

    if occDict == 0:
        return;

    '''
    Algorithm

    Sample:
    1st occupation = teacher --> 20%
    2nd occupation = doctor --> 30%
    3rd occupation = farmer --> 50%

    Pointer randomly chosen lands at 40.
    --> The 2nd occupation, doctor, is chosen.

      1st            2nd                3rd
    ==========|==============|========================|
    |----|----|----|----|----|----|----|----|----|----|
      10   20   30   40   50   60   70   80   90   100
                     ^
                     |
                 (pointer)
    '''

    occChosen = False # has an occupation been chosen by the algorithm
    summ = 0 # collects the sum of the percentages throughout the algorithm
    pointer = random.randint(0, 999) # out of total = 98.0

    for key in occDict:
        summ += occDict[key] * 10

        if pointer < summ:
            print("Chosen job: " + key)
            occChosen = True
            break;

    if occChosen == False:
        print("You are jobless. Try again.")


main()
