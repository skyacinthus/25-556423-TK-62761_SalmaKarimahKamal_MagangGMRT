import math 
import matplotlib.pyplot as plt

femur = int(input("Femur Length: "))
tibia = int(input("Tibia Length: "))
deg1 = math.radians(int(input("Degree 1: ")))
deg2 = math.radians(int(input("Degree 2: ")))

x0 = 0
x1 = femur*math.cos(deg1)
x2 = x1 + tibia*math.cos(deg1+deg2)
y0 = 0
y1 = femur*math.sin(deg1) 
y2 = y1 + tibia*math.sin(deg1+deg2)

print("end effector")
print("x: ", x2) #mencari nilai x
print("y: ", y2) #mencari nilai y

x_coords = [x0, x1, x2]
y_coords = [y0, y1, y2]

plt.figure(figsize=(6, 6))

plt.plot(
    x_coords, y_coords, marker="o", markersize=8, linewidth=4
)

plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(- (femur + tibia), (femur + tibia)) # ukuran garfik tergantung hasil yg didapat
plt.ylim(- (femur + tibia), (femur + tibia))
plt.grid(True)

plt.show() #display