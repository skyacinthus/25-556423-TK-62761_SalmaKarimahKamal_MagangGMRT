#homogenous transformation 

import math
import numpy as np
import matplotlib.pyplot as plt

def rot_z(theta):
    # rotasi z 
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])


def rot_y(theta):
    # rotasi y 

    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
    ])


def trans_x(length):
    # trans x (dipakai utk femur dan tibia)
    return np.array([
        [1, 0, 0, length],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def trans_xyz(x, y, z):
    # base utk tibia
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])


femur = float(input("Femur Length: "))
tibia = float(input("Tibia Length: "))
deg_base1 = math.radians(float(input("Rotational degree at femur base: ")))
deg_base2 = math.radians(float(input("Rotation degree at tibia base: ")))
deg1 = math.radians(float(input("Vertical Degree at femur: ")))
deg2 = math.radians(float(input("Vertical Degree at tibia: ")))

# base
T0 = np.eye(4)

T1 = rot_z(deg_base1) @ rot_y(-deg1) @ trans_x(femur)
x1, y1, z1 = T1[0:3, 3] # extract kol 4 (nilai x y z) 

T2 = trans_xyz(x1, y1, z1) @ (rot_z(deg_base1 + deg_base2) @ rot_y(-(deg1 + deg2)) @ trans_x(tibia))
x2, y2, z2 = T2[0:3, 3] 

print(np.round(T2, 4))

print("end effector")
print("x: ", x2)
print("y: ", y2)
print("z: ", z2)

x_coords = [0, x1, x2]
y_coords = [0, y1, y2]
z_coords = [0, z1, z2]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.plot(x_coords, y_coords, z_coords, marker="o", markersize=8, linewidth=4)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(-(femur + tibia), (femur + tibia))
ax.set_ylim(-(femur + tibia), (femur + tibia))
ax.set_zlim(0, (femur + tibia))
ax.grid(True)

plt.show()