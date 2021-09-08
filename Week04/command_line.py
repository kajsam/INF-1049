# started by copying input.py

import sys

def kinetic_energy(m, v):
    """Formula to calculate kinetic energy
    m: mass of an object (in kg)
    v: velocity of an object (in m/s)

    return: energy (in kJ)
    """
    return m * v**2 / 2 / 1000

if __name__ == "__main__":

    # print(help(kinetic_energy)) # arti for ungan

    print(sys.argv)

    # Get the mass
    mass = float(sys.argv[1])

    # Get the velocity
    vel = float(sys.argv[2])

    # Calculate kinetic energy
    ke = kinetic_energy(mass, vel)

    print(f"Mass: {mass} Velocity: {vel} Kinetic energy = {ke: .3f}")
