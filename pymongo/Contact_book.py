import pymongo
import sys

client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]

# initial phonebook where 1st we will store the contacts
def phonebook():
    rows=int(input("Please enter the number of contacts to be inserted : "))
    col=5
    phone_book=[]
    
    
 
    for i in range(rows):
        mydoc={}
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
       

        
            

    
        
        
    # Input field's which are predefined and shown to user when asked to save the number
    
        category0="_id"
        id=input("Enter the id : ")
        mydoc[category0]=id

        
        category1="Name"
        name=input("Enter the name : ")
        mydoc[category1]=name
        if mydoc[category1]=='' or mydoc[category1]==' ':
            sys.exit("Mandatory Field")


        category2="Number"
        num=int(input("Enter the number : "))
        mydoc[category2]=num


        category3="Email"
        mail=input("Enter the mail id : ")
        mydoc[category3]=mail


        category4="DOB"
        print("Enter details for your dob")
        date=input("Enter date : ")
        month=input("Enter month : ")
        year=input("Enter Year : ")
        dob=date+"/"+month+"/"+year
        mydoc[category4]=dob


        category5="Category"
        category=input("Enter category(Family/Friends/Work/Others): ")
        mydoc[category5]=category   
        phone_book.append(mydoc)
            

            
    x=mycol.insert_many(phone_book)
    return phone_book  


def menu():
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add multiple contacts")
    print("2. Add a new contact")
    print("3. Remove an existing contact")
    print("4. Delete all contacts")
    print("5. Search for a contact")
    print("6. Display all contacts")
    print("7. Exit phonebook")
    choice=int(input("Please Enter Your Choice : "))

    return (choice)


def add_contact():
    
    
    myContact={}

    category0="_id"
    id=input("Enter ID : ")
    myContact[category0]=id
        
    category1="Name"
    name=input("Enter the name : ")
    myContact[category1]=name
    if myContact[category1]=='' or myContact[category1]==' ':
        sys.exit("Mandatory Field")

    category2="Number"
    num=int(input("Enter the number : "))
    myContact[category2]=num

    category3="Email"
    mail=input("Enter the mail id : ")
    myContact[category3]=mail

    category4="DOB"
    print("Enter details for your dob")
    date=input("Enter date : ")
    month=input("Enter month : ")
    year=input("Enter Year : ")
    dob=date+"/"+month+"/"+year
    myContact[category4]=dob
    
    category5="Category"
    category=input("Enter category(Family/Friends/Work/Others): ")
    myContact[category5]=category 
    
    x=mycol.insert_one(myContact) 


    return add_contact

def delete_contact():
    a=input("Enter name to delete : ")
    myquery={"Name":a}
    mycol.delete_one(myquery)

def delete_all():
    mycol.delete_many({})

    return delete_all

def search_contact():


    def search_by_name():
        a=input("Enter name to search : ")
        x = []
        x = mycol.find({"Name": a})
        print(x)

        return search_by_name

    def search_by_number():
        a=input("Enter number to search : ")
        x=[]
        x=mycol.find({"Number":a})
        print(x)

        return search_by_number

    def search_by_mail():
        a=input("Enter Email to search : ")
        x=[]
        x=mycol.find({"Email":a})
        print(x)

        return search_by_mail

    def search_by_dob():
        a=input("Enter DOB to search : ")
        x=[]
        x=mycol.find({"DOB":a})
        print(x)

        return search_by_dob

    def search_by_category():
        a=input("Enter Category to search : ")
        x=[]
        x=mycol.find({})
        for i in x:
            print(i)

        return search_by_category

    def menu():
        print("1.Search contact by a name")
        print("2.Search contact by number")
        print("3.Search contact by Email")
        print("4.Search contact by Date of Birth")
        print("5.Search contact by Category or relations")
        
        choice=int(input("Please Select the way you want to search for a contact : "))

        return choice




    ch=1
    while ch in (1,2,3,4,5):
        ch=menu()
        if ch==1:
            x=search_by_name()
        elif ch==2:
            x=search_by_number()
        elif ch==3:
            x=search_by_mail()
        elif ch==4:
            x=search_by_dob()
        elif ch==5:
            x=search_by_category()
        else:
            print("Please enter a valid input !")
            pass


    return search_contact

def display_all():
    pass

def thanks():
    pass

ch = 1
while ch in (1, 2, 3, 4, 5,6):
    ch = menu()
    if ch==1:
        x=phonebook()
    elif ch == 2:
        x = add_contact()
    elif ch == 3:
        x = delete_contact()
    elif ch == 4:
        x = delete_all()
    elif ch == 5:
        x = search_contact()
        if x == -1:
            print("The contact does not exist. Please try again")
    elif ch == 6:
        display_all()
    else:
        thanks()