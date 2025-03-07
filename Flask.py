from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!<h1>'




@app.route('/promotion_image')
def return_sample_page():
    results = ['Человечество вырастает из детства.',
               'Человечеству мала одна планета.',
               'Мы сделаем обитаемыми безжизненные пока планеты.',
               'И начнем с Марса!',
               'Присоединяйся!']
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
                    <h1 style="color:#DC143C;">Жди нас, Марс!</h1>
                    <img src="/static/img/Mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                        <h3>{results[0]}</h3>
                    </div>
                     <div class="alert alert-success" role="alert">
                        <h3>{results[1]}</h3>
                    </div>
                    <div class="alert alert-dark" role="alert">
                        <h3>{results[2]}</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                        <h3>{results[3]}</h3>
                    </div>
                    <div class="alert alert-danger" role="alert">
                        <h3>{results[4]}</h3>
                    </div>
                  </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
