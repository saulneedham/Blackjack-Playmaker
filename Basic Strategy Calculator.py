import tkinter as tk
from tkinter import *

#######################################################################

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
    if TrueCountEntry.get() == '':
        trueCount = 0
    else:
        trueCount = float(TrueCountEntry.get())

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

cardOptions = ['2','3','4','5','6','7','8','9','10','A']
gameOptions = ['S17','H17']
dasOptions = ['DAS','NDAS']
surrenderOptions = ['Sur','NSur']

#######################################################################


root = tk.Tk()
root.title('Basic strategy checker')

canvas1 = tk.Canvas(root, width = 450, height = 270)
canvas1.pack()

#Player card 1
variableCard1 = StringVar(root)
variableCard1.set(cardOptions[0])
menumask= OptionMenu(root, variableCard1, *cardOptions)
canvas1.create_window(200, 250, window=menumask)

#Player card 2
variableCard2 = StringVar(root)
variableCard2.set(cardOptions[0])
menumask= OptionMenu(root, variableCard2, *cardOptions)
canvas1.create_window(250, 250, window=menumask)

#Dealer card
variableCardDealer = StringVar(root)
variableCardDealer.set(cardOptions[0])
menumask= OptionMenu(root, variableCardDealer, *cardOptions)
canvas1.create_window(225, 70, window=menumask)

#DAS/NDAS
variableDAS = StringVar(root)
variableDAS.set(dasOptions[0])
menumask= OptionMenu(root, variableDAS, *dasOptions)
canvas1.create_window(30, 110, window=menumask)

#S17/H17
variableGame = StringVar(root)
variableGame.set(gameOptions[0])
menumask= OptionMenu(root, variableGame, *gameOptions)
canvas1.create_window(30, 140, window=menumask)

#Sur/NSur
variableSur = StringVar(root)
variableSur.set(surrenderOptions[0])
menumask= OptionMenu(root, variableSur, *surrenderOptions)
canvas1.create_window(30, 170, window=menumask)

#True Count
TrueCountEntry = tk.Entry (root)
canvas1.create_window(40, 197, height=20, width=40, window=TrueCountEntry)
label0 = tk.Label(root, text='TC:')
canvas1.create_window(10, 197, window=label0)

#######################################################################

playLabel = tk.Label(root, text='')
playLabel.config(font=('Helvetica bold',37),fg='blue')
canvas1.create_window(228, 150, window=playLabel)

label0 = tk.Label(root, text='SETTINGS')
label0.config(font=('Helvetica 9 underline'))
canvas1.create_window(30, 85, window=label0)

label1=Label(root, text='Basic Strategy Checker')
label1.config(font=('Helvetica bold',30))
canvas1.create_window(225, 23, window=label1)

button0 = tk.Button(text='Check', command=bsCheck)
canvas1.create_window(420, 150, height=30, width=50,window=button0)

root.mainloop()