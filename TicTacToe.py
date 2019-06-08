## 
## Made by Ratan R. Ojha and Utkarsh Verma
##

print("Welcome to tic tac toe","Player 1: X and Player 2: O", sep="\n")
print("Your response must be integer from 1 to 9", "[1,2,3]","[4,5,6]","[7,8,9]",sep="\n")
print("Let the game begin")

input("Press Enter to continue...")
P1='X'
P2='O'

R1=["   ","   ","   "]
R2=["   ","   ","   "]
R3=["   ","   ","   "]

############################
#                           INPUT LOGIC                             #                
############################

K=0
for i in ['X','O','X','O','X','O','X','O','X','O']:
    print("Its the chance of ",i)
    
    T=0
    while T==0:
        try:
            response=int(input("Enter spot to be marked: "))
        except:
            print("Invalid input")
            continue
        if response in [1,2,3,4,5,6,7,8,9]:

            if response in range(1,4):
                if R1[response-1]=="   ":
                    R1[response-1]=i
                    T=1
                else:
                    print("Already marked")
                    T=0

            elif response in range(4,7):
                if R2[response-4]=="   ":
                    R2[response-4]=i
                    T=1
                else:
                    print("Already marked")
                    T=0

            elif response in range(7,10):
                if R3[response-7]=="   ":
                    R3[response-7]=i
                    T=1
                else:
                    print("Already marked")
                    T=0

        else:
            print("Invalid input")
            T=0
    
    

    print(R1,R2,R3,sep="\n")

################################
#                               WIN LOGIC                                            #
################################

    for x in [R1,R2,R3]:
        if x[0]==x[1] and x[1]==x[2] and x[0]!="   ": 
            print(x[0]," Won the game, thanks for playing")
            K=1
    if K==1:
        break
            
    for y in range(3): 
        if R1[y]==R2[y] and R2[y]==R3[y] and R1[y]!="   ": 
            print(R1[y]," Won the game, thanks for playing")
            K=1
    if K==1:
        break
            
    if R1[0]==R2[1] and R2[1]==R3[2] and R1[0]!="   ": 
        print(R1[0]," Won the game, thanks for playing")
        
        break
        
    if R1[2]==R2[1] and R2[1]==R3[0] and R1[2]!="   ": 
        print(R1[2]," Won the game, thanks for playing")
        
        break
        
    for x in range(1):
        if ((R1[0]!="   " and R2[0]!="   " and R3[0]!="   ") and(R1[1]!="   " and R2[1]!="   " and R3[1]!="   ") and (R1[2]!="   " and R2[2]!="   " and R3[2]!="   ")): 
            print("Game is Draw, thanks for playing")
            K=1
    if K==1:
        break



input("Press Enter to exit...")
quit()
