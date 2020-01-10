from functools import reduce
def students_list(students,courses, scores):
  student_total_score = []
    # RANGE
  for i in range(len(scores)):
    # REDUCE AND LAMBDA
    total_score = reduce((lambda score1, score2: score1 + score2), scores[i])
    student_total_score.append(total_score)
  
    # MAP
  gpa = map((lambda score: score/(len(courses) * 10)), student_total_score)

  gpa_list = list(gpa)



  # ENUMERATE
  student_class = []
  for index, value in enumerate(gpa_list):
    if value >= 7:
      grade = 'First class'
    elif value >= 5:
      grade = 'Second class'
    else:
      grade = 'Third class'
    student_class.append(grade)

  # FILTER
  # first_class = filter(lambda el: (el[1] >= 7),student_class.items())

# ZIP
  students_details = zip(students, gpa_list, student_class)
  return list(students_details)


# SECOND FUNCTION implementing FILTER
def first_class(gpa):
  first_class = filter(lambda el: (el >= 7), gpa)
  number_of_firstclass = (len(list(first_class)))
  return "There are %s first class students." % number_of_firstclass
  

students = ['Tol', 'Teg', 'AFat', 'Jon', 'Say', 'Tal' 'Akm', 'Fath', 'Lee', 'Chris']
courses = ('Py', 'Js', 'Html', 'Css')
scores = [
    (67, 34, 78, 54),
    (88, 54, 90, 43),
    (34, 67, 23, 56),
    (90, 98, 76, 88),
    (43, 45, 65, 43),
    (88, 76, 45, 67),
    (56, 76, 77, 45),
    (67, 78, 98, 90),
    (23, 35, 22, 30),
    (45, 65, 67, 78)
]
print(students_list(students, courses, scores))
print(first_class([1,2,5,8,9,6,5,4,3,2]))