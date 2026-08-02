"""
Input validation for HEDOS Studio.
"""

import os


def validate_inputs(patient, plans):
    """
    Check that all required files and folders exist.
    """

    print("\nChecking inputs...\n")

    # --------------------------------------------------------
    # CT
    # --------------------------------------------------------

    if not os.path.isdir(patient["ct"]):
        raise FileNotFoundError(
            f"CT folder not found:\n{patient['ct']}"
        )

    print("✓ CT folder")

    # --------------------------------------------------------
    # RTSTRUCT
    # --------------------------------------------------------

    if not os.path.isfile(patient["rtstruct"]):
        raise FileNotFoundError(
            f"RTSTRUCT not found:\n{patient['rtstruct']}"
        )

    print("✓ RTSTRUCT")

    # --------------------------------------------------------
    # RTDOSE files
    # --------------------------------------------------------

    for plan_name, dose in plans.items():

        if not os.path.isfile(dose):
            raise FileNotFoundError(
                f"{plan_name} RTDOSE not found:\n{dose}"
            )

        print(f"✓ {plan_name} RTDOSE")

    print("\nAll inputs are valid.\n")