# ursina engine game

from ursina import *
import numpy as np


def update():
    global e
    for entity in e:
        entity.y += 0.003
        entity.x = entity.y/k*np.sin(20*entity.y)
        entity.z = entity.y/k*np.cos(20*entity.y)

        if entity.y > 1.5*np.pi:
            entity.y = 0


app = Ursina()

num = 300
k = 2
y = np.linspace(0, 1.5*np.pi, num)
x = y/k*np.sin(20*y)
z = y/k*np.cos(20*y)

e = [None]*num
for i in range(num):
    e[i] = Entity(model="sphere", color=color.random_color(), scale=0.1, position=(x[i], y[i], z[i]))
    # update()


camera.position = (0, 2.5, -20)

app.run()
