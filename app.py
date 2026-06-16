import sqlite3
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from flask import Flask,render_template,request,redirect
#import library
app=Flask(__name__)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
db_path=os.path.join(BASE_DIR,"loan.db")
X = np.array([[20000],[25000],[30000],[35000],[40000],[60000],[70000],[80000],[90000],[100000]])
# Labels
# 0 = Rejected
# 1 = Approved
Y = np.array([0,0,0,0,0,1,1,1, 1,1])
model=DecisionTreeClassifier()
model.fit(X,Y)
#connect database
conn=sqlite3.connect(db_path)
cursor=conn.cursor()
#create loan table
cursor.execute("""CREATE TABLE IF NOT EXISTS loan(id INTEGER PRIMARY KEY AUTOINCREMENT,salary REAL,prediction INTEGER,probability REAL)""")
conn.commit()
conn.close()
@app.route('/',methods=["GET","POST"])
def home():
    return render_template('home.html')

@app.route('/predictions',methods=["GET","POST"])
def predictions():
    prediction=None
    probability=None
    result=None
    if request.method=="POST":
        salary=float(request.form['salary'])
        applicant=[[salary]]
        prediction=model.predict(applicant)[0]
        if prediction==1:
            result="Loan Approved"
        else:
            result="Loan Rejected"
        probabilities=model.predict_proba(applicant)[0]
        probability=float(np.max(probabilities))
        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        #insert values into table
        cursor.execute("""INSERT INTO loan (salary,prediction,probability) VALUES(?,?,?)""",(salary,int(prediction),probability))
        conn.commit()
        conn.close()
        #visulization decision tree
        plt.figure(figsize=(8,4))
        plot_tree(model,filled=True)
        plt.title("Decision Tree for Loan Approval")
        #save the decision_tree.png graph in static folder
        plt.savefig(os.path.join(app.root_path,'static','decision_tree.png'))
    return render_template('predictions.html',result=result,prediction=prediction,probability=probability)


@app.route("/history")
def history():
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    #view the data
    cursor.execute("SELECT * FROM loan")
    data=cursor.fetchall()
    conn.close()
    return render_template("history.html",history=data)

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    if request.method=="POST":
        salary=float(request.form["salary"])
        applicant=[[salary]]
        prediction=model.predict(applicant)[0]
        probabilities=model.predict_proba(applicant)[0]
        probability=float(np.max(probabilities))
        #update salary 
        cursor.execute(
            """
            UPDATE loan 
            SET salary=?,prediction=?,
            probability=? WHERE id=?""",(salary,int(prediction),probability,id))
        conn.commit()
        conn.close()
        #back to history
        return redirect("/history")
    cursor.execute("SELECT * FROM loan WHERE id=?",(id,))
    # it selects only one row
    loan=cursor.fetchone()
    conn.close()
    return render_template("update.html",loan=loan)
                       
@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    if request.method=="POST":
        #Delete the data
        cursor.execute("DELETE FROM loan where id=?",(id,))
        conn.commit()
        conn.close()
        #after deletion it sends the return message
        return """<h1 style='color:black;  background-color:rgb(81, 104, 216); text-align:center; padding:20px;'> DELETED SUCCESSFULLY</h1>"""
    cursor.execute("SELECT * FROM loan WHERE id=?",(id,))
    data=cursor.fetchone()
    conn.close()
    return render_template("delete.html",data=data)                 

if __name__=="__main__":
    app.run(debug=True)