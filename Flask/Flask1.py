from flask import Flask,jsonify,request

app=Flask(__name__)


store=[
    {
        "name":"mystore",
        "items":[
            {
            "name":"chair",
            "price":"1200",
            "Quantity":"20"
            }
        ]
    }
]
@app.route("/store",methods=['GET','POST'])
def stores():
    if request.method=='GET':
        
        return jsonify(store)

    else:
        request_data=request.get_json()
        new_store={"name":request_data["name"]}
        store.append(new_store)

        return new_store, 201

@app.route("/store/<string:name>/item",methods=["POST"])
def stores1(name):
    request_data=request.get_json()

    for st in store:
        if st["name"]==name:
            new_item={"name":request_data["name"],"price":request_data["price"],"Quantity":request_data["Quantity"]}
            st["items"].append(new_item)
            return new_item, 201

       
    return {"message":"Store not found"},404

if __name__ =='__main__':
    app.run(debug = True)
