from flask import Flask, render_template, request, redirect, url_for
from dbms_func.Dbms import Dbms_tools
import os
from forms import DonorForm
import secrets
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
DBMS = Dbms_tools()
DBMS_CONNECT = DBMS.connection
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET'])
def index():
    message = ""
    if (request.method == 'GET'):
        if (DBMS_CONNECT.is_connected()):
            data = DBMS.get_basic()
            return render_template('index.html', data=data)
        message = "Database no connected"
        return render_template('index.html', data=data, message=message)

@app.route('/add', methods=['GET', 'POST'])
def add_view():
    form = DonorForm()
    if (form.validate_on_submit()):
        DBMS.save_all(
            form.name.data, 
            form.address.data, 
            form.phone_no.data, 
            form.type.data)
        return redirect('/add')
    return render_template('add.html', form=form)
    

if __name__ == "__main__":
    app.run()