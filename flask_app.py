from flask import Flask, render_template, make_response, url_for
from datetime import datetime

DEBUG = True
HOST = '127.0.0.1'
PORT = 8080

app = Flask(__name__)


def getStudents():
    with open("students.csv", "r") as file:
        contents = file.readlines()
        students = []
        for names in contents:
            item = names.split(',')
            students.append(item)
            # print(students)
    return students


@app.route('/')
def home():
    date = datetime.utcnow()
    date_string = date.strftime('%d/%m/%Y')
    students = getStudents()
    # remove the Table data column Names in CSV file
    del students[0]
    return render_template('home.html', date=date_string, students=students)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
