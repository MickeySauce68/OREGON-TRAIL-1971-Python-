import random
import time
from goto import with_goto

'''


def death():
    print()
    print("DUE TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW")
    print("FORMALITIES WE MUST GO THROUGH")
    print()
    print("WOULD YOU LIKE A MINISTER?")
    C0=str(input())
    print("WOULD YOU LIKE A FANCY FUNERAL?")
    C0=str(input())
    print("WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?")
    C0=str(input())
    if C0=="YES":
        pass #GOTO 5310
    print("BUT YOUR AUNT SADIE IN ST. LOUIS IS REALLY WORRIED ABOUT YOU")
    print()
    pass #GOTO 5330
    print("THAT WILL BE $4.50 FOR THE TELEGRAPH CHARGE")
    print()
    print("WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
    print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
    print("BETTER LUCK NEXT TIME")
    print()
    print()
    print("".ljust(30) + "SINCERELY")
    print()
    print("".ljust(17) + "THE OREGON CITY CHAMBER OF COMMERCE")
    exit()





print("DO YOU NEED INSTRUCTIONS (YES/NO)")
C0=input()
if C0!="NO":
    print()
    print()
    print("THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
    print("INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847.")
    print("YOUR FAMILY OF FIVE WILL COVER THE 2040 MILE OREGON TRAIL")
    print("IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.")
    print()
    print("YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST")
    print("   PAID $200 FOR A WAGON.")
    print("YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE")
    print("   FOLLOWING ITEMS:")
    print()
    print("     OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM")
    print("            THE MORE YOU SPEND, THE FASTER YOU'LL GO")
    print("               BECAUSE YOU'LL HAVE BETTER ANIMALS")
    print()
    print("     FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE")
    print("               IS OF GETTING SICK")
    print()
    print("     AMMUNITION - $1 BUYS A BELT OF 50 BULLETS")
    print("            YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS")
    print("               AND BANDITS, AND FOR HUNTING FOOD")
    print()
    print("     CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD")
    print("               WEATHER YOU WILL ENCOUNTER WHEN CROSSING")
    print("               THE MOUNTAINS")
    print()
    print("     MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND")
    print("               OTHER THINGS YOU WILL NEED FOR SICKNESS")
    print("               AND EMERGENCY REPAIRS")
    print()
    print()
    print("YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -")
    print("OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG")
    print("THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT")
    print("THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET")
    print("MORE FOOD.")
    print("WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,")
    print("YOU WILL BE TOLD TO TYPE IN A WORD (ONE THAT SOUNDS LIKE A ")
    print("GUN SHOT). THE FASTER YOU TYPE IN THAT WORD AND HIT THE")
    print("\"RETURN\" KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.")
    print()
    print("AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS")
    print("EXCEPT BULLETS")
    print("WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A \"$\".")
    print()
    print("GOOD LUCK!!!")
    print()
    print()
print("HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?")
print("  (1) ACE MARKSMAN,  (2) GOOD SHOT,  (3) FAIR TO MIDDLIN\'")
print("         (4) NEED MORE PRACTICE,  (5) SHAKY KNEES")
print("ENTER ONE OF THE ABOVE -- THE BETTER YOU CLAIM YOU ARE, THE")
print("FASTER YOU'LL HAVE TO BE WITH YOUR GUN TO BE SUCCESSFUL.")

while True:
    try:
        D9=input()
        if int(D9)<=5:
            D9=0
            break
    except:
        pass
        
X1=-1
D3=0 
M9=0 
M=0
F2=0
F1=0
S4=0
K8=0
T=-1

while T<0:
    print()
    print()
    print("HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM")
    while True:
        try:
            A=int(input())
            while A<200:
                print("NOT ENOUGH")
                A=int(input())
            while int(A)>300:
                print("TOO MUCH")
                A=int(input())
            break
        except:
            pass
    print("HOW MUCH DO YOU WANT TO SPEND ON FOOD")
    while True:
        try:
            F=int(input())
            if F>=0:
                break
        except:
            pass
    print("HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION")
    while True:
        try:
            B=int(input())
            if B>=0:
                break
        except:
            pass
    print("HOW MUCH DO YOU WANT TO SPEND ON CLOTHING")
    while True:
        try:
            C=int(input())
            if C>=0:
                break
        except:
            pass
    print("HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES")
    while True:
        try:
            M1=int(input())
            if M1>=0:
                break
        except:
            pass
    T=700-A-F-B-C-M1
    if T<0:
        print("YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN")


B=B*50
print("AFTER ALL YOUR PURCHASES. YOU NOW HAVE "+str(T)+" DOLLARS LEFT")
print()
print("MONDAY MARCH 29 1847")
print()
'''



@with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    if i == stop:
        goto .end

    result.append(i)
    i += 1
    goto .begin

    label .end
    return result

range(1,10)

    
'''
if M>=2040:
    goto .five430

#***SETTING DATE***
D3=D3+1
print()
print("MONDAY")
if D3>10:
    goto .one300

if D3==1:
    goto .one310
if D3==2:
    goto .one330
if D3==3:
    goto .one350
if D3==4:
    goto .one370
if D3==5:
    goto .one390
if D3==6:
    goto .one410
if D3==7:
    goto .one430
if D3==8:
    goto.one450
if D3==9:
    goto .one410
if D3==10:
    goto .one410
    
label .one300

if D3-10==1:
    goto .one510
if D3-10==2:
    goto .one530
if D3-10==3:
    goto .one550
if D3-10==4:
    goto .one570
if D3-10==5:
    goto .one590
if D3-10==6:
    goto .one610
if D3-10==7:
    goto .one630
if D3-10==8:
    goto .one650
if D3-10==9:
    goto .one670
if D3-10==10:
    goto .one690

label .one310
print("APRIL 12")
goto .one720

label .one330
print("APRIL 26")
goto .one720

label .one350
print("MAY 10")
goto .one720

label .one370
print("MAY 24")
goto .one720

label .begin
print()
'''
