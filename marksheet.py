import random
import inflect
class Marksheet:

	# Generating Random Scholar number
	scholar_number = random.randrange(1111111, 9999999)

	# String with scholar number and state board name correctly formatted
	state_board = f"{'S. No.':>20} {scholar_number:<30}CENTRAL BOARD OF SECONDARY EDUCATION"

	# String with Exam Type 
	exam_type = f"{'ALL INDIA':>52} {'SENIOR SCHOOL CERTIFICATE EXAMINATION,2026'} {'SCH-' + str(random.randrange(111111111, 999999999)) :>30} "

	# String with School name
	school_name = f"{'Govt. Model Higher Secondary School Manasa (M. P.)':>95} "


	# List Of Failed Subjects

	failed_subjects = []
	Absent_subject = 0

	# Authenticate marks of subjects that does not have any practical Exams
	def auth_only_theory_sub(self, marks, subject):
		if str(marks).lower() == "ab":
			self.Absent_subject += 1
			self.failed_subjects.append(subject)
			return "AB"
		elif not(str(marks).isnumeric()) or str(marks).isalpha():
			maths = self.auth_only_theory_sub(input(f"Enter valid Marks for subject {subject}:  "), subject)
		elif int(marks) <= 100 and int(marks) >= 0:
			return int(marks)
		else:
			print(f"Marks of {subject} must be less than equal to 100")
			maths = self.auth_only_theory_sub(input(f"Enter marks for subject {subject}:  "), subject)

	# Authenticate marks of Practical subjects
	def auth_practical_subject(self, marks, subject):
		if not(str(marks).isnumeric()) or str(marks).isalpha():
			print(f"Enter valid marks for subject {subject}")
			marks = self.auth_practical_subject(input(f"Enter marks for subject {subject}: "), subject)	
		if str(marks).isnumeric() or (int(marks) <= 20 and int(marks) >= 0):
			return int(marks)
		else:
			print(f"Marks of {subject} must be less than equal to 20")
			marks = self.auth_practical_subject(input(f"Enter marks for subject {subject}: "), subject)

	# Authenticate marks of subjects that also have practical Exams
	def auth_sub_with_pr(self, marks, subject):
		if str(marks).lower() == "ab":
			self.Absent_subject += 1
			self.failed_subjects.append(subject)
			return "AB"
		elif not(str(marks).isnumeric()) or str(marks).isalpha():
			marks = self.auth_sub_with_pr(input(f"Enter valid marks for subject {subject}: "),subject)			
		elif (marks := int(marks)) <= 80 and int(marks) >= 0:
			print(type(marks), marks)
			return int(marks)
		else:
			print(f" Marks of {subject} must be less than equal to 80")
			marks = self.auth_sub_with_pr(input(f"Enter marks for subject {subject}: "),subject)

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
		self.physics = self.auth_sub_with_pr(input("Enter marks for subject Physics Enter \"AB\" id Absent: "),subject = "Physics")
		self.chemistry = self.auth_sub_with_pr(input("Enter marks for subject Chemistry Enter \"AB\" id Absent: "), subject = "Chemistry")

		# Theory Subject That Have Practical Exams
		self.maths = self.auth_only_theory_sub(input("Enter marks for subject Maths Enter \"AB\" id Absent:  "), subject = "Maths")
		self.hindi = self.auth_only_theory_sub(input("Enter marks for subject Hindi Enter \"AB\" id Absent: "), subject = "Hindi")
		self.english = self.auth_only_theory_sub(input("Enter marks for subject English Enter \"AB\" id Absent: "), subject = "English")

		# Practical Subjects
		self.physics_pr = self.auth_practical_subject(input("Enter marks for subject Physics Practical: "), subject = "Physics Practical")
		self.chemistry_pr = self.auth_practical_subject(input("Enter marks for subject Chemistry Practical: "), subject = "Chemistry Practical")

	# Generating Grades of Subjects that does not hve practical exams
	def gen_only_th_grade(self, marks , subject):
		if not(str(marks).isnumeric()):
			if str(marks).lower() == "ab":
				return "AB"
		elif int(marks) >= 90:
			return "A+"
		elif int(marks) >=80 and int(marks) <= 90:
			return "A"
		elif int(marks) <= 80 and int(marks) >= 70:
			return "B+"
		elif int(marks) <= 70 and int(marks) >= 50:
			return "B"
		elif int(marks) <=50 and int(marks) >= 33:
			return "C"
		else:
			if subject not in self.failed_subjects:
				self.failed_subjects.append(subject)
			return "D"


	def markshit_top_content(self):
		self.name_string = f"{'Name:':>19} {self.name:<85} Roll Number: {self.roll_number}"
		print("-"*150 + "\n")
		print(f"{ '-'*113:>127}")
		print(self.state_board)
		print(self.exam_type)
		print(self.school_name, "\n\n")
		print(self.name_string)
		print(f"{ '-'*113:>127}")

		# Printing Headings
		print(f"{'|':>15}" , f"{"|":>6}" , f"{'|':>34}" , end = " ")
		print( f"{'MARKS OBTAINED':^67}" , f"{'|'}")
		print(f"{'|':>15}" , f"{'|':>6}" , f"{'|':>34}" , f"{'-' * 67}" , "|")

		print(f"{'| CODE |':>22}" , f"{"SUBJECT":^32}","|" , f"{'TH':^8}","|" , f"{'PR':^8}",end = " ")
		print("|" , f"{'TOTAL':^8}" , "|" , f"{'TOTAL IN WORDS':^8}" , "|" , f"{'POSITIONAL GRADE':^8} ", "|")

		print(f"{'|':>15}" , f"{"|":>6}" , f"{'|':>34}" , f"{'|':>10}",end = " ")
		print(f"{'|':>10}" , f"{'|':>10}" , f"{'|':>16} ", f"{'|':>18}")
		print(f"{ '-'*113:>127}")


		# Printing Subjects with marks
		p = inflect.engine()
		
		# For Subjct Maths
		print(f"{'|':>15}",f"{'041 |':^8}",f"{"MATHEMATICS":^30}","|",f"{str(self.maths):^8}","|",f"{'XX':^8}","|",f"{str(self.maths):^8}","|" ,end ="")
		print(f"{(str(p.number_to_words(89)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(self.maths, "Mathematics"):^17}" , "|")

		# For Subject Physics
		print(type(self.physics_pr), self.physics_pr)
		print(type(self.physics), self.physics)
		self.physics_total = (self.physics + self.physics_pr) if(str(self.physics).lower()!="ab") else self.physics_pr
		print(f"{'|':>15}",f"{'042 |':^8}",f"{"PHYSICS":^30}","|",f"{str(self.physics):^8}","|",f"{str(self.physics_pr):^8}","|",f"{str(self.physics_total):^8}","|" ,end ="")
		print(f"{(str(p.number_to_words(self.physics_total)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(self.physics_total, "Physics"):^17}" , "|")

		# For Subject Chemistry
		self.chemistry_total = (self.chemistry + self.chemistry_pr) if(str(self.chemistry).lower()!="ab") else self.chemistry_pr 
		print(f"{'|':>15}",f"{'043 |':^8}",f"{"CHEMISTRY":^30}","|",f"{str(self.chemistry):^8}","|",f"{str(self.chemistry_pr):^8}","|",f"{str(self.chemistry_total):^8}","|",end ="")
		print(f"{(str(p.number_to_words(self.chemistry_total)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(self.chemistry_total, "Chemistry"):^17}" , "|")

		# For Subject English
		print(f"{'|':>15}" , f"{'301 |':^8}" , f"{"ENGLISH":^30}" , "|" , f"{89:^8}" , "|" , f"{'XX':^8}" , "|" , f"{89:^8}" , "|" ,end ="")
		print(f"{(str(p.number_to_words(self.english)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(99, "English"):^17}" , "|")

		# For Subject Hindi
		print(f"{'|':>15}" , f"{'302 |':^8}" , f"{"HINDI":^30}" , "|" , f"{89:^8}" , "|" , f"{'XX':^8}" , "|" , f"{89:^8}" , "|" ,end ="")
		print(f"{(str(p.number_to_words(self.english)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(99, "Hindi"):^17}" , "|")

		print(f"{ '-'*113:>127}" , "\n\n")


		# PRinting Result
		print(f"{'RESULT: ':>70}", f"{'PASS' if len(self.failed_subjects)<=2 else "FAIL"}")

		print(f"{'Abbriviations':>27}")
		print(f"{'AB: Absent in the Subject: ':>41}", f"{self.Absent_subject}")
		print(f"{'FT: Fail in Theory Subject':>40}" , f"{len(self.failed_subjects)}")


		self.failed_sub = ""
		if len(self.failed_subjects) <=2:
			if len(self.failed_subjects) == 1:
				self.failed_sub = f" \"{self.failed_subjects[0]}\""
			elif len(self.failed_subjects) == 2:
				self.failed_sub= f" \"{self.failed_subjects[0]}\""
				self.failed_sub += f" , \" {self.failed_subjects[1]}\""
		print(f"{'*: Appeared in compartmental examination: ':>56}" , f"{self.failed_sub if (self.failed_sub != "") else 0}")
		print("Delhi")

		
m1 = Marksheet()
m1.markshit_top_content()

