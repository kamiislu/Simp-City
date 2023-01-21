#Luismika Lim - S10223527 - P11
#9 August 2021

#Imports
import random

#Global Lists & Variables
buildingList = ["BCH", "HSE", "HWY", "SHP", "FAC"]
turn_no = 1
buildingDict = {"HSE":8,"HWY":8,"SHP":8,"BCH":8,"FAC":8}
randoms = []
boardList = [['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   ']]

#Functions

def boardTemp():#print table to start a new game
    global boardList
    boardList = [['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   '],
                 ['   ', '   ', '   ', '   ','   ','   ']]
def menu():# game menu
    print("Welcome, mayor of Simp City!")
    print("-"*26)
    print("{}\n{}".format("1. Start new game","2. Load saved game\n"))
    print("0. Exit")
    gameChoice = input("Your choice? ")
    optionList = ["1","2","0"]
    if gameChoice not in optionList:
        print("Please choose a valid option.")
    print()
    return gameChoice

def printedBoard():#For Final Layout
    print('     A     B     C     D  ')
    for row in range(4):
        print('  ', end = '')
        for col in range(4):
            print('+-----', end = '')
        print('+')
        print(' {0}| {1} | {2} | {3} | {4} |'.format((row+1),boardList[row+1][1],\
                                                boardList[row+1][2],\
                                                boardList[row+1][3],\
                                                boardList[row+1][4]))
    print('  ' + '+-----' * 4 + '+')

def newGame():#runs the game board and its options

    print("Turn", turn_no)
    print('     A     B     C     D  ')
    for row in range(4):
        print('  ', end = '')
        for col in range(4):
            print('+-----', end = '')
        print('+')
        print(' {0}| {1} | {2} | {3} | {4} |'.format((row+1),boardList[row+1][1],\
                                                boardList[row+1][2],\
                                                boardList[row+1][3],\
                                                boardList[row+1][4]))
    print('  ' + '+-----' * 4 + '+')

    global randoms

    if randoms == []:
        random1, random2  = buildingList[random.randint(0,4)],\
                            buildingList[random.randint(0,4)]
        randoms = [random1,random2]
    
    print("1. Build a", randoms[0])
    print("2. Build a", randoms[1])
    print("3. See remaining buildings")
    print("4. See current score")
    print()
    print("5. Save game")
    print("0. Exit to main menu")

    global buildingChoice
    
    buildingChoice = input("Your Choice? ")
    
    buildingChoiceList = ["1","2","3","4","5","0"]
    while True:
        if buildingChoice not in buildingChoiceList:
            print("You must choose an option from the menu.")
            newGame()
        else:
            break


           
def remaining():
    print()
    print("{:<20}{}".format("Building","Remaining"))
    print("{:<20}{}".format("-"*8,"-"*9))
    for x in buildingList:
        print("{:<20}{}".format(x,buildingDict[x]))
    print()
    
#code to place building in location
def buildingLoc(building):
    while True:
        locationChoice = input("Build where? ").upper()
        letters = ["","A","B","C","D"]
        if len(locationChoice)!=2:
            print("You must enter an alphabet followed by a number.")
            newGame()
        elif locationChoice[0] not in letters:
            print("Input is invalid.")
            newGame()
        elif locationChoice[1] not in ["1","2","3","4"]:
            print("Input is invalid.")
            newGame()
        else:
            locNo = int(locationChoice[1]) 
            for x in letters:
                if locationChoice[0] == x:
                    locAlpha = letters.index(x)
            if boardList[locNo][locAlpha] != "   ":
                print("You cannot build at an occupied location.")
                newGame()
            elif check(locNo,locAlpha) is True:
                print("You must build next to an existing building.")
                newGame()
            else:
                boardList[locNo][locAlpha]=building
                buildingDict[building] = buildingDict[building]-1
                break
    print()


        
#Adjacency check
def check(locNo,locAlpha):
    if turn_no ==1:
        return False
    else:
        if (boardList[locNo-1][locAlpha]!="   "\
           or boardList[locNo][locAlpha-1]!="   " or\
           boardList[locNo+1][locAlpha]!="   "\
           or boardList[locNo][locAlpha+1]!="   "):
            return False
        else:
            return True

#Scoring function
def scoring():
    BCHList = []
    BCHScore = 0
    FACScore = 0
    FACList = []
    FACList2 = [4,4,4,4]
    FacNo = 0
    HWYList = []
    HWYScore = 0
    HwyNo = 0
    SHPList = []
    SHPScore = 0
    SHPBuildings = []
    HSEList = []
    HSEScore = 0
    HSE1_point = ["FAC"]
    HSE1point = ["HSE","SHP"]
    HSE2point = ["BCH"]
    HSEScorefinal = 0
    for row in range(1,5):
        if "HWY" in boardList[row]:
            HWYCount = boardList[row].count("HWY")
       
            if HWYCount == 4 or HWYCount == 1:
                for x in range(HWYCount):
                    HWYList.append(str(HWYCount))
                    HWYScore += HWYCount
          
            elif HWYCount == 3:#3 HWY in a row next to each other and the 3 different combinations they might be in

                if (boardList[row][1] == "HWY" and boardList[row][3] == "HWY" and boardList[row][4] == "HWY"):
                    HWYList.append("1")
                    HWYScore += 1
                    for x in range(2):
                        HWYList.append("2")
                        HWYScore += 2                              
                elif (boardList[row][1] == "HWY" and boardList[row][2] == "HWY" and boardList[row][4] == "HWY"):
                    for x in range(2):
                        HWYList.append("2")
                        HWYScore += 2
                    HWYList.append("1")
                    HWYScore += 1
                else:
                    for x in range(3):
                        HWYList.append("3")
                        HWYScore += 3                          
            elif HWYCount == 2:#2 HWY in a row next to each other and the 2 diff combinations
                if (boardList[row][1] == "HWY" and boardList[row][4] == "HWY") or (boardList[row][1] == "HWY" and boardList[row][3] == "HWY")\
                    or (boardList[row][2] == "HWY" and boardList[row][4] == "HWY"):
                    for x in range(2):
                        HWYList.append("1")
                        HWYScore += 1                                 
                else:
                    for x in range(2):
                        HWYList.append("2")
                        HWYScore += 2

        for column in range(1,5):
            if boardList[row][column] == "BCH":#BCH Scoring
                if column == 1 or column == 4:
                    BCHList.append("3")
                    BCHScore += 3
                else:
                    BCHList.append("1")
                    BCHScore += 1
            elif boardList[row][column] == "FAC":#FAC Scoring
                FacNo += 1
                if FacNo <= 4:
                    FACScore = FacNo * FacNo
                    FACList = (str(FacNo)*FacNo)
                elif FacNo > 4:
                    FacScore = 16 + (FacNo-4)
                    FACList2.append("1")
            elif boardList[row][column] == "SHP":#SHP Scoring
                tempScore = 0
                for x in range (5):#To check how many diff types of buildings there are adjacent to each SHP on the board
                    if boardList[row-1][column] == buildingList[x] or boardList[row][column-1] == buildingList[x] or boardList[row+1][column]\
                        == buildingList[x] or boardList[row][column+1] == buildingList[x]:
                        tempScore += 1
                SHPList.append(str(tempScore))
                SHPScore += tempScore
            elif boardList[row][column] == "HSE":#HSE Scoring
                if boardList[row+1][column] in HSE1_point or boardList[row-1][column] in HSE1_point or \
                   boardList[row][column+1] in HSE1_point or boardList[row][column-1] in HSE1_point:
                    HSEList.append('1')#checking adjacent
                    HSEScorefinal += 1
                else:
                    HSEScore=0
                    if boardList[row+1][column] in HSE1point: 
                        HSEScore += 1
                    elif boardList[row+1][column] == "BCH": 
                        HSEScore += 2
                    if boardList[row-1][column] in HSE1point: 
                        HSEScore += 1
                    elif boardList[row-1][column] == "BCH": 
                        HSEScore += 2
                    if boardList[row][column+1] in HSE1point:
                        HSEScore += 1
                    elif boardList[row][column+1] == "BCH": 
                        HSEScore += 2
                    if boardList[row][column-1] in HSE1point: 
                        HSEScore += 1
                    elif boardList[row][column-1] == "BCH":
                        HSEScore += 2
                    HSEList.append(str(HSEScore))
                    HSEScorefinal += HSEScore
    totalScore = BCHScore + FACScore + HWYScore + SHPScore + HSEScorefinal
#Print the scores    
    print("BCH:" + " + ".join(BCHList) + " = " + str(BCHScore))
    print("FAC:" + " + ".join(FACList) + " = " + str(FACScore))
    print("HWY:" + " + ".join(HWYList) + " = " + str(HWYScore))
    print("SHP:" + " + ".join(SHPList) + " = " + str(SHPScore))
    print("HSE:" + " + ".join(HSEList) + " = " + str(HSEScorefinal))
    if turn_no == 17:
        print("Total score =", totalScore)
        return False

def saveGame():#Save Game
    file = open("ASGsave.txt","w")
    
    file.write(str(turn_no) + '\n')
    for row in range(0,6):
        board = ""
        for column in range(0,6):
            board = board + boardList[row][column] + ","
        file.write(board + "\n")
    for keys in buildingDict:
        file.write('{},{}\n'.format(keys, buildingDict.get(keys)))
    file.close()

def loadGame():#Load Game
    file = open("ASGsave.txt","r")
    turn_no = int(file.readline())
    info = file.readlines()
    for line in file:
        line = line.strip("\n")
        dataList = line.split(",")
        for column in range(0,6):
            boardList[row][column] = dataList[column]
        row += 1 
    for line in info[8:]:
        datalist = line.strip("\n").split(",")
        buildingDict[datalist[0]] = int(datalist[1])             
        
#Body
while True:
    choice = menu()
    if choice == "1":#chooses 1 i menu
        boardTemp()   
        while True:#to keep the game running
            if turn_no <17:#as long as turns dont exceed 16 turns
                newGame()
                if buildingChoice == "1":   
                    buildingLoc(randoms[0])
                    turn_no +=1
                    randoms.clear()
                elif buildingChoice == "2":
                    buildingLoc(randoms[1])
                    turn_no += 1
                    randoms.clear()
                elif buildingChoice == "3":
                    remaining()
                elif buildingChoice == "4":
                    scoring()
                elif buildingChoice == "5":
                    saveGame()
                    print("Game Saved!")
                    print()
                    break#return to main menu
                elif buildingChoice == "0":
                    print()
                    break#return to main menu
            elif turn_no == 17:#End of game
                print("Final layout of Simp City")
                printedBoard()
                scoring()
                break               
        
            
    elif choice == "2":
        loadGame()
        
        while True:
            if turn_no <17:# as long as dont exceed 16 turns
                newGame()
                if buildingChoice == "1":   
                    buildingLoc(randoms[0])
                    turn_no +=1
                    randoms.clear()
                elif buildingChoice == "2":
                    buildingLoc(randoms[1])
                    turn_no += 1
                    randoms.clear()
                elif buildingChoice == "3":
                    remaining()
                elif buildingChoice == "4":
                    scoring()
                elif buildingChoice == "5":
                    saveGame()
                    print("Game Saved!")
                    print()
                    break#return to main menu
                elif buildingChoice == "0":
                    print()
                    break#return to main menu
            elif turn_no == 17:#End of game
                print("Final layout of Simp City")
                printedBoard()
                scoring()
                break
