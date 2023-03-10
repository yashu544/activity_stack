#stack_program
stack_1=[]
stack_2=[]
def push():
    for i in range(5):
        element=int(input("enter the element"))
        if element%2==0:
            stack_1.append(element)
        else:
            stack_2.append(element)
def pop():
    print("1 or 2")
    b=int(input())
    if b==1:
        if not stack_1:
            print("stack is empty")
        else:
            e=stack_1.pop()
            print(stack_1)
    elif b==2:
        if not stack_2:
            print("stack is empty")
        else:
            e=stack_2.pop()
            print(stack_2)
def display():
    print("1 or 2")
    a=int(input())
    if a==1:
        print(stack_1)
    else:
        print(stack_2)
while True:
    print("select option 1.push 2.pop 3.show 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("choose the correct option")
