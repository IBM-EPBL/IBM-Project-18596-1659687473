from flask import Flask, render_template, request, redirect, url_for, session

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
       



if __name__=="__main__":
    app.run(debug=True)
         