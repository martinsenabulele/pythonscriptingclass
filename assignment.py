

class University:
    def __init__(self, students, lecturer, president, classroom,):
        self.students = students
        self.lecturer = lecturer
        self.president = president
        self.classroom = classroom

    def I_am_a_student(self):
        print(" I'm a student of the University of python")
        self.level(final_year)

    def course_teacher(self):
        print("I'm a lecturer at the university of python")


    def university_president(self):
        print("my name is John Paul I'm the president of the university of python")


class CollegeOfScience:
    def __init__(self, Computer_science, Biochemistry, BigData):
        self.Computer_science = Computer_science
        self.Biochemistry = Biochemistry
        self.BigDate = BigData

    def code_Program(self):
        print("I'm a coder with %s flakes" % self.BigDate)

    def drug_chemist(self):
        print("I'm a biochemist")

    def data_ml(self):
        print("I'm a machine learner")




class Falculty(University, CollegeOfScience):
    def __init__(self, head, secretary, clerk, BigData):
        self.head = head
        self.secretary = secretary
        self.clerk = clerk
        self.BigDate = BigData

    def falculty_head(self):
        print("I head this falculty")

    def falculty_secretary(self):
        print("where is the secretary?")

    def falculty_clerk(self):
        print("I'm the clerk")

def f2():
    university_python = Falculty("John", "Peter", "Paul", "ml")
    university_python.falculty_head()
    university_python.falculty_secretary()
    university_python.falculty_clerk()
    university_python.code_Program()
    university_python.course_teacher()


f2()



