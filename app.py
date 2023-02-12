from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
import os
#print(app.template_folder)
print("python Flask code is looking for webpage templates here:", os.path.abspath(app.template_folder))

import sys
print("python libraries are searched in this order in these folders :",sys.path)

print("pythonpath env variable value: ",os.environ.get('PYTHONPATH'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']

    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, number])

    return redirect('/search')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_name = request.form['search_name']
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == search_name:
                    return render_template('search.html', search_result=row[1])
        return render_template('search.html', search_result=None)
    return render_template('search.html', search_result=None)

if __name__ == '__main__':
    app.run()
