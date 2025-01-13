from __init__ import InitAnimals

class Eagle(InitAnimals):
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def getEagleName(self):  # self를 추가합니다.
        return super().getName()