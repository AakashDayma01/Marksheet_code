import random
import inflect
class Marksheet:

	# Generating Random Scholar number
	scholar_number = random.randrange(1111111, 9999999)

	# String with scholar number and state board name correctly formatted
	state_board = f"{'|':>11}{'S. No.':>9} {scholar_number:<32}{'CENTRAL BOARD OF SECONDARY EDUCATION'} {'|':>40}"

	# String with Exam Type 
	exam_type = f"{'|':>11}{'ALL INDIA':>43} {'SENIOR SCHOOL CERTIFICATE EXAMINATION,2026'} {'SCH-' + str(random.randrange(111111111, 999999999)) :>28} {'|':>3}"

	# String with School name

	# List Of Failed Subjects

	failed_subjects = []
	Absent_subject = 0

	# Authenticate marks of subjects that does not have any practical Exams
	def auth_only_theory_sub(self, marks, subject):
		if str(marks).lower() == "ab":
			self.Absent_subject += 1
			self.failed_subjects.append(subject)
			return "AB"
		elif str(marks).isnumeric() and int(marks) <= 100 and int(marks) >= 0:
			return int(marks)
		else:
			return self.auth_only_theory_sub(input(f"Marks of {subject} must be less than equal to 100:  "), subject)

	# Authenticate marks of Practical subjects
	def auth_practical_subject(self, marks, subject):
		if not(str(marks).isnumeric()):
			return self.auth_practical_subject(input(f"Enter valid marks for subject {subject}: "), subject)	
		elif str(marks).isnumeric() and (int(marks) <= 20 and int(marks) >= 0):
			return (marks := int(marks))
		else:
			return self.auth_practical_subject(input(f"Marks of {subject} must be less than equal to 20: "), subject)

	# Authenticate marks of subjects that also have practical Exams
	def auth_sub_with_pr(self, marks, subject):
		if str(marks).lower() == "ab":
			self.Absent_subject += 1
			self.failed_subjects.append(subject)
			return "AB"
		elif not(str(marks).isnumeric()):
			return self.auth_sub_with_pr(input(f"Enter valid marks for subject {subject}: "),subject)	

		marks = int(marks)		
		if str(marks).isnumeric() and (int(marks)) <= 80 and int(marks) >= 0:
			return (marks := int(marks))
		else:
			return self.auth_sub_with_pr(input(f"Marks of {subject} must be less than equal to 80: "),subject)

	# Authenticate Roll Number
	def auth_roll_num(self, r_number):
		if r_number.isnumeric() and len(r_number) == 7:
			return r_number
		else:
			if len(r_number) != 7:
				return self.auth_roll_num(input("Length of roll number must be 7: "))
			else:
				return self.auth_roll_num(input("Please enter only numbers don't use special letters and spellings: "))


	# Check whether any sumbers present in the name or not
	def check_name(self, name):
		special_letters = ('#', "@", "!", "_", "$", "%", "&", "," "^", "*", "(", ")", "{" , "}", "\\" , "|", "?", ":", ";", ">", "<", "/")
		for index, letter in enumerate(special_letters):
			if (str(index) in name) or (letter in name):
				return self.check_name(input("Please don't use special characters and numbers in name: "))
		else:
			return name

	# Constructor method 	
	def __init__(self):	
		# User Name
		self.name = self.check_name(input("Enter Name: "))
		self.roll_number = self.auth_roll_num(input("Enter roll number: "))
		self.school_name = self.check_name(input("Enter school name: "))
		self.father_name = self.check_name(input("Enter father name: "))
		self.mother_name = self.check_name(input("Enter mother name:"))

		# Only THeory Subjects	
		self.physics = self.auth_sub_with_pr(input("Enter marks for subject Physics Enter 'AB' if Absent: "),subject = "Physics")
		self.chemistry = self.auth_sub_with_pr(input("Enter marks for subject Chemistry Enter \"AB\" id Absent: "), subject = "Chemistry")

		# Theory Subject That Have Practical Exams
		self.maths = self.auth_only_theory_sub(input("Enter marks for subject Maths Enter \"AB\" if Absent:  "), subject = "Maths")
		self.hindi = self.auth_only_theory_sub(input("Enter marks for subject Hindi Enter \"AB\" if Absent: "), subject = "Hindi")
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
		self.name_string = f"{'|':>11}{'Name:':>8} {self.name:<85} Roll Number: {self.roll_number} {'|':>3}"
		print("-"*150 + "\n")
		print(f"{ '-'*120:>130}")
		print(self.state_board)
		print(self.exam_type)
		self.school_name = f"{'| ':>12} {self.school_name:^116}|"
		print(self.school_name)
		print(f"{'|':>11}{'|':>119}")
		print(f"{'|':>11}{'|':>119}")
		print(self.name_string)
		print(f"{'|':>11}{'Father name: ':>16}{self.father_name:<85}{'|':>18}")
		print(f"{'|':>11}{'Mother name: ':>16}{self.mother_name:<85}{'|':>18}")
		print(f"{'|':>11}{ '-'*113:>116}{'|':>3}")

		# Printing Headings
		print(f"{'|':>11}{'|':>4}" , f"{"|":>6}" , f"{'|':>34}" , end = " ")
		print( f"{'MARKS OBTAINED':^67}" , f"{'|'} {'|':>2}")
		print(f"{'|':>11}{'|':>4}" , f"{'|':>6}" , f"{'|':>34}" , f"{'-' * 67}" , "|",f"{'|':>2}")

		print(f"{'|':>11}{'| CODE |':>11}" , f"{"SUBJECT":^32}","|" , f"{'TH':^8}","|" , f"{'PR':^8}",end = " ")
		print("|" , f"{'TOTAL':^8}" , "|" , f"{'TOTAL IN WORDS':^8}" , "|" , f"{'POSITIONAL GRADE':^8} ", "|",f"{'|':>2}")

		print(f"{'|':>11}{'|':>4}" , f"{"|":>6}" , f"{'|':>34}" , f"{'|':>10}",end = " ")
		print(f"{'|':>10}" , f"{'|':>10}" , f"{'|':>16} ", f"{'|':>18}{'|':>3}")
		print(f"{'|':>11}{ '-'*113:>116}{'|':>3}")


		# Printing Subjects with marks
		p = inflect.engine()
		
		# For Subjct Maths
		print(f"{'|':>11}{'|':>4}",f"{'041 |':^8}",f"{"MATHEMATICS":^30}","|",f"{str(self.maths):^8}","|",f"{'XX':^8}","|",f"{str(self.maths):^8}","|" ,end ="")
		print(f"{(str(p.number_to_words(self.maths)).upper()):^15}" , "|" , f"{str(self.gen_only_th_grade(self.maths, "Mathematics")):^17}" , "|",f"{'|':>2}")

		# For Subject Physics
		self.physics_total = (self.physics + self.physics_pr) if(str(self.physics).lower()!="ab") else self.physics_pr
		print(f"{'|':>11}{'|':>4}",f"{'042 |':^8}",f"{"PHYSICS":^30}","|",f"{str(self.physics):^8}","|",f"{str(self.physics_pr):^8}","|",f"{str(self.physics_total):^8}","|" ,end ="")
		print(f"{(str(p.number_to_words(self.physics_total)).upper()):^15}","|", f"{self.gen_only_th_grade(self.physics_total,"Physics"):^17}","|",f"{'|':>2}")

		# For Subject Chemistry
		self.chemistry_total = (self.chemistry + self.chemistry_pr) if(str(self.chemistry).lower()!="ab") else self.chemistry_pr 
		print(f"{'|':>11}{'|':>4}",f"{'043 |':^8}",f"{"CHEMISTRY":^30}","|",f"{str(self.chemistry):^8}","|",f"{str(self.chemistry_pr):^8}","|",f"{str(self.chemistry_total):^8}","|",end ="")
		print(f"{(str(p.number_to_words(self.chemistry_total)).upper()):^15}","|",f"{self.gen_only_th_grade(self.chemistry_total,"Chemistry"):^17}","|",f"{'|':>2}")

		# For Subject English
		print(f"{'|':>11}{'|':>4}",f"{'301 |':^8}",f"{"ENGLISH":^30}","|",f"{self.english:^8}","|",f"{'XX':^8}","|",f"{self.english:^8}","|" ,end ="")
		print(f"{(str(p.number_to_words(self.english)).upper()):^15}","|",f"{self.gen_only_th_grade(self.english, "English"):^17}","|",f"{'|':>2}")

		# For Subject Hindi
		print(f"{'|':>11}{'|':>4}" , f"{'302 |':^8}" , f"{"HINDI":^30}" , "|" , f"{self.hindi:^8}" , "|" , f"{'XX':^8}" , "|" , f"{self.hindi:^8}" , "|" ,end ="")
		print(f"{(str(p.number_to_words(self.hindi)).upper()):^15}" , "|" , f"{self.gen_only_th_grade(self.hindi, "Hindi"):^17}" , "|",f"{'|':>2}")

		print(f"{'|':>11}{ '-'*113:>116}{'|':>3}")
		print(f"{'|':>11}{'|':>119}")
		print(f"{'|':>11}{'|':>119}")


		# PRinting Result
		print(f"{'|':>11}{'RESULT: ':>59}", f"{'PASS' if len(self.failed_subjects)<=2 else "FAIL"}{'|':>55}")
		print(f"{'|':>11}{'|':>119}")
		print(f"{'|':>11}{'|':>119}")
		print(f"{'|':>11}{ '-'*118:>112}{'|'}")

		print(f"{'|':>11}{'|':>119}")
		print(f"{'|':>11}{'Abbriviations':>16}{'|':>103}")
		print(f"{'|':>11}{'AB: Absent in the Subject: ':>30}", f"{self.Absent_subject}{'|':>87}")
		print(f"{'|':>11}{'FT: Fail in Theory Subject':>29}" , f"{len(self.failed_subjects)}{'|':>88}")


		self.failed_sub = ""
		if len(self.failed_subjects) <=2:
			if len(self.failed_subjects) == 1:
				self.failed_sub = f" \"{self.failed_subjects[0]}\""
			elif len(self.failed_subjects) == 2:
				self.failed_sub= f" \"{self.failed_subjects[0]}\""
				self.failed_sub += f" , \" {self.failed_subjects[1]}\""
		print(f"{'|':>11}{'*: Appeared in compartmental examination: ':>45}" , f"{self.failed_sub if self.failed_sub else " 0 " + ' ':<71} |")
		print(f"{'|':>11}{'|':>119}")

		print(f"{'|':>11}{ '-'*118:>112}{'|'}")

		
m1 = Marksheet()
m1.markshit_top_content()

