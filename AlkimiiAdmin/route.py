from flask import Flask, url_for, request, render_template, redirect;
from app import app;
import pypyodbc;
from models.connection import SqlConnection;

    
@app.route('/')
def home():
 
    return render_template("Home.html");

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return render_template("AdminLogin.html");
    elif request.method == 'POST':
        username = request.form['Username'];
        password = request.form['Password'];
        if username == "TestUser" and password == "TestPassword":
            return redirect(url_for('display'))
        else: 
            return "<h2>Error</h2>"

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template("UserLogin.html")
    elif request.method == 'POST':
        try:
            #myConnection = pypyodbc.connect('Driver={SQL Server};'
            #                    'Server=SIMON-HP\SQLEXPRESS;'
            #                    'Database=AlkimiiAdmin;'
            #                    'uid=sa;pwd=12345')

            #myCursor = myConnection.cursor()
            UserId = request.form['UserID'];
            Password = request.form['Password'];
            con = SqlConnection();
            con.userLogin(UserId, Password)
            #SQLCommand = ("SELECT * FROM Users "
            #          "WHERE UsererId = '" + UserId +
            #          "' AND Pword = '" + Password + "'")

            #myCursor.execute(SQLCommand)
            #myConnection.commit();
            #myConnection.close();
            return render_template("UserHome.html");
        except:
            return "<h2>Wrong details entered</h2>"

@app.route('/display', methods=['GET', 'POST'])
def display():
    if request.method == 'GET':
        myConnection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=SIMON-HP\SQLEXPRESS;'
                                'Database=AlkimiiAdmin;'
                                'uid=sa;pwd=12345')
        myCursor = myConnection.cursor()
        myCursor.execute("SELECT * FROM Users")
        rows = [dict(id=row[0], name=row[1], email=row[2], password=row[3]) for row in myCursor.fetchall()]
        return render_template("DisplayAll.html", rows = rows)
        myConnection.close();
    else:
        return"<h2>Error</h2>"

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        try:
            return render_template("Add.html");
        except:
            return "<h2>Error in the get</h2>"
    elif request.method == 'POST':
        try:
            myConnection = pypyodbc.connect('Driver={SQL Server};'
                                    'Server=SIMON-HP\SQLEXPRESS;'
                                    'Database=AlkimiiAdmin;'
                                    'uid=sa;pwd=12345')
            myCursor = myConnection.cursor()

            name = request.form['AddName'];
            email = request.form['AddEmail'];
            password = request.form['AddPassword'];

            SQLCommand = ("INSERT INTO Users "
                        "(Name, Email, Pword) "
                        "VALUES (?,?,?)")
            values = [name, email, password]

            myCursor.execute(SQLCommand,values)
            myConnection.commit();
            myConnection.close();
            return redirect(url_for('display'));
        except:
            return "<h2>Error Occurred</h2>"

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        return render_template("Delete.html");
    elif request.method == 'POST':
        try:
            myConnection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=SIMON-HP\SQLEXPRESS;'
                                'Database=AlkimiiAdmin;'
                                'uid=sa;pwd=12345')
            myCursor = myConnection.cursor()
            DeleteId = request.form['DeleteId'];

            SQLCommand = ("DELETE FROM Users "
                      "WHERE UsererId = "
                      + DeleteId)

            myCursor.execute(SQLCommand)
            myConnection.commit();
            myConnection.close();
            return redirect(url_for('display'));
        except:
            return "<h2>Error Occurred</h2>"


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template("Edit.html");
    elif request.method == 'POST':
        try:
            myConnection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=SIMON-HP\SQLEXPRESS;'
                                'Database=AlkimiiAdmin;'
                                'uid=sa;pwd=12345')
            myCursor = myConnection.cursor()
            Name = request.form['EditName'];
            Email = request.form['EditEmail'];
            Password = request.form['EditPassword'];
            EditId = request.form['EditId'];

            SQLCommand = ("UPDATE Users "
                      "SET Name = '" + Name +
                      "', Email = '" + Email +
                      "', Pword = '" + Password +
                      "' WHERE UsererId = "
                      + EditId)

            myCursor.execute(SQLCommand)
            myConnection.commit();
            myConnection.close();
            return redirect(url_for('display'));
        except:
            return "<h2>Error Occurred</h2>"

