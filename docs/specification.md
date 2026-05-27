# Project Specification

## Topic

UAV digital-twin maintenance optimization for production scheduling.

## Core Problem

UAV production and maintenance workshops face uncertain equipment degradation, order delivery pressure, and resource conflicts. The project builds a simulation model that connects process scheduling with equipment maintenance decisions, then evaluates how different maintenance policies affect completion time, delay, utilization, and maintenance cost.

## Main Inputs

- Order set: order ID, due date, priority, and process route.
- Process route: operation sequence, required workstation type, and processing time.
- Workstation set: capability, queue state, and assigned equipment.
- Equipment state: health level, failure threshold, degradation rate, and repair time.
- Maintenance policy: corrective, preventive, condition-based, or learning-based decision logic.

## Main Outputs

- Makespan.
- Average order flow time.
- Tardiness and on-time delivery rate.
- Equipment utilization.
- Maintenance count and maintenance downtime.
- Composite objective value.

## Implementation Scope

The first version focuses on a discrete-event simulation with rule-based scheduling and rule-based maintenance. Reinforcement learning or multi-agent reinforcement learning can be added after the baseline is stable.
