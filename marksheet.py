class Marksheet:
	import random

	# Generating Random Scholar number
	scholar_number = random.randrange(1111111, 9999999)

	# String with scholar number and state board name correctly formatted
	state_board = f"S. No. {scholar_number:<30}CENTRAL BOARD OF SECONDARY EDUCATION"

	# String with Exam Type 
	exam_type = f"{'ALL INDIA':>30} {"SENIOR SCHOOL CERTIFICATE EXAMINATION,2026":^50} {"SCH-" + str(random.randrange(111111111, 999999999))} "

	# String with School name
	school_name = "Govt. Model Higher Secondary School Manasa (M. P.)"

	# Authenticate marks of subjects that does not have any practical Exams
	def auth_only_theory_sub(self, marks, subject):
		if marks <= 100:
			return marks
		else:
			print(f"Marks of {subject} must be less than equal to 100")
			maths = self.auth_only_theory_sub(int(input(f"Enter marks for subject {subject}:  ")), subject)

	# Authenticate marks of Practical subjects
	def auth_practical_subject(self, marks, subject):
		if marks <= 20:
			return marks
		else:
			print(f"Marks of {subject} must be less than equal to 20")
			marks = self.auth_practical_subject(int(input("Enter marks for subject Physics Practical")), subject)

	# Authenticate marks of subjects that also have practical Exams
	def auth_sub_with_pr(self, marks, subject):
		if marks <= 80:
			return marks
		else:
			print(f" Marks of {subject} must be less than equal to 80")
			self.marks = self.auth_sub_with_pr(int(input(f"Enter marks for subject {subject}: ")),subject)

	# Constructor method 	
	def __init__(self):	
		# User Name
		self.name = input("Enter Name: ")

		# Only THeory Subjects	
		self.physics = self.auth_sub_with_pr(int(input("Enter marks for subject Physics: ")),subject = "Physics")
		self.chemistry = self.auth_sub_with_pr(int(input("Enter marks for subject Chemistry: ")), subject = "Chemistry")

		# Theory Subject That Have Practical Exams
		self.maths = self.auth_only_theory_sub(int(input("Enter marks for subject Maths:  ")), subject = "Maths")
		self.hindi = self.auth_only_theory_sub(int(input("Enter marks for subject Hindi: ")), subject = "Hindi")
		self.english = self.auth_only_theory_sub(int(input("Enter marks for subject English")), subject = "English")

		# Practical Subjects
		self.physics_pr = self.auth_practical_subject(int(input("Enter marks for subject Physics Practical")), subject = "Physics Practical")
		self.chemistry_pr = self.auth_practical_subject(int(input("Enter marks for subject Chemistry Practical")), subject = "Chemistry Practical")



		
m1 = Marksheet()
