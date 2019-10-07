import csv
import datetime

print("\t\t\t Hi..!! Welcome To Our Project RAPPEL...!! \t\t\t ")

ans = input("\nDo you want to see the menu..? (y/n) : ")

while ans == 'y':
	print("\nMenu :-")
	print("\n1.Add Birthday\n2.Add Anniversery\n3.Check For any Remainder\n4.Exit")
	choice = input("\nEnter your choice : ")
	ch = int(choice)
	if ch == 1:
		print("\nYou choiced for birthday ")
		name1 = input("\nEnter the name : ")
		date1 = input("\nEnter the birth date (yyyy-mm-dd) : ")
		mail1 = input("\nEnter their Mail Id : ")

		f1 = open("birthday.txt",'a')
		f1.write(name1)
		f1.write(",")
		f1.write(date1)
		f1.write(",")
		f1.write(mail1)
		f1.write("\n")
		f1.close()
		print("\nBirthday added sucessfully..!!")
	elif ch == 2:
		print("\nYou choiced for anniversery ")
		n1 = input("\nEnter first name : ")
		n2 = input("\nEnter second name : ")
		date2 = input("\nEnter the anniversery date (yyyy-mm-dd): ")
		mail2 = input("\nEnter their Mail Id : ")

		f2 = open("anniversery.txt",'a')
		f2.write(n1)
		f2.write(" ")
		f2.write(n2)
		f2.write(",")
		f2.write(date2)
		f2.write(",")
		f2.write(mail2)
		f2.write("\n")
		f2.close()
		print("\nAnniversery added sucessfully..!!")
	elif ch == 3:
		print("\nMenu for checking remainder :-")
		print("\n1.Check remainder of birthday.\n2.Check remainder for anniversery.")
		c = input("\nEnter your choice : ")
		c1 = int(c)
		if c1 == 1:
			x = []	
			y = []
			z = []
			with open('birthday.txt') as csvfile: 	
				csvreader = csv.reader(csvfile,delimiter=',')
				for line in csvreader:
					x.append(line[0])
					y.append(line[1])
					z.append(line[2])
		
				currentDT = datetime.date.today()
				date1 = str(currentDT)
				print("\nToday's date is : ",date1)
				year,month,day = date1.split("-")
				for i in range(len(y)):
					y1,m1,d1 = y[i].split("-")
					if m1 == month and d1 == day:
						print("Its ",x[i]," birthday today..!!")
		else:
			x1 = []	
			y1 = []
			z1 = []
			with open('anniversery.txt') as csvfile1: 	
				csvreader1 = csv.reader(csvfile1,delimiter=',')
				for line1 in csvreader1:
					x1.append(line1[0])
					y1.append(line1[1])
					z1.append(line1[2])
			
			currentDT1 = datetime.date.today()
			date_1 = str(currentDT1)
			print("\nToday's date is : ",date_1)
			year1,month1,day1 = date_1.split("-")
			for j in range(len(y1)):
				y2,m2,d2 = y1[j].split("-")
				if m2 == month1 and d2 == day1:
					print("Its ",x1[j]," anniversery today..!!")

	else:	
		print("\nYou have been exited from the program..!!")
		exit(0)
		
