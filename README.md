Engineering Trade-off Simulator

Purpose:
This program is a small, FRC-inspired engineering tool that evaluates and compares design options using simplified assumptions.

The project was created to help me practice object-oriented programming.

What does the program do?
- Accepts user-defined "weighting factors" for speed, torque, and cost.
- Normalizes weights so they sum  up to 1 (in case user inputed them as percentages or some other format)
- Evaluates one or more design options using a weighted scoring model
- Applies a minimum torque constraint penalty
- Assigns evaluations to each design
- Identifies design focus (performance, power, cost, or balanced)
- Ranks multiple designs and provides summary statiistics

Scoring Model 
Final Score = (speed x speed_weight + torque x torque_weight) - cost x cost_weight

- designs that have a torque less than 5 recieve an additional final score penalty
- Higher scores indicate better trade-offs

by: Tanay Mishra
