"""
Dilution calculations

Only handles water dilution.

Formula:

M1V1 = M2V2

Water added:

Vwater = V2 - V1
"""


def dilution(
    initial_molarity,
    initial_volume,
    final_molarity
):
    """
    Calculate water needed.

    Example:

    dilution(5,100,1)

    {
        "final_volume": 500,
        "water_added": 400
    }

    """


    if initial_molarity <= 0:
        raise ValueError(
            "Initial molarity must be positive"
        )


    if initial_volume <= 0:
        raise ValueError(
            "Volume must be positive"
        )


    if final_molarity <= 0:
        raise ValueError(
            "Final molarity must be positive"
        )


    if final_molarity >= initial_molarity:
        raise ValueError(
            "Final molarity must be lower for dilution"
        )


    # M1V1 = M2V2

    final_volume = (
        initial_molarity
        *
        initial_volume
        /
        final_molarity
    )


    water_added = (
        final_volume
        -
        initial_volume
    )


    return {
        "initial_volume": initial_volume,
        "final_volume": final_volume,
        "water_added": water_added
    }
