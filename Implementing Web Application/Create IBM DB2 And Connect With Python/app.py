from turtle import st

import ibm_db
from flask import Flask, redirect, render_template, request, session, url_for
from markupsafe import escape


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT= 32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hry80177;PWD=hsNGkee9wToP2Hm4",'','')

app = Flask(__name__, template_folder='template')

@app.route("/")
def SignIn():
    return render_template('Sign-In.html')

    

@app.route("/Sign-Up")
def SignUp():
    return render_template('Sign-Up.html') 

@app.route("/Home")
def Home():
    return render_template('Home.html') 

@app.route("/Employee")
def Employee():
    return render_template('Employee.html') 

@app.route("/Supplier")
def Supplier():
    return render_template('Supplier.html') 

@app.route("/Products")
def Products():
    return render_template('Products.html') 

@app.route("/Sales")
def Sales():
    return render_template('Sales.html')
       
@app.route('/empdata',methods = ['POST', 'GET'])
def empdata():
  if request.method == 'POST':

    EmployeeNO = request.form['employeeno']
    Name = request.form['name']
    Gender = request.form['gender']
    Contact = request.form['contact']

    sql = "SELECT * FROM Employee WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,EmployeeNO)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    insert_sql = "INSERT INTO Employee VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, EmployeeNO)
    ibm_db.bind_param(prep_stmt, 2, Name)
    ibm_db.bind_param(prep_stmt, 3, Gender)
    ibm_db.bind_param(prep_stmt, 4, Contact)
    ibm_db.execute(prep_stmt)
    
    return render_template('Employee.html', msg="Employee Data saved successfuly..")

@app.route('/empdata')
def empdata():
  Employee = []
  sql = "SELECT * FROM Employee"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    Employee.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if Employee:
    return render_template("Employee.html", Employee = Employee)

@app.route('/delete/<name>')
def delete(name):
  sql = f"SELECT * FROM Employee WHERE name='{escape(name)}'"
  print(sql)
  stmt = ibm_db.exec_immediate(conn, sql)
  Employee = ibm_db.fetch_row(stmt)
  print ("The Name is : ",  Employee)
  if Employee:
    sql = f"DELETE FROM Employee WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)

    Employee = []
    sql = "SELECT * FROM Employee"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      Employee.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if Employee:
      return render_template("empdata.html", Employee = Employee, msg="Delete successfully")


  
  # # while User != False:
  # #   print ("The Name is : ",  User)

  # print(student)
  return "success..."

@app.route('/supplierdata',methods = ['POST', 'GET'])
def supplierdata():
  if request.method == 'POST':

    InvoiceNo = request.form['invoiceno']
    SupplierName  = request.form['suppliername']
    Contact = request.form['contact']
    Description = request.form['description']

    sql = "SELECT * FROM Supplier WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,InvoiceNo)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    insert_sql = "INSERT INTO Supplier VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, InvoiceNO)
    ibm_db.bind_param(prep_stmt, 2, SupplierName)
    ibm_db.bind_param(prep_stmt, 3, Contact)
    ibm_db.bind_param(prep_stmt, 4, Description)
    ibm_db.execute(prep_stmt)
    
    return render_template('Supplier.html', msg="Supplier Data saved successfuly..")

@app.route('/supplierdata')
def supplierdata():
  Supplier = []
  sql = "SELECT * FROM Supplier"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    Supplier.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if Supplier:
    return render_template("Supplier.html", Supplier = Supplier)

@app.route('/delete/<name>')
def delete(name):
  sql = f"SELECT * FROM Supplier WHERE name='{escape(name)}'"
  print(sql)
  stmt = ibm_db.exec_immediate(conn, sql)
  Supplier = ibm_db.fetch_row(stmt)
  print ("The Name is : ",  Supplier)
  if Supplier:
    sql = f"DELETE FROM Supplier WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)

    Supplier = []
    sql = "SELECT * FROM Supplier"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      Supplier.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if Supplier:
      return render_template("supplierdata.html", Supplier = Supplier, msg="Delete successfully")


  
  # # while User != False:
  # #   print ("The Name is : ",  User)

  # print(student)
  return "success..."

@app.route('/productsdata',methods = ['POST', 'GET'])
def productsdata():
  if request.method == 'POST':

    Name = request.form['name']
    Price = request.form['price']
    QTY = request.form['qty']
    Status = request.form['status']

    sql = "SELECT * FROM Products WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,Name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    insert_sql = "INSERT INTO Products VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, Name)
    ibm_db.bind_param(prep_stmt, 2, Price)
    ibm_db.bind_param(prep_stmt, 3, QTY)
    ibm_db.bind_param(prep_stmt, 4, Status)
    ibm_db.execute(prep_stmt)
    
    return render_template('Products.html', msg="Products Data saved successfuly..")

@app.route('/productsdata')
def productsdata():
  Products = []
  sql = "SELECT * FROM Products"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    Products.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if Products:
    return render_template("Products.html", Products = Products)

@app.route('/delete/<name>')
def delete(name):
  sql = f"SELECT * FROM Products WHERE name='{escape(name)}'"
  print(sql)
  stmt = ibm_db.exec_immediate(conn, sql)
  Products = ibm_db.fetch_row(stmt)
  print ("The Name is : ",  Products)
  if Products:
    sql = f"DELETE FROM Products WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)

    Products = []
    sql = "SELECT * FROM Products"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      Products.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if Products:
      return render_template("Products.html", Products = Products, msg="Delete successfully")


  
  # # while User != False:
  # #   print ("The Name is : ",  User)

  # print(student)
  return "success..."


if __name__=="__main__":
    app.run(debug=True)
         