import matplotlib.pyplot as plt
import numpy as np
def plot_cos_and_sin_hor(domain):
    # Plots sin and cos side by side. Inputs = the length of the domain. Outputs = graphs of sin and cosine horizontally
    x = np.linspace(0, domain, 100)
    fig, ax = plt.subplots(1,2, figsize = (10,10)) # Creates two sets of axes
    y1 = np.cos(x)
    y2 = np.sin(x)
    ax[0].plot(x,y1, label="cos(x)")
    ax[0].set_xlabel("X-Axis")
    ax[0].set_ylabel("Y-Axis")
    ax[0].set_title("cos(x)")
    ax[1].plot(x,y2, label="sin(x)")
    ax[1].set_xlabel("X-Axis")
    ax[1].set_ylabel("Y-Axis")
    ax[1].set_title("sin(x)")
    plt.show()
def plot_cos_and_sin_vert(domain):
    # Plots sin and cos vertically. Inputs = the length of the domain. Outputs = graphs of sin and cosine vertically
    x = np.linspace(0, domain, 100)
    fig, ax = plt.subplots(2,1, figsize = (10,10)) # Creates two sets of axes.
    y1 = np.cos(x)
    y2 = np.sin(x)
    ax[0].plot(x,y1, label="cos(x)")
    ax[0].set_xlabel("X-Axis")
    ax[0].set_ylabel("Y-Axis")
    ax[0].set_title("cos(x)")
    ax[1].plot(x,y2, label="sin(x)")
    ax[1].set_xlabel("X-Axis")
    ax[1].set_ylabel("Y-Axis")
    ax[1].set_title("sin(x)")
    plt.show()