courses = {
"CS101": ("Intro to Computer Science", "Dr. Smith", 30, set()),
"MATH203": ("Calculus II", "Dr. Johnson", 25, set()),
"PHY150": ("General Physics", "Dr. Clark", 20, set()),
"ENG102": ("English Composition", "Dr. Taylor", 40, set()),
"BIO110": ("Introduction to Biology", "Dr. Lee", 35, set())
}

registered_courses = []

while True:
    print("Welcome to the Course Registration System!")
    print("1. View all courses")
    print("2. Register for a course")
    print("3. Drop a course")
    print("4. View my courses")
    print("5. Exit")
    selection = int(input())

    match selection:
        case 1: # view all courses
            for course in courses:
                print(f"Course Code: {course}")
                print(f"Title: {courses[course][0]}")
                print(f"Instructor: {courses[course][1]}")
                print(f"Capacity: {courses[course][2]}")
                print(f"Enrolled: {len(courses[course][3])}\n")
        case 2: # register for a course
            course_code = input("Enter course code: ")
            if course_code not in courses:
                print(f"There is no courses with the code {course_code}.\n")
                continue
            if len(courses[course_code][3]) >= courses[course_code][2]:
                print(f"This course is currently full.\n")
                continue
            if course_code in registered_courses:
                print(f"You are already registered for this course.\n")
                continue
            courses[course_code][3].add("Student")
            registered_courses.append(course_code)
            print(f"Successfully registered for {course_code}.\n")
        case 3: # drop a course
            course_code = input("Enter course code: ")
            if course_code in registered_courses:
                registered_courses.remove(course_code)
                print(f"Successfully dropped {course_code}.\n")
            else:
                print(f"You are not registered for {course_code}.\n")
        case 4: # view my courses
            if len(registered_courses) == 0:
                print("You are not registered for any courses.\n")
            else:
                print("You are registered for the following courses:")
                for course in registered_courses:
                    print(f"- {course}: {courses[course][0]}.")
                print() # new line
        case 5: # exit
            print("Thank you for using the Course Registration System. Goodbye!")
            break
        case _: # default case
            print("Invalid input, try again.")