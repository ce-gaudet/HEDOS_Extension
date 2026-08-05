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
    "ct": "/Users/charles-etiennegaudet/Downloads/35m_CT",
    "rtstruct": "/Users/charles-etiennegaudet/Downloads/RS_35m.dcm",

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
        "red_marrow",
        "oesophagus",
        "stomach_oesophagus",
        "small_intestine",
        "large_intestine",
        "bladder",
        "pancreas",
        "adrenals",
        "thyroid",
        "tumor",
    ],
}

# ============================================================
# SIMULATION
# ============================================================

SIMULATION = {

    # Monte Carlo
    "n_runs": 1, #Use 1 for run_analysis, and use 2+ for run_comparison to assess variability
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