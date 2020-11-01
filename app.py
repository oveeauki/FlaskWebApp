from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')
@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return dashboard()

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'toor' and request.form['username'] == 'admin':
		session['logged_in'] = True
		return dashboard()
	elif request.form['password'] == 'ok' and request.form['username'] == 'ok':
		session['logged_in'] = True
		return dashboard()
	else:
		return render_template('fail.html')

@app.route("/dashboard")
def dashboard():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('dashboard.html')

@app.route("/profile")
def profile():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('profile.html')

@app.route("/sami")
def sami():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:	
		return render_template("sami.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/chat")
def chat():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template("chat.html")

@app.route("/xqcl")
def xqcl():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:	
		return render_template("xqcl.html")

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=4000)  