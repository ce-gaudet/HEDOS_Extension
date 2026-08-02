ORGAN_RECIPES = {

    "lung": [
        [
            "lung_upper_lobe_left",
            "lung_lower_lobe_left",
            "lung_upper_lobe_right",
            "lung_middle_lobe_right",
            "lung_lower_lobe_right",
        ],
    ],

    "kidneys": [
        [
            "kidney_left",
            "kidney_right",
        ],
    ],

    "bone_marrow_pelvic": [
        [
            "sacrum",
            "hip_left",
            "hip_right",
            "femur_left",
            "femur_right",
        ],
    ],

    "bone_marrow_thorax": [
        [
            "sternum",
            "clavicula_left",
            "clavicula_right",
            "scapula_left",
            "scapula_right",
            "vertebrae_body",
            "intervertebral_discs",
        ]
        + [f"rib_left_{i}" for i in range(1, 13)]
        + [f"rib_right_{i}" for i in range(1, 13)],
    ],

    "red_marrow": [
        [
            "bone_marrow_pelvic",
            "bone_marrow_thorax",
        ],
    ],

    "large_veins": [
        [
            "portal_vein_and_splenic_vein",
            "pulmonary_vein",
        ],
    ],

    "oesophagus": [
        [
            "esophagus",
        ],
    ],
}