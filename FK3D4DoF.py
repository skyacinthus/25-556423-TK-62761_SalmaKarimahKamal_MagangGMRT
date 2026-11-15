import math 
import matplotlib.pyplot as plt

femur = int(input("Femur Length: "))
tibia = int(input("Tibia Length: "))
deg_base1 = math.radians(int(input("Rotational degree at femur base: ")))
deg_base2 = math.radians(int(input("Rotation degree at tibia base: ")))
deg1 = math.radians(int(input("Vertical Degree at femur: ")))
deg2 = math.radians(int(input("Vertical Degree  at tibia: ")))

# nilai x
x1 = (femur*math.cos(deg1))*math.cos(deg_base1)
x2 = x1 + (tibia*math.cos(deg1+deg2))*math.cos(deg_base1 + deg_base2)

# nilai y 
y1 = (femur*math.cos(deg1))*math.sin(deg_base1)
y2 = y1 + (tibia*math.cos(deg1+deg2))*math.sin(deg_base1 + deg_base2)

# nilai z
z1 = (femur*math.sin(deg1))
z2 = z1 + (tibia*math.sin(deg1+deg2))


print("end effector")
print("x: ", x2) #mencari nilai x
print("y: ", y2) #mencari nilai y
print("z: ", z2) #mencari nilai z

x_coords = [0, x1, x2]
y_coords = [0, y1, y2]
z_coords = [0, z1, z2]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.plot(
    x_coords, y_coords, z_coords, marker="o", markersize=8, linewidth=4
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(- (femur + tibia), (femur + tibia)) # ukuran garfik tergantung hasil yg didapat
ax.set_ylim(- (femur + tibia), (femur + tibia))
ax.set_zlim(0, (femur + tibia))
ax.grid(True)

plt.show() #display
