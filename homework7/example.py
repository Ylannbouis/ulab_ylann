# File: example.py

import numpy as np

G = 6.6743e-11 # Gravitational contanst in m^3 kg^-1 s^-2

def escape_velocity(mass, radius):
    """
    Calculates escape velocity of a planet.
    v_esc = (2GM/r)^(1/2)

    Inputs:
    mass (float): mass of the planet in grams
    radius (float): radius of the planet in kg

    Output:
    esc_velocity (float): escape velocity in meters per second
    """
    
    result = 2 * G * mass
    result /= radius

    esc_velocity = np.sqrt(result)
    
    return esc_velocity

def orbital_velocity(mass, radius):
    """
    Calculates orbital velocity of a planet.
    v_orb = (GM/r)^(1/2)

    Inputs:
    mass (float): mass of the planet in kilograms
    radius (float): radius of the planet in meters

    Output:
    orb_velocity (float): orbital velocity in meters per second
    """

    orb_velocity = np.sqrt((G * mass) / radius)
    return orb_velocity


def rocket_launch(rocket_velocities, mass_of_planet, radius_of_planet):
    """
    Determines if a rocket can escape based on its final velocity.

    Inputs:
    rocket_velocities (numpy.ndarray): list of rocket velocities in meters per second
    mass_of_planet (float): mass of the planet in kilograms
    radius_of_planet (float): radius of the planet in meters

    Output:
    statuses (list): statements for each rocket, describes its status.
    """

    esc_velocity = escape_velocity(mass = mass_of_planet,
                                      radius = radius_of_planet)
    
    orb_velocity = orbital_velocity(mass = mass_of_planet,
                                        radius = radius_of_planet)
    
    statuses = []
    for rocket in rocket_velocities:
        final_velocity_of_rocket = rocket[-1]
        
        if final_velocity_of_rocket < orb_velocity:
            statement = "Rocket crashes back into the planet!"
        
        elif orb_velocity <= final_velocity_of_rocket < esc_velocity:
            statement = "Rocket is orbiting around the planet."
        
        else:
            statement = "Rocket left the planet!"

        statuses.append(statement)

    return statuses

import numpy as np

def get_kinetic_energy(masses_and_velocities):
    """
    Takes in a 2-d array of masses and velocities and outputs the kinetic energy
    Inputs: (2-d array) the masses in the 1st row, the velocities in the second
    Outputs: The total kinetic energy of the particles returns False if any mass is negative.
    """
    count = 0
    kinetic_energy = 0
    while count < len(mass_and_velocities):
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