class Auto:
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine

    def drive_ahead(self):
        if self.model == 'Toyota' and self.engine > 0:
            return 'Ця машина може їхати вперед'
        else:
            return 'Ця машина не може їхати вперед'

    def drive_back(self):
        if self.model == 'Ford' and self.engine > 1:
            return 'Ця машина може їхати назад'
        else:
            return 'Ця машина не може їхати назад'


class AutoUpgrade(Auto):
    def __init__(self, model, color, engine, left_turn, right_turn):
        super().__init__(model, color, engine)
        self.right_turn = right_turn
        self.left_turn = left_turn

    def drive_left(self):
        if self.left_turn is True and self.model == 'Renault':
            return 'Ця машина може повернути наліво'
        else:
            return 'Ця машина не може повернути наліво'

    def drive_right(self):
        if self.right_turn is True and self.model == 'Nissan':
            return 'Ця машина може повернути направо'
        else:
            return 'Ця машина не може повернути направо'


toyota = Auto('Toyota', 'Red', 2.0)
ford = Auto('Ford', 'Black', 4.5)
renault = AutoUpgrade('Renault', 'Green', 3.0, True, False)
nissan = AutoUpgrade('Nissan', 'Yellow', 1.5, False, True)


t = toyota.drive_ahead()
f = ford.drive_back()
r = renault.drive_left()
n = nissan.drive_right()
