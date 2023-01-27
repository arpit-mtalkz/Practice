import pymongo
import sys

#get a connection to database
connection = pymongo.MongoClient('mongodb://localhost')
    #get a handle to database
db=connection.test
vehicles=db.vehicles

vehicle_VIN = input('What is the Vehicle VIN number? ')
vehicle_Make = input('What is the Vehicle Make? ')
newVehicle = {'VIN' : (vehicle_VIN).upper(), 'Make' : (vehicle_Make)}

try:
    vehicles.insert_one(newVehicle)
    print ('New Vehicle Inserted')

except  Exception as e:
        print ('Unexpected error:', type(e), e)

#print Results
results = vehicles.find()

print()
# display documents in collection
for record in results:
    print(record['VIN'] + ',',record['Make'])
#close the connection to MongoDB
connection.close()