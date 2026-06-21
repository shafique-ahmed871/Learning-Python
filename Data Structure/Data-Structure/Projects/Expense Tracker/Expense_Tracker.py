def setBudget(budgets) :

	category = input("Enter category: ")

	budget = numericalValid("budget")


	budgets[category] = budget

	return budgets


def addExpense(expenses , budgets) :

	if not budgets :

		print("No category in budgets!")
		return expenses

	category = input("Enter category: ")

	if category not in budgets :

		print(f"{category} is not in budgets!")
	
		return expenses

	

	expense = {}
	
	amount= numericalValid("amount")

	desc = input("Enter description: ")

	date = input("Enter date(DD-MM): ")

	expense['category'] = category

	expense['amount'] = amount

	expense['description'] = desc

	expense['date'] = date

	expenses.append(expense)

	print("Expense added successfully!")

	return expenses

def numericalValid(message) :

			
		while True :

			try :

				value = float(input(f"Enter {message}: "))

			except :

				print(f"{message} must be in number!")
				continue

			if value <= 0:

				print(f"{message} must be positive!")
				continue

			break

		return value

	
def showByCategory(expenses) :

	if not expenses :

		print("no expense made yet!")
		return 

	category = input("Enter category: ")

	depart = eachCategoryExpenses(expenses , category)

	print(f"--- {category} Expenses ---")
	
	if not depart :

		print("no expense made in category {category}!")
		return 

	total = 0

	for expense in depart :

		print(f"{expense['date'] :<8}{expense['description'] :<14}RS.{expense['amount']}")

		total += expense['amount']

	print(f"Total in {category}: RS.{total}")



def eachCategoryExpenses(expenses , category) :

	cateList = [expense for expense in expenses if expense['category'].lower() == category.lower()]

	return cateList

def eachCategorySpent(expenses , category) :

	categoryExpenses = eachCategoryExpenses(expenses , category)

	sum = 0

	for exp in categoryExpenses :

		sum += exp['amount']

	return sum
 
def showBudgetStatus(expenses , budgets) :
	
	if not budgets :

		print("No category in budget!")
		return

	print("--- Budget Status ---")

	print(f"{'Category' :<16}{'Spent' :<10}{'Budget' :<10}{'Status' :<10}")

	for bud , price in budgets.items() :

		spent = eachCategorySpent(expenses , bud)

		if spent <= price :

			status = '✅ ok'
		else :

			status = '⚠️ over'

		print(f"{bud :<16}{spent :<10.1f}{price :<10.1f}{status :<10}")


def showAnalytics(expenses , budgets) :
	
	if not budgets or not expenses :

		print("no category in budget or no expense made yet!")

		return 

	totalList = []

	totalSpent = 0

	for budget in budgets.keys() :

		totalSpentCate = {}

		totalSpentCate['category'] = budget

		
		totalSpentCate['spent'] = eachCategorySpent(expenses , budget)

		totalSpent += eachCategorySpent(expenses , budget)

		totalList.append(totalSpentCate)


	totalList = max(totalList, key=lambda x: x['spent'])
	
	print("--- Analytics ---")
	print(f"{'Total Spent' :<16} : RS.{totalSpent}")
	print(f"Biggest Category : {totalList['category']} ({(totalList['spent'] * 100/ totalSpent).:1f}%)")
	print(f"Number of Transactions : {len(expenses)}")
	print(f"Average per Transaction: RS.{(totalSpent/len(expenses)).:1f}")

		

def monthlySummarry(expenses) :

	summary = {}

	for expense in expenses:
		category = expense['category']
		amount = expense['amount']
    
		if category not in summary:
        		# first time seeing this category - create it
        		summary[category] = {"count": 0, "total": 0}
    
    		summary[category]['count'] += 1
    		summary[category]['total'] += amount

	print("--- Monthly Summary ---")
	print(f"{'Category':<15}{'Transactions':<15}Total Spent")

	grand_total = 0
	total_count = 0

	for category, data in summary.items():
    		print(f"{category:<15}{data['count']:<15}Rs.{data['total']}")
    		grand_total += data['total']
    		total_count += data['count']

	print(f"\nTotal Transactions : {total_count}")
	print(f"Total Spent         : Rs.{grand_total}")

	daily_totals = {}
	for expense in expenses:
    		date = expense['date']
    		daily_totals[date] = daily_totals.get(date, 0) + expense['amount']

	highest_day = max(daily_totals, key=daily_totals.get)
	print(f"Highest Spending Day: {highest_day} (Rs.{daily_totals[highest_day]})")

	

def menu() :

	expenses = []

	budgets = {
    	"Food": 6000,
    	"Transport": 2000
		}

	print("=== Expense Tracker ===")

	while True :

		print("1. Add Expense\n2. Set Budget\n3. Show By Category")
		print("4. Monthly Summarry\n5. Show Budget Status\n6. Show Analytics\n7. Exit")

		while True :

			choose = numericalValid("Choose")
		
			if choose < 1 or choose > 7 :

				print("choose must be b/w (1-7): ")
				continue
			break

		match choose :

			case 1 :

				expenses = addExpense(expenses , budgets)
			
			case 2 :

				budgets = setBudget(budgets)

			case 3 :

				showByCategory(expenses)

			case 4 :

				monthlySummarry(expenses)

			case 5 :

				showBudgetStatus(expenses , budgets)

			case 6 :

				showAnalytics(expenses , budgets)

			case 7 :

				print("Goodbye!")
				return


menu()

			
 