# ============================================================
# PATIENT PREPARATION
#
# Functions:
#
# 1) Group RTSTRUCT structures
# 2) Convert DICOM inputs into HEDOS numpy format
#
# Called automatically by run_analysis.py
#
# ============================================================


import os


from dicom.dicom_conversion import dicom_conversion

from dicom.rtstruct_processing import merge_rtstruct


from utils.organs import ORGAN_RECIPES





# ============================================================
# CREATE GROUPED RTSTRUCT
# ============================================================


def create_grouped_rtstruct(
    CT_FOLDER,
    RTSTRUCT
):


    print("""
===================================
PATIENT STRUCTURE PREPARATION
===================================
""")


    print(
        "CT:",
        CT_FOLDER
    )


    print(
        "RTSTRUCT:",
        RTSTRUCT
    )



    grouped_rtstruct_location = os.path.join(
        os.path.dirname(RTSTRUCT),
        "segmentations_grouped.dcm"
    )



    merge_rtstruct(

        RTSTRUCT,

        CT_FOLDER,

        grouped_rtstruct_location,

        groups=ORGAN_RECIPES

    )



    print(
        "[SETUP] Grouped RTSTRUCT saved:"
    )


    print(
        grouped_rtstruct_location
    )


    return grouped_rtstruct_location





# ============================================================
# CONVERT RD TO HEDOS VOXEL INPUTS
# ============================================================


def convert_plan_to_voxels(
    CT_FOLDER,
    grouped_rtstruct,
    RTDOSE
):


    print("""
===================================
DICOM TO HEDOS VOXEL CONVERSION
===================================
""")


    print(
        "RTDOSE:",
        RTDOSE
    )


    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "input",
        "patient",
    )


    dicom_conversion(
        CT_FOLDER,
        grouped_rtstruct,
        RTDOSE,
        output_dir=output_dir,
    )


    print(
        "[SETUP] NumPy inputs ready"
    )