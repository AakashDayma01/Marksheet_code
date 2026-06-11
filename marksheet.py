class Marksheet:
	import random

	state_board = "CENTRAL BOARD OF SECONDARY EDUCATION"
	exam_type = f"{'ALL INDIA':<5} SENIOR SCHOOL CERTIFICATE EXAMINATION,2026 {str(random.randrange(0,10),'B',random.randrange(111111111,999999999))}"
	print(exam_type)
	school_name = "Govt. Model Higher Secondary School Manasa (M. P.)"
	scholar_number = random.randrange(1111111, 9999999)
	def __init__(self):
		self.name = input("Enter Name: ")
		self.maths = input("Enter marks for subject Maths: ")
		self.physics = input("Enter marks for subject Physics: ")
		self.chemistry = input("Enter marks for subject Chemistry: ")
		self.hindi = input("Enter marks for subject Hindi: ")
		self.english = input("Enter marks for subject English")



		
m1 = Marksheet()
