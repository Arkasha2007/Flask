from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def odd_even(prof):
    return render_template('index.html', username=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
