from flask import Flask, render_template, request, url_for
import random


app = Flask(__name__)




@app.route('/')
def eightballapp():
    return render_template('index.html',eightballanswer = url_for('eightballanswer'))

@app.route('/eightballanswer', methods=["GET", "POST"])
def eightballanswer():
    if request.method == "POST":
        outputList = ["Yes", "No", "Maybe so"]
        return render_template('answer.html', randomText = outputList[random.randint(0,2)])
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

