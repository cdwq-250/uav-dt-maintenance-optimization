from pathlib import Path

import matplotlib.pyplot as plt

from src.simulation import SimulationResult


def plot_timeline(result: SimulationResult, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 4))

    station_ids = [station.station_id for station in result.workstations]
    station_index = {station_id: index for index, station_id in enumerate(station_ids)}

    for event in result.event_log:
        y = station_index[event["station_id"]]
        width = event["finish"] - event["start"]
        color = "#4C78A8" if event["event"] == "process" else "#F58518"
        label = event.get("order_id", event.get("reason", "maintenance"))
        ax.barh(y, width, left=event["start"], color=color, edgecolor="white")
        ax.text(event["start"] + width / 2, y, label, ha="center", va="center", fontsize=8)

    ax.set_yticks(range(len(station_ids)))
    ax.set_yticklabels(station_ids)
    ax.set_xlabel("Time")
    ax.set_title("Production and Maintenance Timeline")
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
