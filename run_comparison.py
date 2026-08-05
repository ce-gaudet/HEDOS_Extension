from pipeline.dicom_preparation import create_grouped_rtstruct, convert_plan_to_voxels
from pipeline.hedos_pipeline import run_hedos
from utils.validation import validate_inputs
from settings import PATIENT, SIMULATION
import os

RD1 = "/Users/charles-etiennegaudet/Downloads/RD_35m_MUHC.dcm"
RD2 = "/Users/charles-etiennegaudet/Downloads/RD_35m_Optimized.dcm"

PLANS = {os.path.splitext(os.path.basename(RD1))[0]: RD1,os.path.splitext(os.path.basename(RD2))[0]: RD2,}

def run_pipeline(PATIENT, PLANS, SIMULATION):
    print("Starting HEDOS pipeline")
    validate_inputs(PATIENT, PLANS)
    print("\nPreparing patient structures...")
    grouped_rtstruct = create_grouped_rtstruct(PATIENT["ct"], PATIENT["rtstruct"])
    print("\nRTSTRUCT prepared")
    for plan_name, dose_file in PLANS.items():
        print("\n===================================")
        print(f"Running {plan_name}")
        print("===================================")
        convert_plan_to_voxels(PATIENT["ct"], grouped_rtstruct, dose_file)
        run_hedos(plan_name, PATIENT, SIMULATION)
    print("\nPipeline complete")

if __name__ == "__main__":
    run_pipeline(PATIENT, PLANS, SIMULATION)