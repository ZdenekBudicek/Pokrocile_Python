class Robot:

    # constructor
    def __init__(self, battery, arm_length):
        self.battery = battery
        self.arm_length = arm_length
        self.days_to_repair = 365


# Tvoříme objekty podle classy
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(50, 0.6)
robot_4 = Robot(38, 0.4)

print(robot_1.battery)
print(robot_1.arm_length)
print(robot_1.days_to_repair)

print(robot_2.battery)
print(robot_2.arm_length)
print(robot_2.days_to_repair)

print(robot_3.battery)
print(robot_3.arm_length)
print(robot_3.days_to_repair)

print(robot_4.battery)
print(robot_4.arm_length)
print(robot_4.days_to_repair)
