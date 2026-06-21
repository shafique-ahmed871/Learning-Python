def addEmployee(employee) :

	emp_name = input("Enter Employee name: ")

	emp_id = input("Enter Employee id: ")

	emp_depart = input("Enter Employee Department: ")

	if emp_id in employee :

		print(f"Employee with id {emp_id} already exists!")

		return employee


	while True :

		try :

			basic_salary = float(input("Enter Employee basic salary: "))
	
		except ValueError :

			print("Invalid basic salary, must be number!")

			continue

		if basic_salary <= 0 :

			print("salary must be in positive number!")

			continue
		
		break

	emp_details = {}

	emp_details['name'] = emp_name

	emp_details['department'] = emp_depart

	emp_details['Basic salary'] = basic_salary

	employee[emp_id] = emp_details

	print(f"Employee {emp_name} added successfully!\n")

	return employee


def bonus(basic_salary) :
		
	return basic_salary * 0.1

def tax(basic_salary) :
	
	return (basic_salary + bonus(basic_salary)) * 0.05

def net_salary(basic_salary) :

	return basic_salary + bonus(basic_salary) - tax(basic_salary)


def generatePayslip(employee) :

	if not employee :

		print("No employee currently in system!\n")

		return

	emp_id = input("Enter Employee id: ")

	if emp_id not in employee :

		print(f"Employee with id {emp_id} is not in system!\n")

		return 

	print("--- Payslip ---")

	emp = employee[emp_id]

	print(f"{'Name' :<12} : {emp['name']}\n{'ID' :<12} : {emp_id}\n{'Department' :<12} : {emp['department']}")
	
	print(f"{'Basic Salary' :<12} : {emp['Basic salary'] :>12}\n{'Bonus (10%)' :<12} : {bonus(emp['Basic salary']):.1f}")

	print(f"{'Tax (5%)' :<12} : {tax(emp['Basic salary']):.1f}\n{'Net Salary' :<12} : {net_salary(emp['Basic salary']):.1f}\n")


def showAllEmployees(employee) :

	if not employee :

		print("No employee in system!\n")
		return

	print("--- All Employees ---")

	print(f"{'ID' :<8}{'Name' :<12}{'Department' :<12}Net Salary")

	for key , value in employee.items() :

		print(f"{key :<8}{value['name'] :<12}{value['department'] :<12}{net_salary(value['Basic salary']):.1f}")
	
	print()

	
def showByDepartment(employee) :

	if not employee :

		print("No employee in system!\n")
		return 

	depart = input("Enter department: ")
	
	print(f"--- {depart} Department ---")

	department = {key : value for key , value in employee.items() if value['department'].lower() == depart.lower()}
	
	if not department :

		print(f"No employee in department {depart}\n")
		return

	for key , value in department.items():

		print(f"{key :<8}{value['name'] :<12}{net_salary(value['Basic salary']):.1f}")
	print()

def totalPayroll(employee) :

	if not employee :

		print("No employee in system!\n")
		return
	print("--- Total Payroll ---")
	sum = emp = 0

	for value in employee.values() :

		sum += net_salary(value['Basic salary'])

		emp += 1

	print(f"{'Total Employees' :<16} : {emp}\n{'Total Payroll' :<16} : RS.{sum:.1f}\n")
	
	

def menu() :

	print("=== Employee Salary System ===")

	employee = {}

	while True :

		print("1. Add Employee\n2. Generate Payslip\n3. Show All Employees")
		print("4. Show By Department\n5. Show Total Payroll\n6. Exit")

		while True :

			try :

				choose = int(input("Choose: "))

			except ValueError :

				print("Invalid choose, must be number!")
				continue

			if choose < 1 or choose > 6 :

				print("choose must be b/w 1-6!")
				continue

			break

		match choose :

			case 1 :

				employee = addEmployee(employee)

			case 2 :

				generatePayslip(employee)

			case 3 :

				showAllEmployees(employee)

			case 4 :

				showByDepartment(employee)

			case 5 :

				totalPayroll(employee)

			case 6 :

				print("Goodbye!")

				break

menu()