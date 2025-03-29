from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form():
    return render_template('First_file.html')


@app.route('/auto_answer', methods=['GET', 'POST'])
@app.route('/answer', methods=['GET', 'POST'])
def answer():
    return render_template('index.html', say=request.form['surname'], title=request.form['name'],
                           education=request.form['student_courses'], profession=request.form['user_profession'],
                           sex=request.form['user_age'], motivation=request.form['student_bio'],
                           ready=request.form['approval'])


if __name__ == '__main__':
    app.run()
