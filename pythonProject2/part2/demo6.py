import random
classroom = [[],[],[]]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i in teachers:
    classroom[random.randint(0,2)].append(i)
    #teachers.remove(i)
print(classroom)