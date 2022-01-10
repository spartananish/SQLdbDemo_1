from flask import Flask
from flask_mysqldb import  MySQL
import  mysql.connector as connection
# Creating Connection
from flask import  jsonify, request


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'student'

mysql = MySQL(app)



# def helper():
#     try:
#         mydb = connection.connect(host='localhost', user='root', passwd='root', use_pure=True)
#         cursor = mydb.cursor()
#         return cursor
#     except Exception as e:
#         print(str(e))

# Add New Entry
@app.route('/insert',methods=['POST'])
def insert():
    cursor = mysql.connection.cursor()
    # mysql_query_db ='use student'
    # cursor.execute(mysql_query_db)
    _json = request.json
    _personID = int(_json['personId'])
    _lastName = _json['lastName']
    _firstName = _json['firstName']
    _address = _json['address']
    _city = _json['city']
    try:
        if _personID and _lastName and _lastName and _firstName and _address and _city and request.method == "POST":
            # mysql_query_insert = 'insert into Student values (_personID,_lastName,_firstName,_address,_city)'
            cursor.execute("INSERT INTO student (PersonID,LastName,FirstName,Address,City ) VALUES (%s,%s,%s,%s,%s)" , (_personID , _lastName, _firstName, _address, _city))
            mysql.connection.commit()
            cursor.close()
            resp = jsonify("user Added successfully")
            resp.status_code = 200
        else:
            return not_found()
    except Exception as e:
        print(str(e))
        print(e.with_traceback())


# Return Data on the basis of Person Id
@app.route('/selectbyid',methods=['POST'])
def selectById():
    cursor = mysql.connection.cursor()
    _json = request.json
    _personID= int(_json['personId'])
    # data = None
    try:
        if _personID and request.method == "POST":
            cursor.execute("SELECT * FROM  STUDENT WHERE PersonID = _personID")
            resp = jsonify(cursor.fetchall())
            resp.status_code = 200
        else:
            return  not_found()
    except Exception as e:
        print(str(e))
        print(e.with_traceback())


#Return all data present in DB
@app.route('/selectAll',methods=['POST'])
def selectAll():
    cursor = mysql.connection.cursor()
    try:
        if request.method == "POST":
            cursor.execute("SELECT * FROM student")
            resp = jsonify(cursor.fetchall())
            resp.status_code = 200
        else:
            return not_found()
    except Exception as e:
        print(str(e))
        print(e.with_traceback())


#Delete data on the basic of PersonID
@app.route("/delete",methods = ['DELETE'])
def delete():
    cursor = mysql.connection.cursor()
    _json = request.json
    _personId = _json['personId']
    try:
        if _personId and request.method == 'DELETE':
            cursor.execute("DELETE FROM STUDENT WHERE PersonID = _personId ")
            resp = jsonify("Date deleted Successfully")
            resp.status_code = 200
        else:
            return not_found()
    except Exception as e:
        print(str(e))
        print(e.with_traceback())


# Updating Data for the paticular ID
@app.route("/update",methods=['UPDATE'])
def update():
    cursor = mysql.connection.cursor()
    _json = request.json
    _personId = _json['personId']
    try:
        if _personId and request.method == 'UPDATE':
            cursor.execute("UPDATE STUDENT SET lastName = 'Danile' where PersonID = _personId")
            resp = jsonify('Updated Successfully')
            resp.status_code=200
        else:
            return not_found()
    except Exception as e:
        print(str(e))
        print(e.with_traceback())


def not_found():
    message = {
            'status' : 404,
            'message' : ' Not Found'+request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


# To run or APP
if __name__ == "__main__":
    app.run(debug=True)


