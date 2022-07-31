class Grade:
    def __init__(self, value=0):
        self._value = value

    def __repr__(self):
        return f'Count point: {self._value}'

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value


grade = Grade(3)
grade2 = Grade(2)
print(grade < grade2)
