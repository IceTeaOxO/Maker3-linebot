from flask import Flask, render_template, request
import sqlite3 as sql
import sqlite3
app = Flask(__name__)
# conn = sqlite3.connect('database.db')
# print "Opened database successfully";

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print "Table created successfully";
# conn.close()
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
       try:
          nm = request.form['nm']
          addr = request.form['add']
          city = request.form['city']
          pin = request.form['pin']

          with sql.connect("database.db") as con:
             cur = con.cursor()

             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )

             con.commit()
             msg = "Record successfully added"
       except:
          con.rollback()
          msg = "error in insert operation"

       finally:
            con.close()
            return render_template("result.html",msg = msg)
          

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html",rows = rows)

@app.route('/init')
def init():
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print ("Table created successfully")
    conn.close()
    return None

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug = True)