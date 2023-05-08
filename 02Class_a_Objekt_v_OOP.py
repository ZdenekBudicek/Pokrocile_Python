class Robot:

    # contructor
    def __init__(self, battery, arm_length):
        self.bat = battery
        self.arm_leng = arm_length


# Tvoříme objekty podle classy
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(58, 1.1)
robot_4 = Robot(24, 0.9)
blabla = Robot(50, 15)

print(f"Výdrž baterie: {robot_1.bat}")
print(f"Délka rukou: {robot_1.arm_leng}")

print(f"Výdrž baterie: {robot_2.bat}")
print(f"Délka rukou: {robot_2.arm_leng}")

print(f"Výdrž baterie: {robot_3.bat}")
print(f"Délka rukou: {robot_3.arm_leng}")

print(f"Výdrž baterie: {robot_4.bat}")
print(f"Délka rukou: {robot_4.arm_leng}")

print(f"Výdrž baterie: {blabla.bat}")
print(f"Délka rukou: {blabla.arm_leng}")
