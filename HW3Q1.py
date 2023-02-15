## This program stores information about mobile phone devices in a dictionary. Then it perform some search tasks 
## as shown in the sample run.
#

# YOUR CODE HERE
#add_phones function which takes in the empty dictionary and fills it with user enetered data
#and return the modified dictionary
def add_phone():
    d={}
    userInput=input("To add a new phone device enter:\nserial,brand,model,color,memory:")
    #user entered data is split into 5 parts with comma as seperator
    s1=list(userInput.split(","))
    #the key of the dictionary would be the serial number of the device and the value is a 
    #list with brand,model,color,memory specs in it
    d[s1[0]]=s1[1:]
    
    
    while len(userInput)!=0:
        userInput=input("add another phone or press Enter to finish: ")
        #user entered data is split into 5 parts with comma as seperator
        s1=list(userInput.split(","))
        # if the length of "st" list not equal to zero
        if(len(s1[1:])!=0):
            #the key of the dictionary would be the serial number of the device and the value is a 
    #list with brand,model,color,memory specs in it
            d[s1[0]]=s1[1:]
    return d
def get_user_choice():
    #presenting user with the menu to perform an operation and display the required data
    print("    **User Menu**     ")
    print("1 - Print all phones data in a tabular format")
    print("1 - Print phones information based on the phone serial number")
    print("3 - Print phones information based on brand")
    # user enters the choice number or quit
    choice_input=input('Enter your choice or "quit" to exit: ')
    return choice_input
def displayAll(data):
    #to print the data. the number of dashes may differ as per output console size
    print("-"*86)
    print('%-20s%-20s%-20s%-20s%-20s'%("Phone Serial","Brand","Model","Color","Memory"))
    #to print the data. the number of dashes may differ as per output console size
    print("-"*86)
    #iterating over the dictionary keys and printing it's values in a formatted way for the table
    for i in data.keys():
        x=data[i]
        print('%-20s%-20s%-20s%-20s%-20s'%(i,x[0],x[1],x[2],x[3]))
def displaySerial(data,serial):
    #if the serial number exists in the dictionary then we print the required data
    if serial in data.keys():
        x=data[serial]
        #to print the data. the number of dashes may differ as per output console size
        print("-"*86)
        print('%-20s%-20s%-20s%-20s%-20s'%("Phone Serial","Brand","Model","Color","Memory"))
        #to print the data. the number of dashes may differ as per output console size
        print("-"*86)
        print('%-20s%-20s%-20s%-20s%-20s'%(serial,x[0],x[1],x[2],x[3]))
        f=1
    else:
        #as the device doesn't exist we print a message for the user
        print('Device not found')
def displayBrand(data,brand):
    f=0
    
    for t in data.keys():
        x=data[t]
        #if the entered brand is present in the values of the dictionary then we print all the 
        #devices with specified brand in it
        if x[0]==brand:
            if f==0:
                #to print the data. the number of dashes may differ as per output console size
                print("-"*86)
                print('%-20s%-20s%-20s%-20s%-20s'%("Phone Serial","Brand","Model","Color","Memory"))
                #to print the data. the number of dashes may differ as per output console size
                print("-"*86)
            print('%-20s%-20s%-20s%-20s%-20s'%(t,x[0],x[1],x[2],x[3]))
            f=1
    if f==0:
        #if the brand doesn't exist we just print error message
                  print(brand,'brand is not available')
def main():
    #Here we call the functions
    data=add_phone()
    t=get_user_choice()
    # if "t" is 'quit' then the loop will stop
    while t!='quit':
        if t.isdigit()==True:
            ch=int(t)
            #if the user enters 1 then it will display "displayAll"
            if ch==1:
                displayAll(data)
            #if the user enters 3 then it will display "displaySerial"
            elif ch==2:
                serial=input('Enter the phone serial number : ')
                displaySerial(data,serial)
            #if the user enters 1 then it will display "displayBrand"
            elif ch==3:            
                brand=input('Enter the phone brand : ')
                displayBrand(data,brand)
        else:
            print("Wrong input")
        t=get_user_choice()
main()
