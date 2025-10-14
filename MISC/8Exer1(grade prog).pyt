student_scores = {
  "Josh": 87,
  "Levin": 92,
  "Lopez": 81, 
}

student_grades = {}


for students in student_scores: 
  score = student_scores[students]
  if score > 90: 
    print("A")
  elif score >=81: 
    print("B")
  elif score <= 80: 
    print("C")
