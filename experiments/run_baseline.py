from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.config import SimulationConfig
from src.metrics import calculate_metrics
from src.simulation import build_default_simulation


def main() -> None:
    rows = []
    for dispatch_rule in ["fifo", "edd", "spt"]:
        simulation = build_default_simulation(
            SimulationConfig(),
            dispatch_rule=dispatch_rule,
            maintenance_policy="corrective",
        )
        result = simulation.run()
        rows.append({"dispatch_rule": dispatch_rule, **calculate_metrics(result)})

    output_path = Path("results/csv/baseline.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_path, index=False)
    print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
