#TO-DO LIST

tasks = []

while True:
    try:
        print("**********************")
        print("TO-DO LIST PROGRAM")
        print("1.Show tasks")
        print("2.Add tasks")
        print("3.Remove tasks")
        print("4.Exit")
        print("***********************")
        choice = int(input("Enter your choice : "))
        if(choice == 1):
            for index,task in enumerate(tasks,start = 1):
                print(f"{index} : {task}")
            if not tasks:
                print("There is nothing in your tasks")
        elif(choice == 2):
            t = input("enter your task : ")
            tasks.append(t)
        elif(choice == 3):
            n = int(input("Enter the task number : "))
            r = n - 1
            tasks.pop(r)
        elif(choice == 4):
            print("Exiting....")
            break
    except ValueError:
        print("Invalid Input")

