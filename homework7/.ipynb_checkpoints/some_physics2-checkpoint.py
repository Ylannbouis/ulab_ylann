import numpy as np

def get_kinetic_energy(masses_and_velocities):
    """
    Takes in a 2-d array of masses and velocities and outputs the kinetic energy
    Inputs: (2-d array) the masses in the 1st row, the velocities in the second
    Outputs: The total kinetic energy of the particles returns False if any mass is negative.
    """
    count = 0
    kinetic_energy = 0
    while count < len(masses_and_velocities):
        kinetic_energy += 1/2 * masses_and_velocities[count, 0] * (masses_and_velocities[count, 1]**2)
        count += 1
    return kinetic_energy

def get_momentum(masses_and_velocities):
    """
    Returns the momentum of multiple masses with their velocities
    Inputs: mass and velocity of each particle (2d array)
    Outputs: The momentum (a number)
    """
    sum = np.sum(particle[0] * particle[1] for particle in masses_and_velocities)
    return sum

def shape_of_orbit(e):
    """
    Prints the shape of an orbit given its eccentricity
    Input: e, the eccentricity
    Ouput: A print statement with the shape of the orbit
    """
    if e == 0:
        print("Circle")
    elif e < 1:
        print("Elipse")
    elif e == 1:
        print("Parabola")
    else:
        print("Hyperbola")