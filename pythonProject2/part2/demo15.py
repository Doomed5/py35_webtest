class Person():
    def __init__(self,name,wg):
        self.name = name
        self.wg = wg
    def eat(self):
        self.wg += 1
        print(f'姓名：{self.name}吃完以后,体重：{self.wg}')
    def run(self):
        self.wg -= 0.5
        print(f'姓名：{self.name}吃完以后,体重：{self.wg}')

per1 = Person('xiaoming',70)
per1.eat()
per1.run() 