class Robot:
    pass


robot_1 = Robot()
robot_1.battery = 24
robot_1.arm_length = 0.6

robot_2 = Robot()
robot_2.battery = 48
robot_2.arm_length = 0.5

print(f"Výdrž baterie: {robot_1.battery}")
print(f"Délka rukou: {robot_1.arm_length}")

print(f"Výdrž baterie: {robot_2.battery}")
print(f"Délka rukou: {robot_2.arm_length}")
