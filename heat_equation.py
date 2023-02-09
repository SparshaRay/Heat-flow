import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin


fps = 60
edgelen = 1
resol = 100
timestep = 0.01
k = 0.5
deltdellen = timestep/(edgelen/resol)


class Mesh :
    def __init__(self, pos, state) :
        self.pos = pos
        self.state = state

    def get_state(self) :
        return self.state

    def update_state(self, state) :
        self.state = state


oldgrid = [[Mesh((i,j), sin(0.1*(i+j))+sin(0.1*(i-j))) for i in range(resol)] for j in range(resol)]
newgrid = oldgrid


def mesh_update() :
    global oldgrid
    for j in range(resol) :
        for i in range(resol) :
            pdex = k * deltdellen * ( oldgrid[i][j].get_state() - oldgrid[(i-1)%resol][j].get_state()/2 - oldgrid[(i+1)%resol][j].get_state()/2 )
            pdey = k * deltdellen * ( oldgrid[i][j].get_state() - oldgrid[i][(j-1)%resol].get_state()/2 - oldgrid[i][(j+1)%resol].get_state()/2 )
            newgrid[i][j].update_state( oldgrid[i][j].get_state() - pdex - pdey)
    oldgrid = newgrid


fig = plt.figure()
img = plt.imshow(np.asarray([[oldgrid[i][j].get_state() for i in range(resol)] for j in range(resol)]))


def render(frame) :
    plt.xlabel('Iteration no. '+str(frame).zfill(3))
    mesh_update()
    img.set_data(np.asarray([[oldgrid[i][j].get_state() for i in range(resol)] for j in range(resol)]))
    return img


display = FuncAnimation(fig, render, interval=1000/fps)
plt.show()