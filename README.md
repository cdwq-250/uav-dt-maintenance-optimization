# UAV Digital Twin Maintenance Optimization

This project studies maintenance-aware production scheduling for UAV assembly or maintenance workshops. It builds a lightweight digital-twin simulation, compares maintenance strategies, and exports experiment results for thesis writing.

## Project Goals

- Model orders, processes, workstations, and equipment reliability.
- Simulate baseline production under different scheduling rules.
- Compare corrective, preventive, and condition-based maintenance policies.
- Generate CSV results and figures for analysis.
- Provide reusable paper materials for an undergraduate thesis.

## Structure

```text
uav-dt-maintenance-optimization/
├── docs/              # specification, assumptions, thesis and experiment plans
├── src/               # simulation, scheduling, maintenance and visualization modules
├── experiments/       # runnable experiment scripts
├── results/           # generated CSV, figures and logs
└── paper_materials/   # thesis tables, figures and descriptions
```

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Run experiments:

```bash
python experiments/run_baseline.py
python experiments/run_maintenance_compare.py
python experiments/run_sensitivity_analysis.py
python experiments/run_marl_experiment.py
```

Generated outputs are written to `results/csv`, `results/figures`, and `results/logs`.

## Current Status

The repository contains an initial deterministic simulation scaffold. The MARL experiment file is a placeholder entry point so the project structure can grow without disrupting the baseline experiments.
