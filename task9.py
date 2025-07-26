student_details={
    "Alice": 85,
    "Parvesh": 95,
    "Lokesh" : 75,
    "Ravi": 35,
}
try:
    stud_name=input("Enter the student's name: ")
    print(stud_name+"'s marks: ",student_details[stud_name])
except Exception:
    print("Student not found")