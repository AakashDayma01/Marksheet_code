class Marksheet:
	import random

	# Generating Random Scholar number
	scholar_number = random.randrange(1111111, 9999999)

	# String with scholar number and state board name correctly formatted
	state_board = f"{'S. No.':>50} {scholar_number:<30}CENTRAL BOARD OF SECONDARY EDUCATION"

	# String with Exam Type 
	exam_type = f"{'ALL INDIA':>82} {'SENIOR SCHOOL CERTIFICATE EXAMINATION,2026'} {'SCH-' + str(random.randrange(111111111, 999999999)) :>30} "

	# String with School name
	school_name = f"{'Govt. Model Higher Secondary School Manasa (M. P.)':>125} "

	# Authenticate marks of subjects that does not have any practical Exams
	def auth_only_theory_sub(self, marks, subject):
		if marks <= 100 and marks >= 0:
			return marks
		else:
			print(f"Marks of {subject} must be less than equal to 100")
			maths = self.auth_only_theory_sub(int(input(f"Enter marks for subject {subject}:  ")), subject)

	# Authenticate marks of Practical subjects
	def auth_practical_subject(self, marks, subject):
		if marks <= 20 and marks >= 0:
			return marks
		else:
			print(f"Marks of {subject} must be less than equal to 20")
			marks = self.auth_practical_subject(int(input(f"Enter marks for subject {subject}: ")), subject)

	# Authenticate marks of subjects that also have practical Exams
	def auth_sub_with_pr(self, marks, subject):
		if marks <= 80 and marks >= 0:
			return marks
		else:
			print(f" Marks of {subject} must be less than equal to 80")
			self.marks = self.auth_sub_with_pr(int(input(f"Enter marks for subject {subject}: ")),subject)

	# Authenticate Roll Number
	def auth_roll_num(self, r_number):
		if r_number.isnumeric() and len(r_number) == 7:
			return r_number
		else:
			print("Enter a valid Roll Number")
			r_number = self.auth_roll_num(input("Enter Roll Number: "))

	# Constructor method 	
	def __init__(self):	
		# User Name
		self.name = input("Enter Name: ")
		self.roll_number = self.auth_roll_num(input("Enter roll number: "))

		# Only THeory Subjects	
		self.physics = self.auth_sub_with_pr(int(input("Enter marks for subject Physics: ")),subject = "Physics")
		self.chemistry = self.auth_sub_with_pr(int(input("Enter marks for subject Chemistry: ")), subject = "Chemistry")

		# Theory Subject That Have Practical Exams
		self.maths = self.auth_only_theory_sub(int(input("Enter marks for subject Maths:  ")), subject = "Maths")
		self.hindi = self.auth_only_theory_sub(int(input("Enter marks for subject Hindi: ")), subject = "Hindi")
		self.english = self.auth_only_theory_sub(int(input("Enter marks for subject English: ")), subject = "English")

		# Practical Subjects
		self.physics_pr = self.auth_practical_subject(int(input("Enter marks for subject Physics Practical: ")), subject = "Physics Practical")
		self.chemistry_pr = self.auth_practical_subject(int(input("Enter marks for subject Chemistry Practical: ")), subject = "Chemistry Practical")


	def markshit_top_content(self):
		self.name_string = f"{'Name:':>49} {self.name:<85} Roll Number: {self.roll_number}"
		print("-"*189 + "\n")
		print(self.state_board)
		print(self.exam_type)
		print(self.school_name)
		#print(self.name_string)
		print(f"{ '-'*113:>157}")

		# Printing Headings
		print(f"{'|':>45}" , f"{"|":>6}" , f"{'|':>34}" , end = " ")
		print( f"{'MARKS OBTAINED':^67}" , f"{'|'}")
		print(f"{'|':>45}" , f"{'|':>6}" , f"{'|':>34}" , f"{'-' * 67}" , "|")

		print(f"{'| CODE |':>52}" , f"{"SUBJECT":^32}","|" , f"{'TH':^8}","|" , f"{'PR':^8}",end = " ")
		print("|" , f"{'TOTAL':^8}" , "|" , f"{'TOTAL IN WORDS':^8}" , "|" , f"{'POSITIONAL GRADE':^8} ", "|")

		print(f"{'|':>45}" , f"{"|":>6}" , f"{'|':>34}" , f"{'|':>10}",end = " ")
		print(f"{'|':>10}" , f"{'|':>10}" , f"{'|':>16} ", f"{'|':>18}")
		print(f"{ '-'*113:>157}")

		# Printing Subjects with marks



		
m1 = Marksheet()
m1.markshit_top_content()

