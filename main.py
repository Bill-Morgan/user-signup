from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

def isvalidemail_re(email):
    dots = re.compile(r'\.')
    ats = re.compile(r'\@')
    dot_count = len(list(dots.finditer(email)))
    ats_count = len(list(ats.finditer(email)))
    return (((dot_count == 1 and ats_count == 1 and isvalidstr_re(email)) or len(email) == 0))

def isvalidstr_re(instr):
    nonchars = re.compile(r'\s')
    nonchars_count = len(list(nonchars.finditer(instr)))
    chars = re.compile(r'.')
    char_count = len(list(chars.finditer(instr)))
    return (char_count >= 3 and char_count <= 20 and nonchars_count == 0)

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