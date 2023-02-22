#Create student mark management system without classes or objects

#Student Info: 
def student_number():
    input_Number_Of_Students = int(input("Enter the number of students: "))
    return input_Number_Of_Students
def Student():
    Num_Of_Students = [0, student_number()]
    for i in Num_Of_Students:
        print("Enter the student info: ")
        Student_ID = input("Enter the student ID: ")
        Student_Name = input("Enter the student name: ")
        Student_DoB = input("Enter the student Date of Birth: ")
        Student_Info = dict(ID = Student_ID, Name = Student_Name, Date_of_Birth = Student_DoB)
        print("\n")
        Student_Info.update()

#Course Info:
def course_number():
    input_Number_Of_Courses = int(input("Enter the number of courses: "))
    return input_Number_Of_Courses
def Course():
    Num_Of_Courses = [0, course_number()]
    for c in Num_Of_Courses:
        print("Enter the course info: ")
        Course_ID = input("Enter the course ID: ")
        Course_Name = input("Enter the course name: ")
        Course_Info = dict(ID = Course_ID, Name = Course_Name)
        print("\n")
        Course_Info.update()

#Input the student mark in a course based on the course id
def input_mark():
    input_Course_ID = input("Enter the course ID: ")
    input_Student_ID = input("Enter the student ID: ")
    input_Mark = input("Enter the mark: ")
    Mark_Info = dict(ID = input_Course_ID, Student_ID = input_Student_ID, Mark = input_Mark)
    print("\n")
    Mark_Info.update()

#Display a list of students
def list_students(student):
    student = [0, student_number()]
    if len(student) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for i in range (len(student)):
            print(f"{i+1}. {student[i]['ID']} - {student[i]['Name']} - {student[i]['Date_of_Birth']}")
            if "marks" in student[i]:
                print("Marks (Course Id - Mark): ", end="")
                for course in student[i]["marks"]:
                    print(f"{course} - {student[i]['marks'][course]}", end=", ")
                print()

#Display a list of courses
def list_courses(course):
    if len(course) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for i, course in enumerate(course):
            print(f"{i+1}. {course['ID']} - {course['Name']}")
            
#Ask the user to enter an integer to select an option
def select(option_range, input_message="Choose an option: "):
    selection = input(input_message)
    if not selection.isnumeric():
        return -1
    selection = int(selection)
    if selection not in option_range:
        return -1
    return selection

#Pause the program
def pause():
    input("Press Enter to continue...")
#Main function
def main():
    #Initialize the list
    course = []
    student = []
    Num_Of_Students = 0
    Num_Of_Courses = 0

    while(True):
        print("""
Welcome to the student managament system! Please choose an option as below:
    0. Exit
    1. Input number of students
    2. Input students information (ID, name, DoB)
    3. Input number of courses 
    4. Input courses information (ID, name)
    5. Input marks for student in a course
    6. List courses
    7. List students""") 
        selection = select(range(0, 8))                                                                 
        if selection == 0:
            break
        elif selection == 1:
            student_number()
            pause()
            continue
        elif selection == 2:
            Student()
            pause()
            continue
        elif selection == 3:
            course_number()
            pause()
            continue
        elif selection == 4:
            Course() 
            pause()
            continue                                                   
        elif selection == 5:
            input_mark()
            pause()
            continue
        elif selection == 6: 
            list_courses()
            pause()
            continue
        elif selection == 7:
            list_students()
            pause()
            continue                                                                          
        else:
            print("Invalid input. Please try again!")
        pause()
        continue 
        
# Call the main function
if __name__ == "__main__":
    main()

