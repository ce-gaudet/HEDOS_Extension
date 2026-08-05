# HEDOS Extension

HEDOS Extension contains the code developed to extend the original HEDOS workflow. It automates patient preparation from DICOM (CT, RTSTRUCT, RTDOSE), groups DICOM handling functions into a single workflow, and provides workflows for single-plan and multi-plan blood dose simulations.

## Usage

Simulation and patient parameters are configured in:

```text
settings.py
```

Utility functions are located in:

```text
utils/
```

including `organs.py`, which defines the mapping used to merge clinical organ and substructure names from the RTSTRUCT into the organ names expected by HEDOS.

Two execution scripts are provided:

- `run_single.py` – for a single RTDOSE plan.
- `run_comparison.py` – for comparing multiple RTDOSE plans.

For both scripts, the only required modification is the RTDOSE file path(s). Once updated, simply execute:

```bash
python run_single.py
```

or

```bash
python run_comparison.py
```

Most figures are automatically saved instead of displayed. The only interactive visualization retained is the 3D slice viewer.

## Output

Results are written to:

```text
results/
```

Temporary HEDOS input files generated during DICOM conversion are written to:

```text
input/patient/
```