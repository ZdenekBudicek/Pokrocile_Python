# 4 pilíře OOP
# Encapsulation = zapouzdření
# Abstraction = abstrakce = dáváme přístup pouze k tomu, co je zapotřebí
# Nic na omezení přístupu není, jen existuje konvence kterou říkáš neměň to a to je že se dá do proměnné _ podtržítko

class WizardPlayer:

    def __init__(self, name="anonym", age=0):
        self._name = name
        self._age = age

    def attack(self):
        print("Útok!")

    def age_checker(self):
        if self.age >= 18:
            print("Můžete hrát")
        else:
            print("Nemůžete hrát. Váš věk je příliš nízký.")


# print(WizardPlayer.test_function(60, 100))
player1 = WizardPlayer("david", 25)
player1._name = "martin"
# player1.attack = "ahoj"
# print(player1.attack)
