import tkinter as tk
from tkinter import *

#######################################################################

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
    if variableGame.get() == 'S17':
        s17 = True
    else:
        s17 = False
    if variableSur.get() == 'Sur':
        sur = True
    else:
        sur = False

    ######################################################
    
    if pc1==pc2:
        #Pair splitting
        if pc1 == 2 or pc1 == 3:
            if dc1<=7:
                if dc1<=3:
                    if das==True:
                        play = 'SPLIT'
                    else:
                        play = 'HIT' 
                else:
                    play = 'SPLIT'
            else:
                play = 'HIT'
        elif pc1 == 4:
            if dc1==5:
                if das==True:
                    play = 'SPLIT'
                else:
                    play = 'HIT'
            elif dc1==6:
                if das==True:
                    play = 'SPLIT'
                else:
                    if trueCount>=2:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'
            else:
                play = 'HIT'
        elif pc1 == 5:
            if dc1<=9:
                play = 'DOUBLE'
            else:
                if dc1==10:
                    if trueCount>=4:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'
                else:
                    if s17==True and trueCount>=4:
                        play = 'DOUBLE'
                    elif s17==False and trueCount>=3:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'  
        elif  pc1 == 6:
            if dc1==2:
                if das==True:
                    play = 'SPLIT'
                else:
                    if trueCount>=3:
                        play = 'STAND'
                    else:
                        play = 'HIT'
            elif dc1==3 or dc1==4 or dc1==5 or dc1==6:
                play = 'SPLIT'
            else:
                play = 'HIT'
        elif pc1 == 7:
            if dc1<=7:
                play = 'SPLIT'
            else:
                play = 'HIT'
        elif pc1 == 8:
            if s17 == False and sur == True and dc1==11:
                play = 'SURRENDER'
            else:
                play = 'SPLIT'
        elif pc1 == 9:
            if dc1==7 or dc1==10 or dc1==11:
                play = 'STAND'
            else:
                play = 'SPLIT'
        elif pc1 == 10:
            if dc1==4 and trueCount>=6:
                play = 'SPLIT'
            elif dc1==5 and trueCount>=5:
                play = 'SPLIT'
            elif dc1==6 and trueCount>=4:
                play = 'SPLIT'
            else:
                play = 'STAND'
        else:
            play = 'SPLIT'
    #
    elif pc1 == 11 or pc2 == 11:
        #Soft totals 
        if pc1 == 11:
            softCard = pc2
        else:
            softCard = pc1 

        if softCard == 2 or softCard == 3:
            if dc1==5 or dc1==6:
                play = 'DOUBLE'
            else:
                play = 'HIT'
        elif softCard == 4 or softCard == 5:
            if dc1==4 or dc1==5 or dc1==6:
                play = 'DOUBLE'
            else:
                play = 'HIT'
        elif softCard == 6:
            if dc1==2:
                if trueCount>=1:
                    play = 'DOUBLE'
                else:
                    play = 'HIT'
            elif dc1>=7:
                play = 'HIT'
            else:
                play = 'DOUBLE'
        elif softCard == 7:
            if dc1==2:
                if s17==True:
                    play = 'STAND'
                else:
                    play = 'DOUBLE'
            elif dc1<=6:
                play = 'DOUBLE'
            elif dc1<=8:
                play = 'STAND'
            else:
                play = 'HIT'
        elif softCard == 8:
            if dc1==4:
                if trueCount>=3:
                    play = 'DOUBLE'
                else:
                    play = 'STAND'
            elif dc1==5:
                if trueCount>=1:
                    play = 'DOUBLE'
                else:
                    play = 'STAND'
            elif dc1==6:
                if s17==True:
                    if trueCount>=1:
                        play = 'DOUBLE'
                    else:
                        play = 'STAND'
                else:
                    if trueCount<0:
                        play = 'STAND'
                    else:
                        play = 'DOUBLE'
            else:
                play = 'STAND'
        elif softCard==9:
            play = 'STAND'
        else:
            play = 'BLACKJACK'
    #        
    else:
        #Hard totals
        hardTotal = pc1+pc2

        if hardTotal<=7:
            play = 'HIT'
        elif hardTotal==8:
            if trueCount>=2:
                play = 'DOUBLE'
            else:
                play = 'HIT'
        elif hardTotal==9:
            if dc1==2:
                if trueCount>=1:
                    play = 'DOUBLE'
                else:
                    play = 'HIT'
            elif dc1==7:
                if trueCount>=3:
                    play = 'DOUBLE'
                else:
                    play = 'HIT'
            elif 2<dc1<7:
                play = 'DOUBLE'
            else:
                play = 'HIT'
        elif hardTotal==10:
            if dc1<=9:
                play = 'DOUBLE'
            else:
                if dc1==10:
                    if trueCount>=4:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'
                else:
                    if s17==True and trueCount>=4:
                        play = 'DOUBLE'
                    elif s17==False and trueCount>=3:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'
        elif hardTotal==11:
            if dc1<=10:
                play = 'DOUBLE'
            else:
                if s17==False:
                    play = 'DOUBLE'
                else:
                    if trueCount>=1:
                        play = 'DOUBLE'
                    else:
                        play = 'HIT'
        elif hardTotal==12:
            if dc1==2:
                if trueCount>=3:
                    play = 'STAND'
                else:
                    play = 'HIT'
            elif dc1==3:
                if trueCount>=2:
                    play = 'STAND'
                else:
                    play = 'HIT'
            elif dc1==4:
                if trueCount>0:
                    play = 'STAND'
                else:
                    play = 'HIT'
            elif dc1>=7:
                play = 'HIT'
            else:
                play = 'STAND'
        elif hardTotal==13:
            if dc1==2:
                if trueCount>=-1:
                    play = 'STAND'
                else:
                    play = 'HIT'
            elif dc1<=6:
                play = 'STAND'
            else:
                play = 'HIT'
        elif hardTotal==14:
            if dc1<=6:
                play = 'STAND'
            else:
                play = 'HIT'
        elif hardTotal==15:
            if dc1<=6:
                play = 'STAND'
            elif dc1<=8:
                play = 'HIT'
            elif dc1==9:
                if sur==True and trueCount>=2:
                    play = 'SURRENDER'
                else:
                    play = 'HIT'
            elif dc1==10:
                if sur==True:
                    if trueCount<0:
                        play = 'HIT'
                    else:
                        play = 'SURRENDER'
                else:
                    if trueCount>=4:
                        play = 'STAND'
                    else:
                        play = 'HIT'
            else:
                if sur==True:
                    if s17==True:
                        if trueCount>=2:
                            play = 'SURRENDER'
                        else:
                            play = 'HIT'
                    else:
                        if trueCount>=-1:
                            play = 'SURRENDER'
                        else:
                            play = 'HIT'
                else:
                    if s17==False:
                        if trueCount>=5:
                            play = 'STAND'
                        else:
                            play = 'HIT'
                    else:
                        play = 'HIT'
        elif hardTotal == 16:
            if dc1<=6:
                play = 'STAND'
            elif dc1==7:
                play = 'HIT'
            elif dc1==8:
                if sur==True and trueCount>=4:
                    play = 'SURRENDER'
                else:
                    play = 'HIT'
            elif dc1==9:
                if sur==True:
                    if trueCount<=-1:
                        play = 'HIT'
                    else:
                        play = 'SURRENDER'
                else:
                    if trueCount>=4:
                        play = 'STAND'
                    else:
                        play = 'HIT'
            elif dc1==10:
                if sur==True:
                    play = 'SURRENDER'
                else:
                    if trueCount>0:
                        play = 'STAND'
                    else:
                        play = 'HIT'
            else:
                if sur==True:
                    play = 'SURRENDER'
                else:
                    if s17==True:
                        play = 'HIT'
                    else:
                        if trueCount>=3:
                            play = 'STAND'
                        else:
                            play = 'HIT'
        elif hardTotal==17:
            if dc1==11 and s17==False and sur==True:
                play = 'SURRENDER'
            else:
                play = 'STAND'
        else:
            play = 'STAND'

    playLabel.config(text=play)
    root.update()
    
#######################################################################

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

#######################################################################

root = tk.Tk()
root.title('Basic strategy checker')

canvas1 = tk.Canvas(root, width = 600, height = 270)
canvas1.pack()

canvas1.create_line(450, -30, 450, 300, fill="black", width=2)
root.resizable(False, False)

#######################################################################

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

#######################################################################

playLabel = tk.Label(root, text='...')
playLabel.config(font=('Helvetica bold',37),fg='blue')
canvas1.create_window(228, 150, window=playLabel)

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

label1=Label(root, text='Basic Strategy Checker')
label1.config(font=('Helvetica bold',30))
canvas1.create_window(225, 23, window=label1)

button0 = tk.Button(text='Check', command=bsCheck)
canvas1.create_window(420, 150, height=30, width=50,window=button0)

button0 = tk.Button(text='+1', command=addCount)
canvas1.create_window(525, 100, height=60, width=60,window=button0)

button0 = tk.Button(text='-1', command=minCount)
canvas1.create_window(525, 240, height=60, width=60,window=button0)

root.mainloop()