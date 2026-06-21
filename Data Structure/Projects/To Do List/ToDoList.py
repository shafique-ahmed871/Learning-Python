def addTask(taskList) :
	task = {}
	name = input("Enter task: ")
	
	for tas in taskList :
		if tas['name'].lower() == name.lower() :
			print(f"Task {name} is already in list!")
			return taskList
	task['name'] = name
	task['status'] = False
	taskList.append(task)
	print("Task added!")
	return taskList
def completeTask(taskList) :
	if not taskList :
		print("Empty task list!")
		return taskList
	while True :
		try :
			task_no = int(input(f"Enter task number {1}-{len(taskList)}: "))
		
		except ValueError:
			print("invalid task number!")
			continue
		if task_no < 1 or task_no > len(taskList) :
			print(f"Enter task number within range!")
			continue
		taskList[task_no - 1]['status'] = True
		print(f"{taskList[task_no - 1]['name']} marked complete!")
		break
	return taskList
		
def deleteTask(taskList) :
	if not taskList :
		print("Empty task list!")
		return taskList
	while True :
		try :
			task_no = int(input(f"Enter task number {1}-{len(taskList)}: "))
		
		except ValueError :
			print("invalid task number!")
			continue
		if task_no < 1 or task_no > len(taskList) :
			print(f"Enter task number within range!")
			continue
		name = taskList[task_no - 1]['name']
		taskList.remove(taskList[task_no - 1])
		print(f"{name} is deleted!")
		break
	return taskList

def showPending(taskList) :
	if not taskList :
		print("Empty task List!")
		return 
	
	isPending = False
	for task in taskList :
		if not task['status'] :
			print(f"{task['name']}	[]")
			isPending = True
	if not isPending :
		print("No task in Pending")
	
def showAll(taskList) :
	if not taskList :
		print("Empty task List!")
		return 
	for index , task in enumerate(taskList , 1) :
		if task['status'] :
			print(f"{index}. {task['name']}	[done]")
		else :
			print(f"{index}. {task['name']}	[Pending]")


def display() :
	print("==== To-Do List ====")
	taskList = []
	while True :
		print("""
1. Add Task
2. Complete Task
3. Delete Task
4. Show Pending
5. Show All
6. Exit
""")

		try :
			choose = int(input("Choose: "))
			if choose < 1 or choose > 6 :
				print("Enter choose b/w 1-6: ")
				continue
		except ValueError :
			print("Invalid choose, choose must be number!")
			continue
		if choose == 1 :
			taskList = addTask(taskList)
		elif choose == 2 :
			taskList = completeTask(taskList)
		elif choose == 3 :
			taskList = deleteTask(taskList)
		elif choose == 4 :
			showPending(taskList)
		elif choose == 5 :
			showAll(taskList)
		elif choose == 6 :
			print("Goodbye!")
			break

display()

		