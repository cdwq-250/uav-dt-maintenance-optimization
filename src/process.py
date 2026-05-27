from src.order import ProcessStep


def default_uav_route() -> list[ProcessStep]:
    return [
        ProcessStep("frame_assembly", "assembly", 5.0),
        ProcessStep("avionics_installation", "electronics", 4.0),
        ProcessStep("propulsion_test", "testing", 3.0),
        ProcessStep("final_inspection", "inspection", 2.0),
    ]


def short_repair_route() -> list[ProcessStep]:
    return [
        ProcessStep("fault_diagnosis", "inspection", 2.0),
        ProcessStep("module_replacement", "electronics", 3.0),
        ProcessStep("flight_readiness_test", "testing", 2.5),
    ]
