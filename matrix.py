"""
================================================================================================================================
Author: Sagar Subedi
Description: This program prompts the user to enter elements of matrix and does operations(mentioned in post-conditions). 
Pre-conditions:
               1. Input must be user entered
               2. Matrix elements must be float
Post-conditions
               1. Function to add two 5 X 5 matrices
               2. Function to multiply two 5 X 5 matrices
               3. Function to multiply a 5 X 5 matrix by a number
               4. Function to divide a 5 X 5 matrix by a number
================================================================================================================================
"""
"""
Function name: createMatrix
Parameters: None
Pre-codition: 1.Elements must be of float type
              2.Input validation 
Post-condition: 1. return a matrix
"""

def createMatrix():

    Matrix=[]
    Ct=1
    while(len(Matrix)!=5):      #Since ct is initialized as 1 previously,we want to loop until it is equal to row X columns
        subList=[]
        try:
            #catching exception to validate input
            for j in range(5): 
                Numbers=float(input("Please enter element No: "+str(Ct)+" of your matrix: "))   
                subList.append(Numbers)
                Ct+=1
              #checking if length is 5, if so the row is completed     
            Matrix.append(subList)   
        except:
            print("Error Input !! Please enter a float number..please start over ")
            Ct=1
            continue
    return(Matrix)


"""
Function name: addMatrices
Parameters: two matrices
Pre-codition: none
Post-condition: add two 5 X 5 matrices
"""
def addMatrices(matrix1,matrix2):
    result=[[0 for i in range(5)] for i in range(5)]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):        #nesting two loops to iterate over elements
            result[i][j]=matrix1[i][j]+matrix2[i][j]
    return result

"""
Function name: multiplyMatrices
Parameters: two matrices
Pre-codition: none
Post-condition: multiply two 5 X 5 matrices
"""
def multiplyMatrices(matrix1,matrix2):
    result=[[0 for i in range(5)] for i in range(5)]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j]=matrix1[i][j]*matrix2[i][j] #nesting two loops to iterate over elements
    return result


"""
Function name: numMultiplymatrices
Parameters: a matrix
Pre-codition: none
Post-condition: multiply by a number
"""
def numMultiplymatrices(matrix1):
    num=float(input("Please enter a number to multiply: "))
    try:
        result=[[0 for i in range(5)] for i in range(5)]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):  #nesting two loops to iterate over elements
                result[i][j]=matrix1[i][j]*num
    except:
        print("Please enter a valid input")
    return result
        
"""
Function name: numDividematrices
Parameters: a matrix
Pre-codition: none
Post-condition: divide by a number
"""
def numDividematrices(matrix1):
    num=float(input("Please enter a number to divide: "))
    try:
        result=[[0 for i in range(5)] for i in range(5)]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):  #nesting two loops to iterate over elements
                result[i][j]=matrix1[i][j]/num
    except:
        print("Please enter a valid input")
    return result

"""
Function name: allfunctionCalls
Parameters: none
Pre-codition: none
Post-condition: call all functions
"""
def allfunctionCalls():
    print("Let's get started by creating our first matrix")
    print("")
    m1=createMatrix()
    print("")
    print("Now the second matrix")
    print("")
    m2=createMatrix()
    print("Result by adding two matrices")
    print("")
    print(addMatrices(m1,m2))
    print("Result from multiplication of two matrices")
    print("")
    print(multiplyMatrices(m1,m2))
    print("Result of matrix multiplied by a number")
    print("")
    print (numMultiplymatrices(m1))
    print("Result of matrix divided by a number")
    print("")
    print(numDividematrices(m1))
    

#main
def main():
    allfunctionCalls()
main()
