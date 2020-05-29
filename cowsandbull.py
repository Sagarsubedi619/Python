



# Description: This is Bulls and cows game

# pre-condition: 1.User's 4-digit number MUST be stored in a list and also  program's 4-digit number MUST be stored in a list
#               2.a function to compare two lists and to return a list with two elements (e.g. the first element represents Bulls and the second Cows)
#               3. Import random and use functions in random

# Post-condition: number of bulls and cows should be in output and if user gueses correctly number attempts should also be shown in the output



import random

#Function to generate list of four different numbers

def generateList():

    randomList=[]

    n1 = random.randint(1, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4=random.randint(0, 9)
    while not  (n1!=n2 and n2!=n3 and n3!=n4 and n4!=n1 and n1!=n3 and n2!=n4):   # making sure the digits are not repeated
        n1 = random.randint(1, 9)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4=random.randint(0, 9)

    randomList.append(n1)
    randomList.append(n2)
    randomList.append(n3)
    randomList.append(n4)

    return(randomList)




# Function to compare two list of numbers and find number of bulls and cows

def operation(inputList,randomList):
    cow=0
    bull=0
    for i in range(4):
        if inputList[i]==randomList[i]:
            bull=bull+1
            
        elif inputList[i] in randomList:
            cow=cow+1
    print("Bull/s: ",bull)
    print("Cow/s : ",cow)
            


#main function       

def main():

    randomList=generateList()                                    #function call

#printing solution (Random number List) for checking purpose

    print()
    print("********** For checking purpose *****************")
    print("Randomly generated Solution: ",randomList)
    print("*************************************************")
    print()
    print("Welcome to the Bulls and Cows Game")
    print()


#operating the code by calling functions

    num=input("Please enter four digit number: ")
    print()
    inputList=[]
    count=1
    for i in num:
        i=int(i)
        inputList.append(i)
    while (inputList!=randomList):
        count=count+1
        operation(inputList,randomList)                           #function call
        print()
        num=input("Please enter four digit number: ")
        print()
        inputList=[]
        for i in num:
           i=int(i)
           inputList.append(i)

    print()
    print("Congratulations you won in",count,"number of attempt/s.")
    print()
    print("Thank you for using my Program")

main()
    
