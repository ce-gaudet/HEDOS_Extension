from pipeline.dicom_preparation import create_grouped_rtstruct, convert_plan_to_voxels
from pipeline.hedos_pipeline import run_hedos
from utils.validation import validate_inputs
from settings import PATIENT, SIMULATION
import os

RTDOSE = "/Users/charles-etiennegaudet/Documents/HEDOS_Data/CE_CT/RD_lymphotec.dcm"

RD_name = os.path.splitext(os.path.basename(RTDOSE))[0]

def run_pipeline(PATIENT, RTDOSE, SIMULATION):
    print("Starting HEDOS pipeline")
    validate_inputs(PATIENT, {"PLAN": RTDOSE})
    print("\nPreparing patient structures...")
    grouped_rtstruct = create_grouped_rtstruct(PATIENT["ct"], PATIENT["rtstruct"])
    print("\nRTSTRUCT prepared")
    print("\n===================================")
    print("Running treatment plan")
    print("===================================")
    convert_plan_to_voxels(PATIENT["ct"], grouped_rtstruct, RTDOSE)
    run_hedos(RD_name, PATIENT, SIMULATION)
    print("\nPipeline complete")

if __name__ == "__main__":
    run_pipeline(PATIENT, RTDOSE, SIMULATION)