import os
import numpy as np

from workflows import BloodDoseFromFields

from dicom.simulation_parameters import (
    Patient_parameters,
    Treatment_parameters,
    Simulation_parameters,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATIENT_DIR = os.path.join(
    ROOT,
    "input",
    "patient"
)

BLOOD_PATH = os.path.join(
    ROOT,
    "input",
    "blood_path.npy"
)


def run_hedos(
    plan_name,
    PATIENT,
    SIMULATION,
):

    print(f"\nRunning HEDOS: {plan_name}")


    blood_dose_folder = os.path.join(
        "results",
        "blood_dose",
        plan_name
    )

    os.makedirs(
        blood_dose_folder,
        exist_ok=True
    )


    patient_parameters = Patient_parameters(
        gender=PATIENT["gender"],
        tumor_site=PATIENT["tumor_site"],
        tumor_volume_fraction=PATIENT["tumor_volume_fraction"],
        relative_blood_density=PATIENT["relative_blood_density"],
        relative_perfusion=PATIENT["relative_perfusion"],
        organs=PATIENT["organs"],
    )


    simulation_parameters = Simulation_parameters(
        sample_size=SIMULATION["sample_size"],
        nr_steps=SIMULATION["n_steps"],
        dt=SIMULATION["dt"],
        weibull_shape=SIMULATION["weibull_shape"],
        generate_new=SIMULATION["generate_new"],
        random_walk=SIMULATION["random_walk"],
        accumulate=SIMULATION["accumulate"],
    )


    treatment_parameters = Treatment_parameters(
        nr_fractions=SIMULATION["n_fractions"],
        total_beam_on_time=SIMULATION["total_beam_on_time"],
        start_times=SIMULATION["start_times"],
        beam_on_times=SIMULATION["beam_on_times"],
    )


    all_runs = []

    n_runs = SIMULATION["n_runs"]


    for run_idx in range(n_runs):

        print(
            f"HEDOS {plan_name}: run {run_idx + 1}/{n_runs}"
        )

        blood_dose_array = (
            BloodDoseFromFields.blood_dose_distribution(
                simulation_parameters,
                patient_parameters,
                treatment_parameters,
                PATIENT_DIR,
                BLOOD_PATH,
                plan_name,
                run_idx + 1,
            )
        )


        filename = os.path.join(
            blood_dose_folder,
            f"run_{run_idx+1:03d}.npy",
        )


        np.save(
            filename,
            blood_dose_array,
        )


        all_runs.append(
            blood_dose_array
        )


    all_runs = np.stack(
        all_runs,
        axis=0
    )


    np.save(
        os.path.join(
            blood_dose_folder,
            "all_runs.npy",
        ),
        all_runs,
    )


    print(
        f"HEDOS finished: {plan_name}"
    )