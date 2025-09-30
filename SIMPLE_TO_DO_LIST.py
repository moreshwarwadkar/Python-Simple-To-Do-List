# SIMPLE TO DO LIST 

task = []

def display():

    if task == []:
        print('\nNo More Tasks')
    
    else:
        print("\nYour To Do List:")
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")

def add():

    item1 = input('Enter Task Name:')
    task.append(item1)
    print('\nTask Added Successfully..')

def remove():

    print("\nYour To Do List:")
    for i, t in enumerate(task, 1):
        print(f"{i}. {t}")

    no = int(input('Enter Task Number To Delete Task:'))-1

    try:
        print(task[no])

    except:
        print('Task Not Present..!')
        
    else:
        task.pop(no)
        

def main():

    while True:

        print('\n*** SELECT ANY OPERATION *** ')
        print('\n1.Display All Task\n2.Add Task\n3.Remove Task\n4.Exit')
        ch = int(input('Enter Your Choice:'))

        if ch == 1:

            display()

        elif ch == 2:

            add()

        elif ch == 3:

            remove()

        elif ch == 4:
            
            print('Thank You..!')
            break

main()