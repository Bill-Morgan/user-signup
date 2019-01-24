from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

def isvalidemail_re(email):
    dot_valid = (len(list(re.findall(r'\.', email)))) == 1
    at_valid = (len(list(re.findall(r'\@',email)))) == 1
    return (((dot_valid and at_valid and isvalidstr_re(email)) or len(email) == 0))

def isvalidstr_re(instr):
    return (re.fullmatch(r'\S{3,20}', instr))

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        vpassword = request.form['vpassword']
        email = request.form['email']
        username_error=''
        password_error=''
        vpassword_error=''
        email_error=''
        if not isvalidstr_re(username):
            username_error = "That's not a valid username"
            username = ''
        if not isvalidstr_re(password):
            password_error = " That's not a valid password"
        if not password == vpassword:
            vpassword_error = "Passwords don't match"
        if not isvalidemail_re(email):
            email_error = "That's not a valid email"
            email = ''
        if not (username_error or password_error or vpassword_error or email_error):
            return redirect("/welcome?username={}".format(username))
        return render_template('form.html', username=username, username_error=username_error, password_error=password_error, vpassword_error=vpassword_error, email=email, email_error=email_error, title='Signup')    
    return render_template('form.html', title='Signup')

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username, title='Welcome')

app.run()