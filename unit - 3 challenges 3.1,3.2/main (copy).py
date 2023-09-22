#linearsearch products
class student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students_list):
# sort the list of students in decending order of CGPA
sorted_students = sorted(student_list, key=lambda student :student.cgpa,reverse=True)
return sorted_students
#Example usage
student = [
    student("sameera","A123",6.8),student("ashefa","A124",7.9),student("foujiya","A125",9.0),
]
sorted_students = sort_students(student)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
                      
                            