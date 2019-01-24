''' Assignment: Administration
    Created on 7 jan 2019
    @author: Millen Mortier'''

INPUT_FILE = "administration_input.txt"
SS_PREFIX = "\t"

# This function takes a string of grades seperated by spaces and return the
# average of grades as a string, since one of the posential return values is 
# '6-'
def get_grades_average(grades) :
    total = 0
    for grade in grades:
        total += float(grade)
    average = total / len(grades)
    if average >= 5.5 and average < 6 :
        return "6-"
    return "%0.1f" % (round(average * 2) / 2)

# This function takes a string of the format:
#   [Student name][a number of underscores][grades]
# and prints the student name along with the average grade
def calculate_student_final_grade(line) :
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades_str = split_line[list_len - 1]
    grades_list = grades_str.split()
    average = get_grades_average(grades_list)
    print "%s has an average of %s" % (student_name, average)

# This function takes a string of the format "X=X=X...", where X is an integer
# and print the similarity_scores_graph
def print_similarity_scores_graph(similarity_scores_string) :
    similarity_scores = similarity_scores_string.split("=")
    graph = ""
    for sim_score in similarity_scores :
        sim_score_int = int(sim_score)
        if sim_score_int == 0 :
            graph += "_"
        elif sim_score_int < 20:
            graph += "-"
        else :
            graph += "^"
    print "%s%s" % (SS_PREFIX, graph)

# This function takes a string of the format "name,name,name...", where the
# number of names might be 0 (student_names == "").
def print_student_names(student_names) :
    if student_names == "" :
        print "%sNo matches found" % SS_PREFIX
    else :
        student_names_list = student_names.split(",")
        for student_name in student_names_list :
            print "%s%s" % (SS_PREFIX, student_name.rstrip())


# This function takes a string of the format:
#   [similarity_scores];[optional list of student names]
# and processes it accordingly
def process_similarity_scores(line) :
    split_line = line.split(";")
    similarity_scores = split_line[0]
    student_names = split_line[1]
    print_similarity_scores_graph(similarity_scores)
    print_student_names(student_names)
    

''' Start Program '''
input = open(INPUT_FILE).readlines()
for i in range(0, len(input), 2) :
    first_line = input[i]
    second_line = input[i + 1]
    calculate_student_final_grade(first_line)
    process_similarity_scores(second_line)