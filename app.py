import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 

    jsonStr = request.get_json()
    #print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    s=jsonObj['mat']
    r=int(jsonObj['m'])
    c=int(jsonObj['n'])
    l1=s.split(':')
    for i in range(len(l1)):
        l2=l1[i].split(',')
        l1[i]=l2
    def transpose_calculator(lst,m,n):
        mat_tr=[[0 for x in range(n)] for y in range(m)]
        for i in range(n):
            for j in range(m):
                mat_tr[i][j]=lst[j][i]
        return(mat_tr)
    if transpose_calculator(l1,r,c)==l1:
        response+="Symmetric matrix"
    else:
        response+="Asymmetric matrix"
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
