class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
        
    def fly(self):
        return f"{self.name}이(가) 날라다닙니다. 날개 길이는 {self.wingspan}m 입니다."