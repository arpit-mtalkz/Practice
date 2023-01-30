import pymongo

client = pymongo.MongoClient("mongodb+srv://arpit-mtalkz:12345@cluster0.kd6smw3.mongodb.net/?retryWrites=true&w=majority")
project=client["project"]
mycol=project["website"]
# input from the user during runtime
mymultpledoc = []
n=int(input())

for i in range(n):
    mydoc={}

    category1 = "Name"
    Name = input("Enter name of person : ")
    mydoc[category1] = Name

    category2 = "Project : "
    Project=input("Enter the project allocated : ")
    mydoc[category2] = Project

    category3 = "Coworker : "
    Coworker=input("Enter the Coworker in number working along with : ")
    mydoc[category3] = Coworker

    category4 = "Deadline in days : "
    deadline=input("Enter deadline in days : ")
    mydoc[category4] = deadline
    
    mymultpledoc.append(mydoc)

# predefined input
'''mydoc =[{
    'name' :'Prashant',
    'Project':'Admin Page',
    'Coworker': 5,
    'Deadline in days':'7 days'
},
{
    'name':'Arpit',
    'Project':'Front end',
    'Coworker': 7,
    'Deadline in days':'5 days'
},
{
    'name':'Ajay',
    'Project':'Front end',
    'Coworker': 7,
    'Deadline in days':'5 days',
    'Cohead' : 'manas'
}]'''

#Find the data of the user searched by name
'''a = input()
x = []
x = mycol.find({"name": a})
print(x[0])'''
#Add
x = mycol.insert_many(mymultpledoc)


#Update
'''myquery = { "name": "Prashant" }
newvalues = { "$set": { "Project": "Aashiqui 2" } }'''

# mycol.update_one(myquery, newvalues)


#Delete
'''myquery = { "name": "Prashant" }

# mycol.delete_one(myquery)'''

#delete all data from database
''' x = mycol.delete_many({})'''

# print(x.deleted_count, " documents deleted.")
'''myquery = { "name": {"$regex": "^P"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")'''