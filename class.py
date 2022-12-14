from dataclasses import dataclass
@dataclass
class Student:
    s_id :int
    name : str
    age : int
    s_dep : str
    def __repr__(self):
        return f"Student id is{self.s_id}\nStudent name is{self.name}\nStudent age is{self.age}\n"

@dataclass
class Department:
    d_id : int
    d_name : str
    s_id : int
    def __repr__(self):
        return f"Department name is{self.d_name}\nDepartment id is{self.d_id}\nStuddent id is{self.s_id}\n"

def inner_join(student,department):
    result = []
    for s in student:
        for d in department:
            if s.s_id == d.s_id:
                result.append((s.s_id,s.name,d.d_name))
    return result


s1 = Student(1,"Ayushi",19,"CSE")
s2 = Student(2,"Sam",20,"ECE")
s3 = Student(3,"Manish",21,"EE")
s4 = Student(4,"Hema",18,"CE")

students =[s1,s2,s3,s4]

d1 = Department(10,"CSE",1)
d2 = Department(11,"ECE",2)
d3 = Department(12,"CE",4)
d4 = Department(13,"EE",3)

departments = [d1,d2,d3,d4]

print(inner_join(students,departments))



