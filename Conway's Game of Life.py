# CONWAY'S GAME OF LIFE
import numpy as np #numpy
import matplotlib.pyplot as plt #matplotlib
from matplotlib.animation import FuncAnimation #animation
array = np.array([[0,0,1,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,0,1,1]]) #2D array (glider mess)
world = np.zeros((50,50)) #50x50 area 
world[20:26, 20:32] = array #placement in the field
fig, ax = plt.subplots() #frame
img = ax.imshow(world, cmap="gray") #view of matrix
def update(frame): #frame is a parameter as event in tkinter, counter 
    global world # it will change after executing function
    new_world = np.zeros((50,50))
    #shifting
    North = np.roll(world, shift=-1, axis=0) 
    South = np.roll(world, shift=1, axis=0)
    East = np.roll(world, shift=1, axis=1)
    West = np.roll(world, shift=-1, axis=1)
    South_West = np.roll((np.roll(world, shift=-1, axis=1)), shift=1, axis=0)
    South_East = np.roll((np.roll(world, shift=1, axis=1)), shift=1, axis=0)
    North_West = np.roll((np.roll(world, shift=-1, axis=1)), shift=-1, axis=0)
    North_East = np.roll((np.roll(world, shift=1, axis=1)), shift=-1, axis=0)
    #all sum of neighbors
    neighbor = North + South + East + West + North_East + South_East + North_West + South_West
    #numpy boolean indexing for life cycle 
    new_world[(world == 0) & (neighbor == 3)] = 1  
    new_world[(world == 1) & (neighbor == 2)] = 1
    new_world[(world == 1) & (neighbor == 3)] = 1
    img.set_data(new_world) #in every frame image will change
    world = new_world.copy()
animation = FuncAnimation(fig, func=update, frames=200, interval=75)
plt.show()
