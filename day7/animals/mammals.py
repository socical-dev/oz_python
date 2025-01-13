class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name}({self.breed})이(가) 멍멍 짖습니다."
        