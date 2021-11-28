name=[]
contact=[]
address=[]
count=0
# Function to Enter Details
def insert():
        global count
        n=int(input("How many contacts you want to insert: "))
        for i in range(0,n):
            print("ENTER DETAILS of ",(i+1),"Person.")
            na=input("ENTER  Name:")
            cont=input("ENTER Phone number:")
            ad=input("ENTER Address: ")
            name.append(na)
            contact.append(cont)
            address.append(ad)
            print((i+1)," person succesfully registered.\n")
            count=count+1
# Function to Search Details
def search():
    c=input("ENTER NAME OF PERSON TO SEARCH DETAILS: ")
    for i in range(0,count):
        if c==name[i]:
            print("DETAILS FOUND\n")
            print("Name: ",name[i])
            print("Contact: ",contact[i])
            print("Address:",address[i])
            break
         # "else" to check if i has reached the end of list ;
        # if reched at end and data doesn't exist otherwise loop back to "if"
        else:
            if (i == len(name)-1):
                print("NOT FOUND")
# Function to delete customer Details
def deltee():
    global count
    m = input("ENTER NAME OF PERSON TO DELETE DETAILS: ")
    for i in range(0, count):
        if m == name[i]:
            del name[i]
            del contact[i]
            del address[i]
            print("\nDETAILS DELETED SUCESSFULLY!")
            count=count-1
            break
         # "else" to check if i has reached the end of list ;
        # if reched at end and data doesn't exist otherwise loop back to "if"
        else:
            if (i == len(name)-1):
                print("NOT FOUND")

# Function to Update details of Customer
def update():
    global count
    l = input("ENTER NAME OF PERSON TO UPDATE DETAILS: ")
    for i in range(0, count):
        if(l==name[i]):
            print("DETAILS FOUND: \n")
            print("___________________________________________")
            print("NAME   ->", name[i], "                      ")
            print("Contact->", contact[i], "                  ")
            print("Address->", address[i], "                  ")
            print("___________________________________________", "\n")
            print("Now Update Details:")
            del name[i]
            del contact[i]
            del address[i]

            for j in range(0,count):
                nam = input("ENTER  Name:")
                contt = input("ENTER Phone number:")
                add = input("ENTER Address: ")
                name.append(nam)
                contact.append(contt)
                address.append(add)
                print("DETAILS SUCESSFULYY UPDATED")
                break
            count=count-1    
            count=count+1
# Function to view details
def view():
        print("**********************")
        print("***CUSTOMER DETAILS***")
        print("**********************\n")
        for i in range(0,count):

            print("___________________________________________")
            print("NAME   ->",name[i],"                      ")
            print("Contact->",contact[i], "                  ")
            print("Address->",address[i], "                  ")
            print("___________________________________________","\n")
# Function to allow user choode between diffrent operations.
def options():
        ch=-1
        while(ch!=0):
            print("****************************")
            print("*WELCOME!To PHONE DIRECTORY *")
            print("****************************\n\n")
            print("**************************")
            print("1-Insert contact         *")
            print("2-Delete contact         *")
            print("3-Update contact         *")
            print("4-Display contact        *")
            print("5-Search                 *")
            print("0-Exit                   *")
            print("**************************")
            ch = int(input("\nENTER YOUR CHOICE:\n"))
            if (ch == 1):
                insert()
            elif (ch == 2):
                deltee()
            elif (ch == 3):
                update()
            elif (ch == 4):
                view()
            elif (ch == 5):
                search()
            elif(ch==0):
                print("\nEXIT\n")
                break
            else:
                print("INVALID! INPUT\n")
                options()

options()