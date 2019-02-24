from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def htmlWebpage():
	return render_template('Checkerboard_Static.html')

@app.route('/<numberString1>/<numberString2>')
def numberWebpage(numberString1=None, numberString2=None):
	numberInteger1 = int(numberString1)
	numberInteger2 = int(numberString2)
	return render_template('Checkerboard_Dynamic.html', numberInteger1=numberInteger1, numberInteger2=numberInteger2)

if __name__=="__main__":
    app.run(debug=True)