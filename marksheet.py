import random
import inflect
from datetime import datetime
import psycopg2
class Marksheet:

	conn = psycopg2.connect(database="result", user="aakash", password="aakash123")
	cursor = conn.cursor()

	# Create Database Table if not exist
	table_auery = """
	CREATE TABLE IF NOT EXISTS marksheet(
		roll_number INT PRIMARY KEY,
		sch_number INT NOT NULL, 
		sch INT NOT NULL,
		school_name VARCHAR(150) NOT NULL,
		name VARCHAR(100) NOT NULL, 
		father_name VARCHAR(100) NOT NULL,
		mother_name VARCHAR(100) NOT NULL,
		dob DATE NOT NULL,
		maths VARCHAR(10) NOT NULL,
		physics VARCHAR(10) NOT NULL,
		chemistry VARCHAR(10) NOT NULL,
		hindi VARCHAR(10) NOT NULL,
		english VARCHAR(10) NOT NULL,
		physics_practical VARCHAR(10) NOT NULL,
		chemistry_practical VARCHAR(10) NOT NULL
	);
	"""
	cursor.execute(table_auery)
	conn.commit()

	def __init__(self):
		self.user_choice = input("""
Enter 1 if you want to add marksheet 
Enter 2 if you want to show marksheeet using roll number 
Enter 3 to delete marksheet using roll number
Enter 4 to update information from existing marksheet using roll number: 
Enter Done if completed everything """)

		if self.user_choice == "1":
			self.add_marksheet()
			select_query =f"""SELECT * FROM marksheet WHERE roll_number = {self.roll_number};"""
			self.cursor.execute(select_query) 
			data = self.cursor.fetchall() 
			self.show_marksheet(self.roll_number)
		elif self.user_choice == "2":
			roll_number = input("Enter Roll number to show marksheet: ")
			self.show_marksheet(roll_number)
		elif self.user_choice == "3":
			roll_number = input("Enter Roll number to delete marksheet: ")
			self.delete_marksheet(roll_number)
		elif self.user_choice == "4":
			roll_number = self.check_roll_num(input("Enter roll number to update marksheet: "))
			self.update_marksheet(roll_number)
		elif self.user_choice.lower() == "done":
			pass
		else:
			print("Invalid choice")
			self.__init__()

	def check_roll_num(self, r_number):
		if r_number.isnumeric() and len(r_number) == 7:
			return r_number
		else:
			if not(r_number.isnumeric()):
				return self.check_roll_num(input("Please enter only numbers don't use special letters and spellings: "))
			elif len(r_number) != 7 :
				return self.check_roll_num(input("Length of roll number must be 7: "))
			else:
				return self.check_roll_num(input("Please reenter Roll number: "))

	def add_marksheet(self):
		add_query = """
		INSERT INTO marksheet(roll_number, sch_number, sch, school_name, name, father_name, mother_name, dob,
			maths, physics, chemistry, hindi, english, physics_practical, chemistry_practical)
		VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
		"""

		self.enter_data()
		values = (self.roll_number, self.scholar_number, self.sch, 
			self.school_name, self.name, self.father_name, 
			self.mother_name, self.dob,self.maths, self.physics, self.chemistry,
			self.hindi, self.english, self.physics_pr, self.chemistry_pr
		)

		self.cursor.execute(add_query, values)
		self.conn.commit() 


	def show_marksheet(self, roll_number):
		select_query =f"""SELECT * FROM marksheet WHERE roll_number = {roll_number};"""
		self.cursor.execute(select_query) 
		data = self.cursor.fetchall()

		if len(data)==0 :
			self.show_marksheet(input("Marksheet for this roll number is not exist please check and re enter roll number: "))
		else:
			data = data[0]
			self.roll_number = str(data[0])
			self.scholar_number = str(data[1]) 
			self.sch = str(data[2]) 
			self.school_name = data[3]
			self.name = data[4] 
			self.father_name = data[5] 
			self.mother_name = data[6]
			self.dob = data[7] 
			self.maths = int(data[8]) if data[8].lower() != "ab" else "AB" 
			self.physics = int(data[9]) if data[9].lower() != "ab" else "AB" 
			self.chemistry = int(data[10]) if data[10].lower() != "ab" else "AB" 
			self.hindi = int(data[11]) if data[11].lower() != "ab" else "AB"  
			self.english = int(data[12]) if data[12].lower() != "ab" else "AB" 
			self.physics_pr = int(data[13]) if data[13].lower() != "ab" else "AB" 
			self.chemistry_pr = int(data[14]) if data[14].lower() != "ab" else "AB" 
			self.markshit_top_content()

	def delete_marksheet(self, roll_number):
		select_query =f"""SELECT * FROM marksheet WHERE roll_number = {roll_number};"""
		self.cursor.execute(select_query) 
		data = self.cursor.fetchall()
		if len(data) != 0 :
			recheck = input("Do you really want to delete the marksheet if yes enter 1 else enter 0: ")
			if int(recheck.lower()):
				delete_query = f"DELETE FROM marksheet WHERE roll_number = {roll_number}"
				self.cursor.execute(delete_query)
				self.conn.commit()
				print("Marksheet Deleted successfully: ")
			else:
				self.__init__()
		else:
			self.delete_marksheet(input("Marksheet for this roll number is not exist please check and Re enter roll number:"))

	def update_marksheet(self, roll_number):
		
		select_query =f"""SELECT * FROM marksheet WHERE roll_number = {roll_number};"""
		self.cursor.execute(select_query) 
		data = self.cursor.fetchall()
		if len(data) !=0:
			data = data[0]
		else:
			print("Marksheet for this roll number is not exisx: ")
			self.update_marksheet(roll_number)

		user_choice = input("What do you want to update personal detailes or marks if personal detailes enter 0 else enter 1: ")
		if int(user_choice) == 0:
			while True:
				choice = input("Enter number to update detailes like  1 for name, 2 for father_name, 3 for mother_name, 4 for date of birth: ")
				if choice == '1':
					name = self.check_name(input(f"Enter name to update your current name present in marksheet is {data[4]}: "))
					update_query = "UPDATE marksheet SET name = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (name, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == '2':
					name = self.check_name(input(f"Enter father name to update current name present in marksheet is {data[5]}: "))
					update_query = "UPDATE marksheet SET father_name = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (name, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == '3':
					name = self.check_name(input(f"Enter mother name to update current name present in marksheet is {data[6]}: "))
					update_query = "UPDATE marksheet SET mother_name = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (name, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == '4':
					dob = self.check_name(input(f"Enter new date of birth to update your current date of birth present in marksheet is {data[7]}: "))
					update_query = "UPDATE marksheet SET dob = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (dob, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				else:
					print("Invalid Choice please re enter: ")
					self.update_marksheet(roll_number)
		elif int(user_choice) == 1:
			while True:
				choice = input("Enter a number betwin 1 to 7 to update marks like Maths, Physics, Chemistry, Hindi, English, Physics Practical, Chemistry Practical: ")
				if choice == "1":
					maths =  self.auth_only_theory_sub(input("Enter marks for subject Maths Enter \"AB\" if Absent to upfdate:  "), subject = "Maths")
					update_query = "UPDATE marksheet SET maths = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (marths, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "2":
					physics = self.auth_sub_with_pr(input("Enter marks for subject Physics Enter 'AB' if Absent to update: "),subject = "Physics")
					update_query = "UPDATE marksheet SET physics = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (physics, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "3":
					chemistry = self.auth_sub_with_pr(input("Enter marks for subject Chemistry Enter \"AB\" id Absent to update: "), subject = "Chemistry")
					update_query = "UPDATE marksheet SET chemistry = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (chemistry, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "4":
					hindi = self.auth_only_theory_sub(input("Enter marks for subject Hindi Enter \"AB\" if Absent to update: "), subject = "Hindi")
					update_query = "UPDATE marksheet SET hindi = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (hindi, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "5":
					english = self.auth_only_theory_sub(input("Enter marks for subject English Enter \"AB\" id Absent to update: "), subject = "English")
					update_query = "UPDATE marksheet SET english = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (english, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "6":
					physics_pr = self.auth_practical_subject(input("Enter marks for subject Physics Practicalto update: "), subject = "Physics Practical")
					update_query = "UPDATE marksheet SET physics_practical = %s WHERE roll_number = %s"
					self.cursor.execute(update_query, (physics_pr, roll_number))
					self.conn.commit()
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				elif choice == "7":
					chemistry_pr = self.auth_practical_subject(input("Enter marks for subject Chemistry Practical to update: "), subject = "Chemistry Practical")
					update_query = "UPDATE marksheet SET chemistry_practical = %s WHERE roll_number = %s"
					self.cursor.execute(update_query)
					self.conn.commit(roll_number)
					print("Data updated successfully ")
					continue_update = input("Do you want to update more info if yes enter 'yes' else enter 'no': ")
					if continue_update.lower() == "no":
						break
				else:
					print("Invalid Choice: ")
					self.update_marksheet(roll_number)

		else:
			print("Invalid choice: ")
			self.update_marksheet()
		self.__init__()
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
		select_query =f"""SELECT * FROM marksheet WHERE roll_number = {r_number};"""
		self.cursor.execute(select_query) 
		data = self.cursor.fetchall() 
		if len(data) != 0:
			return self.auth_roll_num(input("Roll Number already exists please try diffrent: "))
		elif r_number.isnumeric() and len(r_number) == 7:
			return r_number
		else:
			if not(r_number.isnumeric()):
				return self.auth_roll_num(input("Please enter only numbers don't use special letters and spellings: "))
			elif len(r_number) != 7 :
				return self.auth_roll_num(input("Length of roll number must be 7: "))
			else:
				return self.auth_roll_num(input("Please reenter Roll number: "))


	# Check whether any sumbers present in the name or not
	def check_name(self, name):
		special_letters = ('#', "@", "!", "_", "$", "%", "&", "," "^", "*", "(", ")", "{" , "}", "\\" , "|", "?", ":", ";", ">", "<", "/")
		for index, letter in enumerate(special_letters):
			if (str(index) in name) or (letter in name):
				return self.check_name(input("Please don't use special characters and numbers in name: "))
		else:
			return name

	def auth_dob(self, dob):
		day, month, year = dob.split('-')
		if len(day) == 2:
			if len(month) == 2:
				if len(year) == 2 or len(year) ==4:
					try:
						d =  datetime.strptime(dob, "%d-%m-%Y")
						return str(d).split(" ")[0]
					except Exception as e:
						return self.auth_dob(input("Enter date of birth in correct formate: "))
				else:
					return self.auth_dob(input("Enter date of birth in correct formate: "))
			else:
				return self.auth_dob(input("Enter date of birth in correct formate: "))
		else:
			return self.auth_dob(input("Enter date of birth in correct formate: "))

	# Constructor method 	
	def enter_data(self):	
		# User Name
		# Autogenerate scholar number and sch number
		self.scholar_number = random.randrange(1111111, 9999999)
		self.sch = str(random.randrange(111111111, 999999999)) 

		self.name = self.check_name(input("Enter Name: "))
		self.roll_number = self.auth_roll_num(input("Enter roll number: "))
		self.school_name = self.check_name(input("Enter school name: "))
		self.father_name = self.check_name(input("Enter father name: "))
		self.mother_name = self.check_name(input("Enter mother name:"))
		self.dob = self.auth_dob(input("Enter date of birth, formate must be 'dd-mm-yyyy': "))

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
		# String with scholar number and state board name correctly formatted
		self.state_board = f"{'|':>11}{'S. No.':>9} {self.scholar_number:<32}{'CENTRAL BOARD OF SECONDARY EDUCATION'} {'|':>40}"

		# String with Exam Type 
		self.exam_type = f"{'|':>11}{'ALL INDIA':>43} {'SENIOR SCHOOL CERTIFICATE EXAMINATION,2026'} {'SCH-' + self.sch :>28} {'|':>3}"

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
		print(f"{'|':>11}{'Date of birth: ':>18}{str(self.dob):<85}{'|':>16}")
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

