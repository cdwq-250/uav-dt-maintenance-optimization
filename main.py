from pathlib import Path

from src.config import SimulationConfig
from src.metrics import summarize_results
from src.simulation import build_default_simulation
from src.visualization import plot_timeline


def main() -> None:
    config = SimulationConfig()
    simulation = build_default_simulation(config)
    result = simulation.run()

    print(summarize_results(result))

    output_dir = Path("results/figures")
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_timeline(result, output_dir / "baseline_timeline.png")


if __name__ == "__main__":
    main()
