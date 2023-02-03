from flask import Flask,jsonify,request
from bson import json_util
import pymongo
import json
  
app = Flask(__name__)
  

client = pymongo.MongoClient("mongodb+srv://arpit:12345@cluster0.de4wpvp.mongodb.net/?retryWrites=true&w=majority")
contact=client["School"]
mycol=contact["Teacher"]
 

#Inserting or POST operation

@app.route('/insert',methods=['POST'])
def insert():
    data=request.get_json()
    mycol.insert_one(data)
    #client.close()
    return jsonify({"status":"Connection successful"}),200


#Fetching or GET operation
@app.route('/',methods=['GET'])
def get():
    documents = mycol.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response, indent=4, default=json_util.default)


#update or PUT operation

@app.route('/update/<string:name>',methods=['PUT'])
def update(name):
    query = {"name":name}
    data = request.get_json()

    new_query={"$set":{"Deadline in days":data["Deadline in days"]}}
    query=mycol.update_one(query, new_query)

    return jsonify({"Status":"Connection Successful"}),200

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete(name):
    query={"name":name}
    mycol.delete_many(query)

    return jsonify({"status":"Connection successful"})

if __name__ == '__main__':
  
    app.run(debug=True,port=9001)