"""
====================================================
                    HEDOS Studio

Configure your patient and simulation here.

After editing this file, run:

    python run_analysis.py

====================================================
"""

# ============================================================
# PATIENT
# ============================================================

PATIENT = {

    # DICOM inputs
    "ct": "/Users/charles-etiennegaudet/Documents/Screenshots/MUHC/MUHC_CT-2",
    "rtstruct": "/Users/charles-etiennegaudet/Documents/Screenshots/MUHC/RS_muhc.dcm",

    # Patient characteristics
    "gender": "M",
    "tumor_site": "lung",
    "tumor_volume_fraction": 0.06,

    # Physiological scaling
    "relative_blood_density": 1.0,
    "relative_perfusion": 1.0,

    # Organs included in the blood circulation model
    "organs": [
        "brain",
        "heart",
        "lung",
        "liver",
        "spleen",
        "kidneys",
        "large_veins",
        "tumor",
        "red_marrow",
        "oesophagus",
        "aorta",
        "inferior_vena_cava",
        "stomach",
        "pancreas",
    ],
}

# ============================================================
# TREATMENT PLANS
# ============================================================

PLANS = {

    "INITIAL": "/Users/charles-etiennegaudet/Documents/Screenshots/MUHC/RD_muhc.dcm",

    "OPTIMIZED": "/Users/charles-etiennegaudet/Documents/Screenshots/MUHC/RD_lymphotec.dcm",

}

# ============================================================
# SIMULATION
# ============================================================

SIMULATION = {

    # Monte Carlo
    "n_runs": 2,
    "sample_size": 2000,

    # Time discretization
    "n_steps": 3400,
    "dt": 0.05,

    # Blood flow model
    "weibull_shape": 2,
    "generate_new": True,
    "random_walk": True,
    "accumulate": False,

    # Treatment delivery
    "n_fractions": 30,
    "total_beam_on_time": 140,
    "start_times": [0, 90],
    "beam_on_times": [70, 70],
}