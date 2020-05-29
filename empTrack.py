



#  Description: This program Create a menu-driven Python program that functions as a phone book. Input is from a data file called phone.txt
#             that consists of comma-separated values with one entry per line

#  Pre-condition: Use functions where appropriate,The main part of your program should be at the bottom and not interspersed between the functions
#               The main part of your program should consist mostly of function calls

#  post-condition: Menu-driven program



import os
def  menu (choices):

    #  Description:  This function creates Menu.
    #  Pre-condition: choices : list
    #  Post-condition: user's choice : int
    
    count=0
    print()
    for i in choices:
        
        print(str(count)+". "+i)
        count=count+1
    
    print()
    userChoice=input("choice? ")
   
    while(userChoice.isdigit()!=True):
        print()
        print(" No-letters or symbols allowed !! Please enetr your choice again")
        print()
        userChoice=input("choice? ")
       
        
        
   
    return int(userChoice)



def readFile (filename):
    
    #  Description: This function reads text from text file
    #  Pre-condition: filename : str
    #  Post-condition: phonebook : list
    if os.path.exists(filename):
        phonebook=[]
       
        count=0
        with open(filename) as file:
            data = file.read().splitlines()
            
        for alline in data:
            phonebook.append(alline.rstrip().split(','))
        return phonebook
    else:
        print()
        print("Input file doesnot exists, creating new phonebook")
        x=open(filename,"w")
        phonebook=[]
        return phonebook
       
    



def printEntries (phonebook):
    
    #  Description:  This function prints formatted version of  text from textfile
    #  Pre-condition: phonebook : list
    #  Post-condition: None
   
    
    print()
    print("{0:<30} {1:>14}".format("Name","Phone # "))
    print("{0:<30} {1:>14}".format("_________________","__________________"))
   
    for i in  phonebook:
       
       
        print("{0:<30} {1:>14}".format(i[0],i[1]))



def writeFile (filename, phonebook):
    
    #  Description: Writes the phonebook in new text file phone02.txt
    #  Pre-condition: filename : str, phonebook : list
    #  Post-condition: None
    
    alist=[]
    MyFile=open(filename,'w')
    for i in phonebook:
       dataStr=i[0]+","+i[1]
       MyFile.write(dataStr)
       MyFile.write('\n')
    MyFile.close()
    print()
    
   

def addToPhonebook (phonebook):

    
    #  Description: adds the name  to phonebook
    #  Pre-condition:  phonebook, input
    #  Post-condition: None
    
    myList=[]
    nameList=[]
    if phonebook is not None:
        name=input("please enter new name: ")
        for i in phonebook:
            nameList.append(i[0])
        if name in nameList:
           
            print("name is already in the phonebook,  duplicates not allowed")
        else:
            phone=input("Please enter phone num: ")
            myList.append(name)
            myList.append(phone)
            phonebook.append(myList)
           
            print(name,"added to the phonebook ")
    elif phonebook is None:
        name=input("please enter new name: ")
        
        phone=input("Please enter phone num: ")
        myList.append(name)
        myList.append(phone)
        phonebook.append(myList)
       
        print(name,"added to the phonebook ")
        


        
    
    
   
def deleteFromPhonebook (phonebook):

    
    #  Description: deletes name from phonebook 
    #  Pre-condition:  phonebook, name
    #  Post-condition: None

    
    name=input("please enter the name to be deleted: ")
    nameList=[]
   
    for i in phonebook:
        nameList.append(i[0])
        if i[0]==name:
           valueofName=i
    if name in nameList:
        phonebook.remove(valueofName)
        
        print(name, " Deleted from the phonebook ")
    else:
       
        print("name not found in the phonebook,nothing deleted")



def searchPhonebook (phonebook):
    
    #  Description: searces name from phonebook 
    #  Pre-condition: name , phonebook 
    #  Post-condition: None

    
    nameList=[]
    name=input("enter  name to search for: ")
    for i in phonebook:
        if i[0]==name or name in i[0]:
            nameList.append(i)
            
    if len(nameList)>0:
       
        printEntries (sorted(nameList))
        
    else:
        print()
        print("< No Results>")
        
           

            
   
def main():
    
   #  Description: Calls all the functions
    #  Pre-condition: None
    #  Post-condition: None
    phonebook = readFile("phone.txt")
    
    
    choices = ['exit', 'search phonebook', 'add entry', 'delete entry', 'print phonebook']
    option = menu(choices)
   
    while option != 0:
        if option == 1:
            searchPhonebook (phonebook)
        elif option == 2:
            addToPhonebook (phonebook)
           
        elif option == 3:
            deleteFromPhonebook (phonebook)
        elif  option == 4:
            printEntries(phonebook)
        else:
            print ('not an option')
        option = menu(choices)
       
    writeFile("phone.txt", phonebook) 
    print()
    
   
        

    
    
main()
    
    
    
    
        
