from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def isvalidstr(instr):
    return (len(instr) >= 3 and len(instr) <= 20 and not (' ' in instr))

def isvalidemail(email):
    return ((email.count('.') == 1 and email.count('@') == 1 and isvalidstr(email) or len(email) == 0)) 

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
        if not isvalidstr(username):
            username_error = "That's not a valid username"
            username = ''
        if not isvalidstr(password):
            password_error = " That's not a valid password"
        if not password == vpassword:
            vpassword_error = "Passwords don't match"
        if not isvalidemail(email):
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

