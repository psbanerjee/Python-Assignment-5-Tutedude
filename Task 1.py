try:
    marks = {"Alice" : 85, "Bob" : 81, "Student" :81}   #creates the dictionary containing marks of every student
    stud = input("Enter the student's name: ")          #Takes the name of the student
    smarks = marks[stud]                                #Finds his/her marks
    print("{}'s marks: {}".format(stud,smarks))   #Prints formatted output
except:
    print("Student not found.")                         #Handles error gracefully