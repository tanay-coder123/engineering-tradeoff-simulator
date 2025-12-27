print("Engineering Trade-Off Simulator")
print("This tool evaluates design choices using simplified engineering assumptions\n")


print("Enter weighting factors for the evaluation (does not need to add to 1):")

speed_weight = float(input("Speed weight: "))
torque_weight = float(input("Torque weight: "))
cost_weight = float(input("Cost weight: "))

total_weight = speed_weight + torque_weight + cost_weight

speed_weight /= total_weight
torque_weight /= total_weight
cost_weight /= total_weight

print("\nNormalized Weights Applied:")
print(f" Speed: {round(speed_weight, 2)}")
print(f" Torque: {round(torque_weight, 2)}")
print(f" Cost: {round(cost_weight, 2)}\n")


class Design:
    def __init__(self, name, speed, torque, cost):
        self.name = name
        self.speed = speed
        self.torque = torque
        self.cost = cost
        self.score = 0
        self.evaluation = ""
        self.focus = ""

        self.calculate_score()
        self.evaluate_tradeoff()
        self.find_design_focus()

    def calculate_score(self):
        self.score = (
            self.speed * speed_weight +
            self.torque * torque_weight -
            self.cost * cost_weight
        )


        if self.torque < 5:
            self.score -= 1

    def evaluate_tradeoff(self):
        if self.torque < 5:
            self.evaluation = "Fails minimum torque constraint."
        elif self.score >= 6:
            self.evaluation = "Well-balanced trade-off."
        elif self.score >= 4:
            self.evaluation = "Acceptable trade-off, but with limitations."
        else:
            self.evaluation = "Not optimal trade-off."

    def find_design_focus(self):
        if self.speed > self.torque and self.speed > self.cost:
            self.focus = "Performance-focused (speed-driven)"
        elif self.torque > self.speed and self.torque > self.cost:
            self.focus = "Power-focused (torque-driven)"
        elif self.cost < self.speed and self.cost < self.torque:
            self.focus = "Cost-efficient"
        else:
            self.focus = "Balanced properties"

    def display(self):
        print(f"Design: {self.name}")
        print(f" Score: {round(self.score, 2)}")
        print(f" Evaluation: {self.evaluation}")
        print(f" Design Focus: {self.focus}\n")


def user_input(prompt):
    while True:
        value = float(input(prompt))
        if 1 <= value <= 10:
            return value
        print("Please enter a value between 1 and 10.")


designs = []
amount_of_designs = int(input("How many designs would you like to evaluate? "))

for i in range(amount_of_designs):
    print(f"\nDesign {i + 1}")
    name = input("Enter design name: ")

    speed = user_input("Enter speed rating (1-10): ")
    torque = user_input("Enter torque rating (1-10): ")
    cost = user_input("Enter cost rating (1-10): ")

    design = Design(name, speed, torque, cost)
    designs.append(design)


if amount_of_designs == 1:
    print("\nDesign Evaluation")
    designs[0].display()

else:
    designs.sort(key=lambda d: d.score, reverse=True)

    print("\nDesign Rankings:")
    for i, design in enumerate(designs, start=1):
        suffix = "th"
        if i == 1:
            suffix = "st"
        elif i == 2:
            suffix = "nd"
        elif i == 3:
            suffix = "rd"

        print(f"{i}{suffix} Place:")
        design.display()

    scores = [d.score for d in designs]
    print("Summary Analysis:")
    print(f" Highest Score: {round(max(scores), 2)}")
    print(f" Average Score: {round(sum(scores) / len(scores), 2)}")
    print(f" Score Range: {round(max(scores) - min(scores), 2)}")
