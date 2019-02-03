''' Assignment: Geography Grades 1
    Created on whenever
    @author: Whoever'''

def get_grades_average(grades):
    grade1 = float(grades[0])
    grade2 = float(grades[1])
    grade3 = float(grades[2])
    return (grade1 + grade2 + grade3) / 3

def process_input_line(line):
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades = split_line[list_len - 1]
    split_grades = grades.split() 
    average = get_grades_average(split_grades)
    print "%s has an average grade of %0.1f" % (student_name, average)

def print_report():
    lines = open('input.txt').readlines()
    for line in lines:
        process_input_line(line)

'''Start Program'''
print "Report for group 2b"
print_report()  # this function is going to take care of printing the actual report
print "End of report"