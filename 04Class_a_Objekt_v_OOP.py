class Robot:

    # constructor
    def __init__(self, battery, arm_length):
        self.battery = battery
        self.arm_length = arm_length
        self.actions_to_control = 1000

    def step_forward(self):
        print("Robot udělal krok vpřed")
        self.actions_to_control -= 1

    def step_back(self):
        print("Robot udělal krok vzad")
        self.actions_to_control -= 1


# Tvoříme objekty podle classy
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(50, 0.6)
robot_4 = Robot(38, 0.4)

print(robot_1.battery)
print(robot_1.arm_length)
print(robot_1.actions_to_control)
robot_1.step_forward()
robot_1.step_back()
robot_1.step_forward()
robot_1.step_back()
robot_1.step_forward()
robot_1.step_back()
robot_1.step_forward()
robot_1.step_back()
print(robot_1.actions_to_control)
