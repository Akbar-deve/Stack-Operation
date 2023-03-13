# Stack is linear data structure, It follows the principle of "LIFO"(Last in First out).
# Insertion & Deletion of element is happens only at one end.
# We are creating stack with the help of List.
# Operations can be performed on stack are 
# 1.PUSH()
# 2.POP()
# 3.PEEK()
# 4.ISEMPTY()
# 5.ISFULL()
# 6.DISPLAY()
#




#performing Stack operations
#Creating a class called Stack
class stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        #creating stack with the help of list.
        self.data=[]

    #Checking whether the stack is full or not.
    def isFull(self):
        if len(self.data)==self.maxsize:
            return True
        else:
            return False 
        
    #Checking whethar the stack is empty or not.    
    def isEmpty(self):
         if len(self.data)==0:
              return True
         else:
              return False
         
    #Function to add the element to the stack at last.
    def push(self,ele):
        if len(self.data) == self.maxsize:
            print( "Stack is full no element will get added now.")
        else:
            self.data.append(ele)

    #Function to removing the last element from the stack.
    def pop(self):
        if self.isEmpty():#If stack is empty the it prints no element to pop.
          print("No element in stack to pop")
        else:
          print(self.data.pop()) 

    #Function displaying the peek element that is top most element of stack.
    def peek(self):
          if self.isEmpty():
            print('stack has no peek element to display')
          else:
            print(self.data[-1]) 

    #Function to Display the stack elements
    def display(self):
        print(self.data)


#Creating object of class stack.
s=stack(int(input("enter size of stack")))

#while loop for continues execution that is like it execute infinite times
while True:
    print('Select the option to perform')
    print('1.Push\n2.Pop\n3.display\n4.peek\n5.empty\n6.isFull')
    print()
    #Enter only interger value
    opt=int(input("enter the optiion wants to perform"))
    match opt:
        case 1:
            val=int(input("enter the val to push => "))
            s.push(val)
        case 2:
            s.pop()
        case 3:
            s.display()
        case 4:
            s.peek()
        case 5:
            print("Stack is Empty -->",s.isEmpty())
        case 6:
            print("stack is full --> ",s.isFull())
        #If none case is true then the default case _ block will executes.
        case _ :
              print('enter a correct option')