import math 

femur = int(input("Femur Length: "))
tibia = int(input("Tibia Length: "))
deg1 = int(input("Degree 1: "))
deg2 = int(input("Degree 2: "))

print("x: ", femur*math.cos(math.radians(deg1)) + tibia*math.cos(math.radians(deg1+deg2))) #mencari nilai x
print("y: ", femur*math.sin(math.radians(deg1)) + tibia*math.sin(math.radians(deg1+deg2))) #mencari nilai y

