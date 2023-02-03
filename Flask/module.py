from flask import Flask,jsonify,request
import pymongo
import json
from teacher import Teacher


app=Flask(__name__)

        

@app.route('/dataSend',methods=['GET','POST'])
def home():
    try:
        client = pymongo.MongoClient("mongodb+srv://arpit:12345@cluster0.de4wpvp.mongodb.net/?retryWrites=true&w=majority")
        db = client['School']
        coll = db['Teacher']
        if request.method == 'POST':
            data = request.get_json()
            coll.insert_one(data)
            client.close()
            return jsonify({"status":"Connection Succesfull"}) , 200
        else:
            x = []
            x = coll.find({"name":"Prashant"})
            for i in x:
                print(i)

    except Exception as e:
        print("error ::::::::",e)
    return {}, 200




if __name__=="__main__":
    app.run(debug=True,port=9001)  