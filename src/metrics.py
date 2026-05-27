from src.simulation import SimulationResult


def calculate_metrics(result: SimulationResult) -> dict[str, float]:
    completion_times = [order.completion_time or 0.0 for order in result.orders]
    tardiness = [
        max(0.0, (order.completion_time or 0.0) - order.due_date)
        for order in result.orders
    ]
    maintenance_downtime = sum(
        station.equipment.maintenance_downtime for station in result.workstations
    )
    maintenance_count = sum(
        station.equipment.maintenance_count for station in result.workstations
    )
    busy_time = sum(
        event["finish"] - event["start"]
        for event in result.event_log
        if event["event"] == "process"
    )
    makespan = max(completion_times)
    workstation_count = max(1, len(result.workstations))

    return {
        "makespan": makespan,
        "average_flow_time": sum(completion_times) / len(completion_times),
        "total_tardiness": sum(tardiness),
        "on_time_rate": sum(1 for value in tardiness if value == 0.0) / len(tardiness),
        "maintenance_count": float(maintenance_count),
        "maintenance_downtime": maintenance_downtime,
        "utilization": busy_time / (makespan * workstation_count),
    }


def summarize_results(result: SimulationResult) -> str:
    metrics = calculate_metrics(result)
    lines = [
        "Simulation Summary",
        f"policy: {result.policy_name}",
        f"dispatch_rule: {result.dispatch_rule}",
    ]
    lines.extend(f"{key}: {value:.3f}" for key, value in metrics.items())
    return "\n".join(lines)
