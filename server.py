
import os
import sqlite3
import json
from flask import Flask, redirect, request, render_template, jsonify, url_for

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/", methods=['GET'])
def mainPage():
    if request.method == "GET":
        mentors = []
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()
            #selects all rows from db to display them
            cur.execute('SELECT * FROM ApprovedMentors')
            mentors = cur.fetchall()

        except sqlite3.Error as error:
            app.logger.error("Error: %s", error)


        finally:              
            con.close()
            print("connection closed")

            return render_template('mentorCreditHome.html', data = mentors)
       
@app.route("/Register-page.html",  methods=["GET","POST"])
def registerPage():
    if request.method == "GET":
        return render_template("Register-page.html")
    elif request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['pass']
        phoneNumber = request.form['phoneNumber']
        LinkedIn = request.form['LinkedIn']
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()

            #insert values query and commit to db
            cur.execute('INSERT INTO Users ("Email", "Password", "First Name", "Last Name", "Phone Number","LinkedIn") VALUES (?, ?, ?, ?, ?,?)',
            (email, password, fname, lname, phoneNumber,LinkedIn))
            con.commit()
            

            #check for successful insert into table
            query = ('SELECT * FROM Users WHERE Email=?')
            res = cur.execute(query, (email,))

            if res.fetchone() is not None:
                print("successful")
            else:
                print("unsuccessful")
  
        except sqlite3.Error as e:
            print("error in saving to database: ", e)
        finally:
            con.close()
            print("connection closed")
    return render_template("mentorCreditHome.html")
        

@app.route("/login_page.html", methods=["GET","POST"])
def loginPage():
    if request.method == 'GET':
        return render_template("login_page.html")
    elif request.method == "POST":
        email = request.form['emailInput']
        password = request.form['passwordInput']
    try:
        con = sqlite3.connect("mentoring.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Moderator WHERE Email = ? AND Password = ?", (email, password))
        modDetails = cur.fetchone()
        if modDetails:
            print("Successful mod Login")
            #Reference: https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
            return redirect(url_for('moderatorPage'))
        cur.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))
        details = cur.fetchall()
        print(f"details: {details}")
        if details:
            print("Successful user Login")
        else:
            print("Unsuccessful user Login")
    except sqlite3.Error as e:
        print("Error in accessing the database:", e)
    finally:
        con.close()
    return render_template("login_page.html")

@app.route("/moderator_page.html", methods=["GET","POST"])
def moderatorPage():
    if request.method == 'GET':
        mentors = []
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()
            #selects all rows from db to display them
            cur.execute('SELECT * FROM PendingMentors')
            mentors = cur.fetchall()
        except sqlite3.Error as error:
            app.logger.error("Error: %s", error)
        finally:              
            con.close()
            print("connection closed")

            return render_template('moderator_page.html', data = mentors)

    elif request.method == "POST":
        poolName = request.form['nameInput']
        poolDescription = request.form['descriptionInput']
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()

            #insert values query
            cur.execute('INSERT INTO Pools ("Name", "Description") VALUES (?, ?)',
            (poolName, poolDescription))

            con.commit()
            
        except sqlite3.Error as e:
            print("Error in saving to database", e)
        finally:
            con.close()
            print("connection closed")
    return redirect(url_for('moderatorPage'))

@app.route("/approve_mentor", methods=["POST"])
def approveMentor():
    if request.method == "POST":   
        userId = request.form.get("userId")
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()

            # Get the details of the mentee who applied to be a mentor
            cur.execute("SELECT * FROM PendingMentors WHERE UserID=?", (userId,))
            mentorDetails = cur.fetchone()
            print(f"Mentor details: {mentorDetails}")

            # Move said mentee into a table for approved mentors
            cur.execute("INSERT INTO ApprovedMentors (UserID, Name) VALUES (?, ?)",
                        (mentorDetails[0], mentorDetails[2]))

            # Delete said mentee from the table where their information was fetched from
            cur.execute("DELETE FROM PendingMentors WHERE UserID=?", (userId,))

            con.commit()
        except sqlite3.Error as e:
            print("Error:", e)
        finally:
            con.close()
            print("Successful Approval")
        return("W")

@app.route("/reject_mentor", methods=["POST"])
def rejectMentor():
    if request.method == "POST":   
        userId = request.form.get("userId")
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()

            # Get the details of the mentee who applied to be a mentor
            cur.execute("SELECT * FROM PendingMentors WHERE UserID=?", (userId,))
            mentorDetails = cur.fetchone()
            print(f"Mentor details: {mentorDetails}")

            # Delete said mentee from PendingMentors table
            cur.execute("DELETE FROM PendingMentors WHERE UserID=?", (userId,))

            con.commit()
        except sqlite3.Error as e:
            print("Error:", e)
        finally:
            con.close()
        return("W")

@app.route("/Account_page.html", methods=["GET","POST"])
def accountPage():
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        cur.execute("SELECT FirstName, LastName, Email, Description FROM Users")

        data = cur.fetchall()
        conn.close()

        return render_template("Account_page.html", user=data)
    except sqlite3.Error as e:
        return "An error has occurred: {}".format(str(e))
   
    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

@app.route("/mentor_registration.html", methods=["GET", "POST"])
def mentorRegisterPage():
    if request.method == "GET":
        return render_template("mentor_registration.html")
    elif request.method == "POST":
        email = request.form['email']
        description = request.form['description']
        selected_tags = request.form.getlist("tags")       
        try:
            con = sqlite3.connect("mentoring.db")
            cur = con.cursor()

            cur.execute("INSERT INTO PendingMentors (Email, Description) VALUES (?, ?)", (email, description,))
            con.commit()

            print("Successful")
            #checks if user is in the database by email
            #need to adjust once pending mentor table is finalised
            #as should be checking for mentor status
            cur.execute("SELECT UserID FROM Users WHERE Email = ?", (email,))
            row = cur.fetchone()
            if row:
                user_id = row[0]
                tags_json = json.dumps(selected_tags)
                #checks if the image was uploaded               
                if 'mentorImage' in request.files:
                    file = request.files['mentorImage']
                    #print statements for debugging, still need
                    print(request.files)
                    print(file)
                    print("Is file allowed?", allowed_file(file.filename))
                    #refers to function to see if file is valid
                    if file and allowed_file(file.filename):
                        # read the contents of the file into image_data
                        image_data = file.read()
                        # convert to binary using sqlite3.Binary
                        blob = sqlite3.Binary(image_data)
                        #for debugging purposes
                        print("Image Data Length:", len(image_data))
                        cur.execute("INSERT INTO PendingMentors (Email, UserID, Description, Tags, Image) VALUES (?, ?, ?, ?, ?)",
                                    (user_id, email, description, tags_json, blob))                                              
                        con.commit()                       
                        print("Successful")                       
                    else:
                        print("Invalid file or file type not allowed")                       
        except sqlite3.Error as e:
            print("SQLite Error:", e)
            return 'Error in saving to the database'
        finally:
            con.close()
            print("Connection closed")
            
        return render_template("mentor_registration.html")

if __name__ == "__main__":
    app.run(debug=True)