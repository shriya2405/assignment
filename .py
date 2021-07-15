import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    response = ""
    for key, value in jsonObj.items():
        response += "<b>" +key+ "</b> is: <b>"+value +"</b><br>"
        
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    