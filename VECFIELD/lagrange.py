import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#import the libraries
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider



# Generating Half Moon DataSets
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=300, noise=0.1, random_state=0)


# defining function that will generate the Lagrangian polynomial that passes through the points

def lagrange(X):
    # define the number of points
    n = len(X)
    # define the polynomial
    def L(x):
        # define the polynomial
        p = 0
        # create a loop to add the terms
        for i in range(n):
            # define the term
            term = X[i,1]
            # create a loop to add the factors
            for j in range(n):
                if j != i:
                    term = term*(x-X[j,0])/(X[i,0]-X[j,0])
            # add the term to the polynomial
            p = p + term
        # return the polynomial
        return p
    # return the function
    return L



# Graphic interface to select the points with the mouse and generate the Lagrangian polynomial


# define the figure
fig = plt.figure()
plt.scatter(X[:,0], X[:,1], c=y)
# define the axes
ax = plt.axes(xlim=(-1.5, 2.5), ylim=(-1    , 2))
# plot the data
plt.scatter(X[:,0], X[:,1], c=y)
Xplot = np.array([]).reshape(0,2)
# define function that place a point when the user clicks on the figure
def onclick(event):
    # get the coordinates of the point
    x = event.xdata
    y = event.ydata
    # plot the point
    plt.scatter(x,y, color = 'red')
    # update the figure
    fig.canvas.draw()
    # add the point to the list
    global Xplot
    Xplot = np.vstack([Xplot, [x,y]])


# plot the lagrangian polynomial after each new point is added
def plotLagrange(event):
    # get the number of points
    n = len(X)
    # generate the Lagrangian polynomial
    L = lagrange(Xplot)
    # plot the polynomial
    x = np.linspace(-1.5,2.5,100)
    #set y axis limits
    plt.ylim(-1,2)
    plt.plot(x,L(x), color = 'red')
    # update the figure
    fig.canvas.draw()
    #erase the previous curve but keep the points on the figure
    plt.clf()
    plt.scatter(X[:,0], X[:,1], c=y)
    plt.scatter(Xplot[:,0], Xplot[:,1], color = 'red')






# attribute the function onclick to the event button_press_event
cid = fig.canvas.mpl_connect('button_press_event', onclick)
# attribute the function plotLagrange to the event button_press_event
cid = fig.canvas.mpl_connect('button_press_event', plotLagrange)

# show the figure
plt.show()


