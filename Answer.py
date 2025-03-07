from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def return_planet_name(planet_name):
    results = ['На ней много необходимых ресурсов;',
               'На ней есть вода и атмосфера;',
               'На ней есть небольшое магнитное поле',
               'Наконец, она просто красива!']
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1> Мое предложение: {planet_name}</h1>
                    <h3> Эта планета близка к Земле; </h3>
                    <div class="alert alert-success" role="alert">
                        <h3>{results[0]}</h3>
                    </div>
                     <div class="alert alert-dark" role="alert">
                        <h3>{results[1]}</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                        <h3>{results[2]}</h3>
                    </div>
                    <div class="alert alert-danger" role="alert">
                        <h3>{results[3]}</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')