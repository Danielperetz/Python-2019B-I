class Student:

    # class level property
    sum_students=0

    def __init__(self):
        Student.sum_students+=1

        # object level property
        self.id=Student.sum_students
    

    # object level function
    def print_Id(self):
        print("my id:",self.id, " , all students:",Student.sum_students)
    

    # class level function
    @classmethod
    def print_sum(class_level):
        print(class_level.sum_students)



s1=Student()
Student.print_sum()     # 1
s1.print_Id()           # my id: 1 , all students: 1

s2=Student()
Student.print_sum()     # 2
s2.print_Id()           # my id: 2  , all students: 2

s1.print_Id()           # my id: 1  , all students: 2
