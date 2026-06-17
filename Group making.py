from random import randint
# list of student
students = ["Camilla","Penny","Muriel","Myriam","Sibylle","Kaya","Imane B.","Parita","Elena","Julie","Imane Z."]

# making groups
group_of = 2
x_group = 5


for i in range (x_group) :
    
    for k in range (group_of):
        rdm = randint(0,len(students) -1)
        print(students[rdm])
        students.pop(rdm)

    print()




