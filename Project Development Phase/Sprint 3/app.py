from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=blk20068;PWD=LsEEBW71f9uXFNsf",'','')

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

@app.route("/Employee-Data")
def EmployeeData():
    return render_template('Employee-Data.html')

@app.route("/Supplier")
def Supplier():
    return render_template('Supplier.html') 

@app.route("/Supplier-Data")
def SupplierData():
    return render_template('Supplier-Data.html')

@app.route("/Products")
def Products():
    return render_template('Products.html') 

@app.route("/Products-Data")
def ProductsData():
    return render_template('Products-Data.html')

@app.route("/Sales")
def Sales():
    return render_template('Sales.html')


@app.route('/Employee-Data')
def Employeedata():
  return render_template('Employee-Data.html')

@app.route('/addemployee')
def new_employee():
  return render_template('add_employee.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['employeeno']
    address = request.form['name']
    city = request.form['gender']
    pin = request.form['contact']

    sql = "SELECT * FROM employee WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('employee.html')
    else:
      insert_sql = "INSERT INTO Employee VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, employeeno)
      ibm_db.bind_param(prep_stmt, 2, name)
      ibm_db.bind_param(prep_stmt, 3, gender)
      ibm_db.bind_param(prep_stmt, 4, contact)
      ibm_db.execute(prep_stmt)
    
    return render_template('employee.html', msg="Employee Data saved successfuly..")

@app.route('/Employee')
def Employee():
  Employee = []
  sql = "SELECT * FROM Employee"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    Employee.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if Employee:
    return render_template("Emplyee-Data.html", Employee = Employee)

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
      return render_template("Employee-Data.html", Employee = Employee, msg="Delete successfully")


      
  
  # # while student != False:
  # #   print ("The Name is : ",  student)

  # print(student)
  return "success..."

# @app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
    
#     post = BlogPost.query.get_or_404(id)

#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.author = request.form['author']
#         post.content = request.form['content']
#         db.session.commit()
#         return redirect('/posts')
#     else:
#         return render_template('edit.html', post=post)


@app.route('/Supplier-Data')
def Supplierdata():
  return render_template('Supplier-Data.html')

@app.route('/addsupplier')
def new_supplierdata():
  return render_template('add_supplier.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['invoiceno']
    address = request.form['name']
    city = request.form['contact']
    pin = request.form['description']

    sql = "SELECT * FROM supplier WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('supplier.html')
    else:
      insert_sql = "INSERT INTO Employee VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, invoiceno)
      ibm_db.bind_param(prep_stmt, 2, name)
      ibm_db.bind_param(prep_stmt, 3, contact)
      ibm_db.bind_param(prep_stmt, 4, description)
      ibm_db.execute(prep_stmt)
    
    return render_template('supplier.html', msg="supplier Data saved successfuly..")

@app.route('/Supplier')
def supplier():
  supplier = []
  sql = "SELECT * FROM Supplier"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    supplier.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if supplier:
    return render_template("Supplier-Data.html", Supplier = Supplier)

@app.route('/delete/<name>')
def delete(name):
  sql = f"SELECT * FROM supplier WHERE name='{escape(name)}'"
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
      return render_template("Supplier-Data.html", Supplier = Supplier, msg="Delete successfully")


      
  
  # # while student != False:
  # #   print ("The Name is : ",  student)

  # print(student)
  return "success..."

# @app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
    
#     post = BlogPost.query.get_or_404(id)

#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.author = request.form['author']
#         post.content = request.form['content']
#         db.session.commit()
#         return redirect('/posts')
#     else:
#         return render_template('edit.html', post=post)


@app.route('/Products-Data')
def Productsdata():
  return render_template('Products-Data.html')

@app.route('/addproducts')
def new_productsdata():
  return render_template('add_products.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['name']
    address = request.form['price']
    city = request.form['QTY']
    pin = request.form['status']

    sql = "SELECT * FROM Products WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('products.html', )
    else:
      insert_sql = "INSERT INTO Supplier VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, price)
      ibm_db.bind_param(prep_stmt, 3, QTY)
      ibm_db.bind_param(prep_stmt, 4, status)
      ibm_db.execute(prep_stmt)
    
    return render_template('products.html', msg="supplier Data saved successfuly..")

@app.route('/Products')
def Products():
  Products = []
  sql = "SELECT * FROM Products"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    Products.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if supplier:
    return render_template("Products-Data.html", Products = Products)

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
    sql = "SELECT * FROM Supplier"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
      Products.append(dictionary)
      dictionary = ibm_db.fetch_both(stmt)
    if Products:
      return render_template("Products-Data.html", Supplier = Supplier, msg="Delete successfully")


      
  
  # # while student != False:
  # #   print ("The Name is : ",  student)

  # print(student)
  return "success..."

# @app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
    
#     post = BlogPost.query.get_or_404(id)

#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.author = request.form['author']
#         post.content = request.form['content']
#         db.session.commit()
#         return redirect('/posts')
#     else:
#         return render_template('edit.html', post=post)

       



if __name__=="__main__":
    app.run(debug=True)
         