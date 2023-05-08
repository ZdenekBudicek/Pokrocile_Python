# Objektově orientované programování

# Atributy a metody
class WizardPlayer:
    wizard_club = True

    # constructor
    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def attack(self):
        print("Útok!")

    def age_checker(self):
        if self.age >= 18:
            print("Můžete hrát")
        else:
            print("Nemůžete hrát. Váš věk je příliš nízký.")

    @staticmethod
    def test_function(n1, n2):
        return n1 + n2

    @classmethod
    def test_function2(cls, player_name, n1, n2):
        return cls(player_name, n1 + n2)


# print(WizardPlayer.test_function(60, 100))
test_player = WizardPlayer.test_function2("Ron", 30, 20)
print(test_player.name)
print(test_player.age)

test_player2 = WizardPlayer.test_function2("Hermiona", 10, 10)
print(test_player2.name)
print(test_player2.age)
