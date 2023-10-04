from flask import Flask, render_template, request, redirect, url_for, flash 
import mysql.connector
app=Flask(__name__)

app.secret_key = 'secret'

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="vending_service"
)

cursor = db.cursor()

@app.route('/')
def Istpage():
    return render_template('1stpage.html')


@app.route('/end')
def valid():
    return render_template("validupdation.html")


@app.route('/add_data', methods=["POST", "GET"])
def add_data():
    if request.method == "POST":
        # Assuming you have a form with fields named 'medicineName', 'quantity', and 'expiryDate'
        medicineName = request.form['medicineName']
        quantity = request.form['quantity']
        expirydate = request.form['expiryDate']

        try:
            # Insert data into the database
            cursor.execute("INSERT INTO medicines (medicine_name, quantity, expiry_date) VALUES (%s, %s, %s)", (medicineName, quantity, expirydate))
            db.commit()  # Commit the changes to the database

            flash("Data added successfully", "success")
        except Exception as e:
            # Print the error message for troubleshooting
            print("Error:", str(e))
            flash("Error adding data to the database", "error")

        # Fetch any unread results to clear the cursor
        while cursor.nextset():
            pass

    return render_template("validupdation.html")  # Return a response, even in case of an error

@app.route('/retry',methods=['POST'])
def retry():
    return render_template('loginerror.html')




@app.route('/authenticate', methods=["POST","GET"])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT * FROM workers WHERE worker_name = %s AND password = %s", (username, password))
    
    # Fetch the result set or clear it
    user = cursor.fetchone()
    
    
    if user:
        # Authentication successful, render the "updation.html" template
        return render_template("updation.html")
    else:
        # Authentication failed, render the "loginerror.html" template
        return redirect(url_for('retry'))



@app.route('/2ndpage')
def IIndpage():
    return render_template("2ndpage.html")


if __name__=='__main__':
    app.run(debug=True)