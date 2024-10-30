from goto import goto, label
import random
import time
import random
import threading
global sound
global pressed




def main():
    
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


    B=50*B
    print("AFTER ALL YOUR PURCHASES. YOU NOW HAVE "+str(T)+" DOLLARS LEFT")
    print()
    print("MONDAY MARCH 29 1847")
    print()

####################################################################################################

    goto .one750


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
    
    label .one390
    print("JUNE 7")
    goto .one720

    label .one410
    print("JUNE 21")
    goto .one720

    label .one430
    print("JULY 5")
    goto .one720

    label .one450
    print("JULY 19")
    goto .one720

    label .one470
    print("AUGUST 2")
    goto .one720

    label .one490
    print("AUGUST 16")
    goto .one720

    label .one510
    print("AUGUST 31")
    goto .one720

    label .one530
    print("SEPTEMBER 13")
    goto .one720

    label .one550
    print("SEPTEMBER 27")
    goto .one720

    label .one570
    print("OCTOBER 11")
    goto .one720

    label .one590
    print("OCTOBER 25")
    goto .one720

    label .one610
    print("NOVEMBER 8")
    goto .one720

    label .one630
    print("NOVEMBER 22")
    goto .one720

    label .one650
    print("DECEMBER 6")
    goto .one720

    label .one670
    print("DECEMBER 20")
    goto .one720


    print("YOU HAVE BEEN ON THE TRAIL TOO LONG  ------")
    print("YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER")
    
    goto .five170

    label .one720
    print("1847")

    #***BEGINNING EACH TURN***
    label .one750
    if F>=0:
        goto .one770
    F=0

    label .one770
    if B>=0:
        goto .one790
    B=0

    label .one790
    if C>=0:
        goto .one810
    C=0

    label .one810
    if M1>=0:
        goto .one830
    M1=0
    
    label .one830
    if F>=0:
        goto .one850

    print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")

    label .one850
    F=int(F)
    B=int(B)
    C=int(C)
    M1=int(M1)
    T=int(T)
    M=int(M)
    M2=M

    if S4==1:
        goto .one950
    if K8==1:
        goto .one950
    goto .one990

    label .one950
    T=T-20

    if T<0:
        goto .five080

    print("DOCTOR'S BILL IS $20")
    K8=S4=0

    label .one990
    if M9==1:
        goto .two020

    print("TOTAL MILEAGE IS "+str(M)) #2000

    goto .two040

    print("TOTAL MILEAGE IS 950")

    M9 = 0

    label .two040 
    print(  " FOOD: ",         " BULLETS: ",        " CLOTHING: ",         " MISC. SUPP.: ",          " CASH: ")
    print(" "+str(F)+"   ","   "+str(B)+"   ","     "+str(C)+"   ","       "+str(M1)+"   ","          "+str(T)+"   ")

    if X1==-1:
        goto .two170
    
    X1=X1*(-1)


    label .two080
    print("DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, ")
    print("OR (3) CONTINUE")
    X=input() #2100

    if X>2:
        goto .two150

    if X<1:
        goto .two150

    X=int(X)

    goto .two270

    label .two150
    X=3

    goto .two270

    label .two170
    print("DO YOU WANT TO (1) HUNT, OR (2) CONTINUE") #2170
    X=input() #2180

    if X==1:
        goto .two210
    X=2

    label .two210
    X=X+1

    if X==3:
        goto .two260
        
    if B>39:
        goto .two260

    print("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")

    goto .two170

    label .two260
    X1=X1*(-1) #2260

    if X==1:
        goto .two290

    if X==2:
        goto .two540

    if X==3:
        goto .two720 #2270
    
    #***STOPPING AT FORT***
    label .two290
    print("ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING")
    print("FOOD")
    
    def two330(): # Function for line 2310
        global P
        P=input()
        if  P<0:
            goto .two400
        T=T-P

        if T>=0:
            goto .two400

        print("YOU  DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        print("YOU MISS YOUR CHANCE TO SPEND ON THAT ITEM") #2375

        T=T+P
        P=0

        label .two400
    
    two330() #This is at line 2310

    F=F+(2/3)*P #2410

    print("AMMUNITION")

    two330()

    B=int(B+(2/3)*P*P*50)
    print("CLOTHING")

    two330()

    C=C+(2/3)*P
    print("MISCELLANEOUS SUPPLIES")

    two330()

    M1=M1+(2/3)*P
    M=M-45

    goto .two720

    #***HUNTING*** ########### LINE 2530
    #START ------ Type Line two540
    label .two540
    if B>39:
        goto .two570
    print("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")

    goto .two080

    M=M-45

    #IGNORE-------------------------------------------------
    def get_user_input(sound, input_ready):
        """Gets user input while the timer is running."""
        pressed = input("TYPE " + sound + ": ")
        input_ready.append(pressed)

    def check(sound, pressed):
        """Checks if the user's input matches the sound."""
        if pressed and sound == pressed[0]:
            print("DONE")
        else:
            print("WRONG! The correct sound was: " + sound)
    #-------------------------------------------------------
    def six140():
        """Main game function."""
        rand = random.randint(0, 3)
        gun_sounds = ["BANG", "BLAM", "POW", "WHAM"]
        sound = gun_sounds[rand]


        # Create a list to store user input
        input_ready = []


        # Get user input in the main thread
        get_user_input_thread = threading.Thread(target=get_user_input, args=(sound, input_ready))
        get_user_input_thread.start()

        # Wait for both threads to finish
        get_user_input_thread.join()

        # Check the input after both threads are done
        check(sound, input_ready)

    six140() #LINE 3120

    if pressed and sound == pressed[0]:
        goto .two660
    else:
        goto .two710
    
    label .two660
    print("RIGHT BETWEEN THE EYES---YOU GOT A BIG ONE!!!!")
    print("FULL BELLIES TONIGHT!")
    goto .two720

    label .two710
    print("YOU MISSED---AND YOUR DINNER GOT AWAY.....")

    label .two720
    if F>=13:
        goto .two750
    goto .five060
    
    ###EATING###

    label .two750
    print("DO YOU WANT TO EAT (1) POORLY (2) MODERATELY")
    print("OR (3) WELL")

    E = input() 
    
    if E > 3: 
        goto .two750
    if E < 1:
        goto .two750
    
    int(E)

    F = F - 8 - 5 * E

    if F >= 0:
        goto .two860
    
    print("YOU CAN'T EAT THAT WELL")
    goto .two750
    
    label .two860
    M = M + 200 + (A - 220) / 5 + 10 * round(-1)
    
    L1 = 0
    C1 = 0

    ###RIDERS ATTACK### 
    if (round(-1 ) * 10 > ((M / 100 - 4) 
    ** 2 + 72) / ((M / 100 - 4) ** 2 + 12) - 1): #LINE 2890 - START HERE!!! 
        goto .three550
    
    print("RIDERS AHEAD. THEY ")

    S5 = 0

    if round(-1) < .8:
        goto .two950
    
    print("DON'T ")

    S5 = 1

    label .two950
    print("LOOK HOSTILE")
    print("TACTICS")

    label .two970
    print("(1) RUN (2) ATTACK (3) CONTINUE (4) CIRCLE WAGONS")

    if round(1) > .2:
        goto .three000
    
    S5 = 1 - S5

    label .three000
    T1 = input()

    if T1 < 1:
        goto .two970

    if T1 > 4:
        goto .two970

    T1 = int(T1)

    if S5 == 1:
        goto .three330

    if T1 > 1:
        goto .three110

    M = M + 20

    M1 = M1 - 15 
    
    B = B - 150

    A = A - 40

    goto .three470 # LINE 3100

    label .three110
    if T1 > 2:
        goto .three240

    goto .six140 #START HERE --- LINE 3120












    
main()

