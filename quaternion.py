# Name: Sagar Subedi
# Assignment

import math

def createRotationQuaternion(axis,angle):
    angleInRadians=angle*(math.pi/180)
    x=axis[0]
    y=axis[1]
    z=axis[2]
    rotationQuaternion=[math.cos(angleInRadians/2),math.sin(angleInRadians/2)*x,math.sin(angleInRadians/2)*y,
    math.sin(angleInRadians/2)*z]
    return rotationQuaternion

def createPointQuaternion(point):
    Px=point[0]
    Py=point[1]
    Pz=point[2]
    pointQuaternion=[0,Px,Py,Pz]
    return pointQuaternion

def multiplyQuaternion(Q1,Q2):
    Q3=[Q1[0]*Q2[0]-Q1[1]*Q2[1]-Q1[2]*Q2[2]-Q1[3]*Q2[3],
        Q1[0]*Q2[1]+ Q1[1]*Q2[0]+ Q1[2]*Q2[3]- Q1[3]*Q2[2],
        Q1[0]*Q2[2]+ Q1[2]*Q2[0]+ Q1[3]*Q2[1]- Q1[1]*Q2[3],
        Q1[0]*Q2[3]+ Q1[3]*Q2[0]+ Q1[1]*Q2[2]- Q1[2]*Q2[1]]
    return Q3

def getConjugateOfQuaternion(Quat):
    a=Quat[0]
    bi=Quat[1]*(-1)
    ci=Quat[2]*(-1)
    di=Quat[3]*(-1)
    conjugate=[a,bi,ci,di]
    return conjugate

def createResult(axis,point,angle):
    rotationQuaternion=createRotationQuaternion(axis,angle)
    pointQuaternion=createPointQuaternion(point)
    halfwayRotation=multiplyQuaternion(rotationQuaternion,pointQuaternion)
    conjugate=getConjugateOfQuaternion(rotationQuaternion)
    rotatedPoint=multiplyQuaternion(halfwayRotation,conjugate)
    print("Quaternion after rotation:", rotatedPoint)
    print("")
    print("Points after rotation    : ",round(rotatedPoint[1],3),round(rotatedPoint[2],3),round(rotatedPoint[3],3))


def main():
    print("1. Rotate the point (0.123, 0.331, 0.998) by 73 degrees around the x-axis")
    print("")
    createResult([1,0,0],[0.123,0.331,0.998],73)
    
    print("")
    print("2. Rotate the point (0.661, 0.834, 0.528) by 15 degrees around the y-axis")
    print("")
    createResult([0,1,0],[0.661, 0.834, 0.528],15)

    print("")
    print("3. Rotate the point (0.348, 0.387, 0.169) by 45 degrees around the z-axis")
    print("")
    createResult([0,0,1],[0.348, 0.387, 0.169],45)

    print("")
    print("4. Rotate the point (0.433, 0.834, 0.367) by 85 degrees around the <875, 332, 238> axis")
    print("")
    createResult([875,332,238],[0.433, 0.834, 0.367],85)
    

main()
    
