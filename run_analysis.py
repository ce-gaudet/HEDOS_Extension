from pipeline.patient_preparation import (
    create_grouped_rtstruct,
    convert_plan_to_voxels,
)

from pipeline.hedos_pipeline import run_hedos

from utils.validation import validate_inputs


def run_pipeline(
    PATIENT,
    PLANS,
    SIMULATION,
):

    print("Starting HEDOS pipeline")


    print("\nChecking inputs...")
    validate_inputs(
        PATIENT,
        PLANS,
    )


    print("\nPreparing patient structures...")

    grouped_rtstruct = create_grouped_rtstruct(
        PATIENT["ct"],
        PATIENT["rtstruct"],
    )


    print("\nRTSTRUCT prepared")


    for plan_name, dose_file in PLANS.items():

        print("\n===================================")
        print(f"Running {plan_name} plan")
        print("===================================")


        convert_plan_to_voxels(
            PATIENT["ct"],
            grouped_rtstruct,
            dose_file,
        )


        run_hedos(
            plan_name,
            PATIENT,
            SIMULATION,
        )


    print("\nPipeline complete")


if __name__ == "__main__":

    from settings import (
        PATIENT,
        PLANS,
        SIMULATION,
    )


    run_pipeline(
        PATIENT,
        PLANS,
        SIMULATION,
    )