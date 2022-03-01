import sqlite3 as sql
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addView')
def addView():
    return render_template("add.html")

@app.route('/addRec',methods=['POST','GET'])
def addRec():
    if(request.method=='POST'):
        try:
            nm=request.form["nm"]
            rn=request.form["rn"]

            with sql.connect('student.db') as con:
                cur=con.cursor()
                cur.execute("insert into students (regNo,name) values (?,?)",(rn,nm))
                con.commit()
                msg="record has been successfully inserted into the table"
        
        except:
            con.rollback()
            msg="error occured in the insertion of the record"

        finally:
            print(msg)
            return render_template("result.html",msg=msg)
            con.close()


@app.route('/list')
def display():
    con=sql.connect('student.db')
    con.row_factory = sql.Row
    cur=con.cursor()
    cur.execute('select * from students')
    rows=cur.fetchall()
    for i in rows:
        print(i['name'])
        print(i[0])
    return render_template("list.html",rows=rows)

@app.route('/delView')
def delView():
    return render_template("delete.html")

@app.route('/delete',methods=['GET'])
def delete():
    try:
        rn=request.args.get('rn')
        con=sql.connect('student.db')
        cur=con.cursor()
        s='delete from students where regNo=?'
        cur.execute(s,(rn,))
        print(rn)
        con.commit()
        msg="the record has been successfully deleted"
    except:
        con.rollback()
        msg="error occured"
    return render_template("delResult.html",msg=msg)


if __name__==('__main__'):
    app.run(debug=True)
