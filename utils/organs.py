ORGAN_RECIPES = {

    "lung": [
        [
            "lung_upper_lobe_left",
            "lung_lower_lobe_left",
            "lung_upper_lobe_right",
            "lung_middle_lobe_right",
            "lung_lower_lobe_right",
        ],
        [
            "lung_left",
            "lung_right",
        ],
        [
            "left_lung",
            "right_lung",
        ],
        [
            "lung",
        ],
    ],


    "kidneys": [
        [
            "kidney_left",
            "kidney_right",
        ],
        [
            "left_kidney",
            "right_kidney",
        ],
        [
            "kidneys",
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
        [
            "sacrum",
            "os_coxae",
            "femora_upper",
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

        [
            "sternum",
            "clavicles",
            "scapulae",
            "Vertebrae_C",
            "Vertebrae_T",
            "Vertebrae_L",
            "ribs",
        ],
    ],


    "red_marrow": [
        [
            "bone_marrow_pelvic",
            "bone_marrow_thorax",
        ],
        [
            "red_marrow",
        ],
    ],


    "large_veins": [
        [
            "portal_vein_and_splenic_vein",
            "pulmonary_vein",
        ],
        [
            "large_veins",
        ],
    ],


    "superior_vena_cava": [
        [
            "superior_vena_cava",
        ],
        [
            "svc",
        ],
    ],


    "inferior_vena_cava": [
        [
            "inferior_vena_cava",
        ],
        [
            "ivc",
        ],
    ],


    "aorta": [
        [
            "aorta",
        ],
    ],


    "pulmonary_artery": [
        [
            "pulmonary_artery",
        ],
    ],


    "heart": [
        [
            "heart",
        ],
        [
            "cardiac",
        ],
    ],


    "brain": [
        [
            "brain",
        ],
    ],


    "liver": [
        [
            "liver",
        ],
    ],


    "spleen": [
        [
            "spleen",
        ],
    ],


    "pancreas": [
        [
            "pancreas",
        ],
    ],


    "adrenals": [
        [
            "adrenal_left",
            "adrenal_right",
        ],
        [
            "gland_adrenal_left",
            "gland_adrenal_right",
        ],
        [
            "gland_adrenal_tot",
        ],
        [
            "adrenals",
        ],
    ],


    "thyroid": [
        [
            "thyroid",
        ],
        [
            "gland_thyroid",
        ],
    ],


    "oesophagus": [
        [
            "esophagus",
        ],
        [
            "oesophagus",
        ],
    ],


    "stomach_oesophagus": [
        [
            "stomach",
            "esophagus",
        ],
        [
            "stomach_oesophagus",
        ],
    ],


    "small_intestine": [
        [
            "small_bowel",
        ],
        [
            "small_intestine",
        ],
    ],


    "large_intestine": [
        [
            "large_bowel",
        ],
        [
            "large_intestine",
        ],
        [
            "colon",
        ],
        [
            "colon_ascending",
            "colon_sigmoid",
            "colon_descending",
        ],
        [
            "colon_tot",
        ],
    ],


    "bladder": [
        [
            "bladder",
        ],
    ],


    "bronchial": [
        [
            "bronchus",
        ],
        [
            "bronchial",
        ],
    ],


    "lymph_nodes": [
        [
            "lymph_nodes",
        ],
    ],


    "skeletal_muscle": [
        [
            "skeletal_muscle",
        ],
        [
            "muscle",
        ],
    ],


    "fat": [
        [
            "fat",
        ],
        [
            "adipose",
        ],
    ],


    "skin": [
        [
            "skin",
        ],
    ],
}