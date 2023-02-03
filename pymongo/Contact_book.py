import pymongo
import sys

client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.cbks6s7.mongodb.net/?retryWrites=true&w=majority")
contact=client["Contact"]
mycol=contact["Book"]

class contactBook():


# initial phonebook where 1st we will store the contacts


    def phonebook():
        rows=int(input("Please enter the number of contacts to be inserted : "))
        col=5
        phone_book=[]


    
        for i in range(rows):
            mydoc={}
            print("\nEnter contact %d details in the following order (ONLY):" % (i+1))


        # Input field's which are predefined and shown to user when asked to save the number


            
            name=input("Enter the name : ")
            x = mycol.find({"name": name})
            category1="Name"
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

            x = mycol.find({"name": name})
            if mydoc[category1]==x:
                print('Name already exist')


        x=mycol.insert_many(phone_book)
        
        return phone_book  

    #Menu which will show user to choose or perform action
    def menu():
        print("\t--------------------------------------------------------------\n")
        print("\tWelcome to smart phone directory\n")
        print("\t--------------------------------------------------------------\n")
        print("\tYou can now perform the following operations on this phonebook\n")
        print("\t--------------------------------------------------------------\n")
        print("1. Add multiple contacts")
        print("2. Add a new contact")
        print("3. Remove an existing contact")
        print("4. Delete all contacts")
        print("5. Search for a contact")
        print("6. Update a contact present in directory")
        print("7. Display all contacts")
        print("8. Exit phonebook")
        print("\t--------------------------------------------------------------\n")
        choice=int(input("Please Enter Your Choice : "))


        return (choice)

    #for addition of contact one at a time
    def add_contact():


        myContact={}


        
        name=input("Enter the name : ")
        category1="Name" 
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


        return myContact


    #Deletion of contacts in the directory of contactbook one by one
    def delete_contact():
        a=input("Enter name to delete : ")
        myquery={"Name":a}
        mycol.delete_one(myquery)

        return mycol

    #Empty the call book all at once

    def delete_all():
        mycol.delete_many({})

        return mycol


    #Searching contacts on the basis of the category seacrhed by user i.e., it can be name, number , mail id etc.
    def search_contact():

        # Searching contacts by entering name which is stored in contactbook
        def search_by_name():
            a=input("Enter name to search : ")
            x = []
            x = mycol.find({"Name": a})
            for i in x:
                print(i)

            return x

        # Searching contacts by entering number which is stored in contactbook
        def search_by_number():
            a=input("Enter number to search : ")
            x=[]
            x=mycol.find({"Number":a})
            for i in x:
                print(i)

            return mycol

        # Searching contacts by entering Email which is stored in contactbook
        def search_by_mail():
            a=input("Enter Email to search : ")
            x=[]
            x=mycol.find({"Email":a})
            for i in x:
                print(i)

            return mycol

        # Searching contacts by entering DOB which is stored in contactbook
        def search_by_dob():
            a=input("Enter DOB to search : ")
            x=[]
            x=mycol.find({"DOB":a})
            for i in x:
                print(i)

            return mycol

        # Searching contacts by entering Category or relation which is stored in contactbook
        def search_by_category():
            a=input("Enter Category to search : ")
            x=[]
            x=mycol.find({"Category",a})
            for i in x:
                print(i)

            return mycol

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
                menu()


        return ch

    def update_contact():
        a=input("Enter the name to search : ")
        myquery={"Name":a}
        x = []
        x = mycol.find({"Name": a})
        for i in x:
            print(i)
        d=input("Enter new name to update : ")
        newvalue={"$set":{"Name":d}}
        z=mycol.update_one(myquery,newvalue)
        
        return z



    def display_all():
        cursor = mycol.find({})
        for document in cursor:
            print(document)

        return cursor


    def thanks():
    
        print("1.Do you really wish to exit")
        cho=input("")
        if cho=="y":
            sys.exit
        else:
                
        return cho


    ch = 1
    while ch in (1, 2, 3, 4, 5, 6, 7):
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
        elif ch==6:
            x = update_contact()
        elif ch == 7:
            display_all()
        else:
            thanks()


