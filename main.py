from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def isvalidstr(instr):
    return (len(instr) >= 3 and len(instr) <= 20 and not (' ' in instr))

def isvalidemail(email):
    return (email.count('.') == 1 and email.count('@') == 1 and isvalidstr(email))

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username_error=''
        password_error=''
        vpassword_error=''
        email_error=''
        username = request.form['username']
        password = request.form['password']
        vpassword = request.form['vpassword']
        email = request.form['email']
        if not isvalidstr(username):
            username_error = "Username Error"
        if not isvalidstr(password):
            password_error = "Password Error"
        if not password == vpassword:
            vpassword_error = "Passwords do not match"
        if not isvalidemail(email):
            email_error = "Email Error"
        return render_template('form.html', username=username, username_error=username_error, password_error=password_error, vpassword_error=vpassword_error, email=email, email_error=email_error)    
    return render_template('form.html')


app.run()

