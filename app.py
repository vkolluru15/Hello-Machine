from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)
hostname = 'mymldbinstance.cwfpdkanfj9a.us-west-1.rds.amazonaws.com'
username = 'scientist'
password = 'Experiments'
database = 'MLDB_01'

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "select dteday, temp, atemp,hum,windspeed from day" )
    data = cur.fetchall()
    return data

@app.route('/showData')
def showData():
    myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    data = doQuery( myConnection )
    myConnection.close()
    return render_template('showdata.html', data=data)

@app.route('/')
def showHello():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()
