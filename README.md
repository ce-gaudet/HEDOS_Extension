# HEDOS Studio

HEDOS Studio is a frontend workflow for HEDOS 2.0 that prepares patient DICOM data and runs blood dose simulations.

## Features

- RTSTRUCT preprocessing
- Automatic organ grouping
- DICOM → HEDOS conversion
- Blood dose simulation
- Multi-plan comparison

## Requirements

- Python 3.10+
- HEDOS 2.0 installed (`pip install -e .`)
- CT DICOM series
- RTSTRUCT
- RTDOSE

## Project structure

```
input/
    patient/
    phantom/

results/

run_analysis.py
settings.py
organs.py
patient_preparation.py
hedos_pipeline.py
```

## Configuration

Edit only:

```
settings.py
```

Specify:

- CT folder
- RTSTRUCT
- RTDOSE
- Patient parameters
- Simulation parameters

## Run

```bash
python run_analysis.py
```

## Output

Results are written to

```
results/blood_dose/
```