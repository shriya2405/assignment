import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    temp1=jsonObj['temp1']
    temp2=jsonObj['temp2']
    response+="<b> The input temparatures in Celcius are: <b>"+temp1+" and "+temp2+"</b><br>"
        
    f1=((float(temp1)*9.0)/5.0)+32.0
    f2=((float(temp2)*9.0)/5.0)+32.0
    
    response+="<b> The output temparatures in Fahrenheit are: <b>"+str(f1)+" and "+str(f2)+"</b><br>"
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    