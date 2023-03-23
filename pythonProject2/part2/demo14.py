class Students():
    def __init__(self, name, scorce):
        self.name = name
        self.scorce = scorce

    def print_scorce(self):
        if self.scorce >= 80:
            print("良好")
        elif self.scorce >= 70:
            print('中等')
        elif self.scorce >= 60:
            print('及格')
        else:
            print('不及格')


stu1 = Students('lili', 50)
stu1.print_scorce()
