from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.config import SimulationConfig
from src.metrics import calculate_metrics
from src.simulation import build_default_simulation


def main() -> None:
    rows = []
    for degradation_per_hour in [0.02, 0.04, 0.06, 0.08]:
        config = SimulationConfig(degradation_per_hour=degradation_per_hour)
        simulation = build_default_simulation(config)
        result = simulation.run()
        rows.append(
            {
                "degradation_per_hour": degradation_per_hour,
                **calculate_metrics(result),
            }
        )

    output_path = Path("results/csv/sensitivity_analysis.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_path, index=False)
    print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
