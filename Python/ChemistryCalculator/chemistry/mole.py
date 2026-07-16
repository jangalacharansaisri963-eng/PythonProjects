"""
Mole calculations

Conversions:

Mass <-> Moles
Particles <-> Moles
Gas Volume <-> Moles
"""

from chemistry.constants import (
    AVOGADRO,
    MOLAR_VOLUME_STP,
)


# ==========================
# Mass and Moles
# ==========================

def moles_from_mass(
    mass,
    molar_mass
):
    """
    n = m / M
    """

    if molar_mass <= 0:
        raise ValueError(
            "Molar mass must be positive"
        )

    return mass / molar_mass



def mass_from_moles(
    moles,
    molar_mass
):
    """
    m = nM
    """

    if molar_mass <= 0:
        raise ValueError(
            "Molar mass must be positive"
        )

    return moles * molar_mass



# ==========================
# Particles and Moles
# ==========================

def moles_from_particles(
    particles
):
    """
    n = N / NA
    """

    return particles / AVOGADRO



def particles_from_moles(
    moles
):
    """
    N = n × NA
    """

    return moles * AVOGADRO



# ==========================
# Gas Volume and Moles
# ==========================

def moles_from_volume(
    volume,
    molar_volume=MOLAR_VOLUME_STP
):
    """
    n = V / V0
    """

    return volume / molar_volume



def volume_from_moles(
    moles,
    molar_volume=MOLAR_VOLUME_STP
):
    """
    V = n × V0
    """

    return moles * molar_volume
