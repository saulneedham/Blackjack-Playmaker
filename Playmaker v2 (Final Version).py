import tkinter as tk
from tkinter import *

#-------------------------------------------------------------------------------------------

#HARD TOTALS

                #2         3         4         5         6         7         8         9        10         A
hardPlaysH17 =[['H      ','H      ','H      ','H      ','H      ','H      ','H      ','H      ','H      ','H      '], #7
               ['H      ','H      ','H      ','H      ','H +2>Dh','H      ','H      ','H      ','H      ','H      '], #8
               ['H +1>Dh','Dh     ','Dh     ','Dh     ','Dh     ','H +3>Dh','H      ','H      ','H      ','H      '], #9
               ['Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','H +4>Dh','H +3>Dh'], #10
               ['Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     '], #11
               ['H +3>S ','H +2>S ','S +0<H ','S      ','S      ','H      ','H      ','H      ','H      ','H      '], #12
               ['S -1<H ','S      ','S      ','S      ','S      ','H      ','H      ','H      ','H      ','H      '], #13
               ['S      ','S      ','S      ','S      ','S      ','H      ','H      ','H      ','H      ','H      '], #14
               ['S      ','S      ','S      ','S      ','S      ','H      ','H      ','H      ','Rh+4>S ','Rh+5>S '], #15
               ['S      ','S      ','S      ','S      ','S      ','H      ','H      ','Rh+4>S ','Rh+0>S ','Rh+3>S '], #16
               ['S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','Rs     '], #17
               ['S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ']  #18
               ]

hardPlaysS17 = [sublist[:] for sublist in hardPlaysH17]
hardPlaysS17[3][9]='H +4>Dh'  #10 v A
hardPlaysS17[4][9]='H +1>Dh'  #11 v A
hardPlaysS17[8][9]='H      '  #15 v A
hardPlaysS17[9][9]='Rh     '  #16 v A
hardPlaysS17[10][9]='S      ' #17 v A

#SOFT TOTALS

                #2         3         4         5         6         7         8         9        10         A
softPlaysH17 =[['H      ','H      ','H      ','Dh     ','Dh     ','H      ','H      ','H      ','H      ','H      '], #A,2
               ['H      ','H      ','H      ','Dh     ','Dh     ','H      ','H      ','H      ','H      ','H      '], #A,3
               ['H      ','H      ','Dh     ','Dh     ','Dh     ','H      ','H      ','H      ','H      ','H      '], #A,4
               ['H      ','H      ','Dh     ','Dh     ','Dh     ','H      ','H      ','H      ','H      ','H      '], #A,5
               ['H +1>Dh','Dh     ','Dh     ','Dh     ','Dh     ','H      ','H      ','H      ','H      ','H      '], #A,6
               ['Ds     ','Ds     ','Ds     ','Ds     ','Ds     ','S      ','S      ','H      ','H      ','H      '], #A,7
               ['S      ','S      ','S +3>Ds','S +1>Ds','Ds+0<S ','S      ','S      ','S      ','S      ','S      '], #A,8
               ['S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      ','S      '], #A,9
               ['B      ','B      ','B      ','B      ','B      ','B      ','B      ','B      ','B      ','B      ']  #A,10
               ]

softPlaysS17 = [sublist[:] for sublist in softPlaysH17]
softPlaysS17[5][0]='S      ' #A,7 v 2
softPlaysS17[6][4]='S +1>Ds' #A,8 v 6

#SPLITS

                #2         3         4         5         6         7         8         9        10         A
splitsH17    =[['Ph     ','Ph     ','P      ','P      ','P      ','P      ','H      ','H      ','H      ','H      '], #2,2
               ['Ph     ','Ph     ','P      ','P      ','P      ','P      ','H      ','H      ','H      ','H      '], #3,3
               ['H      ','H      ','H      ','Ph     ','Ph     ','H      ','H      ','H      ','H      ','H      '], #4,4
               ['Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','Dh     ','H +4>Dh','H +3>Dh'], #5,5
               ['Ph     ','P      ','P      ','P      ','P      ','H      ','H      ','H      ','H      ','H      '], #6,6
               ['P      ','P      ','P      ','P      ','P      ','P      ','H      ','H      ','H      ','H      '], #7,7
               ['P      ','P      ','P      ','P      ','P      ','P      ','P      ','P      ','P      ','Rp     '], #8,8
               ['P      ','P      ','P      ','P      ','P      ','S      ','P      ','P      ','S      ','S      '], #9,9
               ['S      ','S      ','S +6>P ','S +5>P ','S +4>P ','S      ','S      ','S      ','S      ','S      '], #T,T
               ['P      ','P      ','P      ','P      ','P      ','P      ','P      ','P      ','P      ','P      '], #A,A
               ]

splitsS17 = [sublist[:] for sublist in splitsH17]
splitsS17[6][9]='P      ' #8,8 v A
splitsS17[3][9]='H +4>Dh' #10 v A

#-------------------------------------------------------------------------------------------

#['playC1''playC2''+/-''TC''>/<''deviation']

def trueCountCalc(cardsDealt):
    shoeSize = int(variableShoe.get()[0])
    totalCards = shoeSize*52
    cardsLeft = totalCards - cardsDealt
    decksLeft = cardsLeft/52
    rounded =  round(decksLeft / 0.25)
    decksLeftRounded = rounded * 0.25
    trueCount = count/decksLeft
    return trueCount, cardsLeft, decksLeftRounded

def addCount():
    global count, cardsDealt, cardsDealt, trueCount
    cardsDealt+=1
    count+=1
    countLabel.config(text=count)
    trueCount, cardsLeft, decksLeft = trueCountCalc(cardsDealt)
    tcLabel.config(text=trueCount)
    clLabel.config(text=cardsLeft)
    dlLabel.config(text=decksLeft)
    root.update()

def zeroCount():
    global count, cardsDealt, cardsDealt, trueCount
    cardsDealt+=1
    countLabel.config(text=count)
    trueCount, cardsLeft, decksLeft = trueCountCalc(cardsDealt)
    tcLabel.config(text=trueCount)
    clLabel.config(text=cardsLeft)
    dlLabel.config(text=decksLeft)
    root.update()

def minCount():
    global count, cardsDealt, cardsDealt, trueCount
    cardsDealt+=1
    count-=1
    countLabel.config(text=count)
    trueCount, cardsLeft, decksLeft = trueCountCalc(cardsDealt)
    tcLabel.config(text=trueCount)
    clLabel.config(text=cardsLeft)
    dlLabel.config(text=decksLeft)
    root.update()

def convertCard(card):
    if card == 'A':
        convertedCard = 11
    else:
        convertedCard = int(card)
    return convertedCard

def bsCheck():
    pc1 = convertCard(variableCard1.get())
    pc2 = convertCard(variableCard2.get())
    dc1 = convertCard(variableCardDealer.get())

    if variableDAS.get() == 'DAS':
        das = True
    else:
        das = False
    if variableSur.get() == 'Sur':
        sur = True
    else:
        sur = False

    ###
        
    column = dc1-2
    
    if pc1==pc2:
        #Pair splitting
        if variableGame.get() == 'S17':
            table = splitsS17
        else:
            table = splitsH17
        row = pc1-2
        
    #
    elif pc1 == 11 or pc2 == 11:
        #Soft totals
        if variableGame.get() == 'S17':
            table = softPlaysS17
        else:
            table = softPlaysH17
        row = pc1+pc2-13

    #        
    else:
        #Hard totals
        if variableGame.get() == 'S17':
            table = hardPlaysS17
        else:
            table = hardPlaysH17
        if pc1+pc2<8:
            row = 0
        elif pc1+pc2>17:
            row = 11
        else:
            row = pc1+pc2-7

    data=play=table[row][column]

    ###

    play = data[0:2]
    if data[2:4]!='  ':
        tc = int(data[2:4])
    else:
        tc = 'no deviation'
    greaterOrLess = data[4]
    deviation = data[5:7]

    if tc!='no deviation':
        if greaterOrLess=='>':
            #count must be greater to deviate
            if trueCount>=tc:
                play = deviation
        else:
            #count must be less to deviate
            if trueCount<=tc:
                play = deviation

    finalPlay = getCodeData(play,das,sur)
    if dc1==11:
        insurance = checkInsurance()
    else:
        insurance = ''

    playLabel.config(text=finalPlay)
    insuranceLabel.config(text=insurance)
    root.update()

def checkInsurance():
    if trueCount<3:
        insurance = 'Dont take insurance'
    else:
        insurance = 'Take insurance'
    return insurance

def getCodeData(play,das,sur):
    if play[0]=='R': #surrender
        if sur==True:
            finalPlay='SURRENDER'
        else:
            if play[1]=='h':
                finalPlay='HIT'
            elif play[1]=='s':
                finalPlay='STAND'
            elif play[1]=='p':
                finalPlay='SPLIT'
    elif play[0]=='P': #split
        if play[1]=='h':
            if das==True:
                finalPlay='SPLIT'
            else:
                finalPlay='HIT'
        else:
            finalPlay='SPLIT'
    elif play[0]=='D': #double
        if play[1]=='s':
            finalPlay='DOUBLE (S)'
        elif play[1]=='h':
            finalPlay='DOUBLE (H)'
    elif play[0]=='S': #stand
        finalPlay='STAND'
    elif play[0]=='H': #hit
        finalPlay='HIT'
    elif play[0]=='B': #blackjack
        finalPlay='BLACKJACK'

    return finalPlay
    
#-------------------------------------------------------------------------------------------

count = 0
trueCount = 0
cardsDealt = 0
shoeSize = 6 #4-8
cardsLeft = shoeSize*52
decksLeft = float(shoeSize)
cardOptions = ['2','3','4','5','6','7','8','9','10','A']
shoeOptions = ['4 deck','6 deck', '8 deck']
gameOptions = ['S17','H17']
dasOptions = ['DAS','NDAS']
surrenderOptions = ['Sur','NSur']

#-------------------------------------------------------------------------------------------

root = tk.Tk()
root.title('AP Playmaker')

canvas1 = tk.Canvas(root, width = 600, height = 270)
canvas1.pack()

canvas1.create_line(450, -30, 450, 300, fill="black", width=2)
root.resizable(False, False)

#-------------------------------------------------------------------------------------------

#Player card 1
variableCard1 = StringVar(root)
variableCard1.set(cardOptions[0])
menu= OptionMenu(root, variableCard1, *cardOptions)
canvas1.create_window(200, 250, window=menu)

#Player card 2
variableCard2 = StringVar(root)
variableCard2.set(cardOptions[0])
menu= OptionMenu(root, variableCard2, *cardOptions)
canvas1.create_window(250, 250, window=menu)

#Dealer card
variableCardDealer = StringVar(root)
variableCardDealer.set(cardOptions[0])
menu= OptionMenu(root, variableCardDealer, *cardOptions)
canvas1.create_window(225, 70, window=menu)

#DAS/NDAS
variableDAS = StringVar(root)
variableDAS.set(dasOptions[0])
menu= OptionMenu(root, variableDAS, *dasOptions)
canvas1.create_window(33, 110, window=menu)

#S17/H17
variableGame = StringVar(root)
variableGame.set(gameOptions[0])
menu= OptionMenu(root, variableGame, *gameOptions)
canvas1.create_window(30, 140, window=menu)

#Sur/NSur
variableSur = StringVar(root)
variableSur.set(surrenderOptions[0])
menu= OptionMenu(root, variableSur, *surrenderOptions)
canvas1.create_window(31, 170, window=menu)

#Shoe size
variableShoe = StringVar(root)
variableShoe.set(shoeOptions[1])
menu= OptionMenu(root, variableShoe, *shoeOptions)
canvas1.create_window(37, 200, window=menu)

#-------------------------------------------------------------------------------------------

playLabel = tk.Label(root, text='...')
playLabel.config(font=('Helvetica bold',37),fg='blue')
canvas1.create_window(228, 150, window=playLabel)

insuranceLabel = tk.Label(root, text='')
insuranceLabel.config(font=('Helvetica bold',12),fg='blue')
canvas1.create_window(228, 200, window=insuranceLabel)

countLabel = tk.Label(root, text=count)
countLabel.config(font=('Helvetica bold',50),fg='red')
canvas1.create_window(525, 170, window=countLabel)

tcLabel = tk.Label(root, text=trueCount)
canvas1.create_window(532, 12, window=tcLabel)
label0 = tk.Label(root, text='TC:')
canvas1.create_window(462, 12, window=label0)

clLabel = tk.Label(root, text=cardsLeft)
canvas1.create_window(565, 30, window=clLabel)
label0 = tk.Label(root, text='Remaining cards:')
canvas1.create_window(500, 30, window=label0)

dlLabel = tk.Label(root, text=decksLeft)
canvas1.create_window(565, 48, window=dlLabel)
label0 = tk.Label(root, text='Decks remaining:')
canvas1.create_window(500, 48, window=label0)

label0 = tk.Label(root, text='SETTINGS')
label0.config(font=('Helvetica 9 underline'))
canvas1.create_window(30, 85, window=label0)

label1=Label(root, text='AP Playmaker')
label1.config(font=('Helvetica bold',30))
canvas1.create_window(225, 23, window=label1)

button0 = tk.Button(text='Check', command=bsCheck)
canvas1.create_window(420, 150, height=30, width=50,window=button0)

button0 = tk.Button(text='+1', command=addCount)
canvas1.create_window(525, 100, height=60, width=60,window=button0)

button0 = tk.Button(text='0', command=zeroCount)
canvas1.create_window(587, 170, height=30, width=30,window=button0)

button0 = tk.Button(text='-1', command=minCount)
canvas1.create_window(525, 240, height=60, width=60,window=button0)

root.mainloop()