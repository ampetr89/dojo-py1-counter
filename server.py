from flask import Flask, render_template, request, redirect, session

print('starting')
app = Flask(__name__)
secretKey = open('secret-key.txt', 'r').read().strip()
app.secret_key = secretKey

def fmtnum(n):
	# starting with 0th, 1st, 2nd.. 
	sufs = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
	if n % 100 in [11, 12, 13]:
		sufnum = 0
	else:
		sufnum = n % 10
	return str(n)+sufs[sufnum]

@app.route('/')
def index():
	try:
		session['n'] += 1
	except:
		session['n'] = 1 # start counting visits at 1

	
	return render_template('index.html', counter=fmtnum(session['n']))

@app.route('/plus2')
def plus2():
	try:
		session['n'] += 1 # add one, because when it redirects, it will get another added
	except:
		session['n'] = 1

	return redirect('/')


@app.route('/reset')
def reset():
	
	session['n'] = 0 # when it redirects, it will get another added
	
	return redirect('/')

app.run(debug=True)
