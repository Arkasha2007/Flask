from flask import Flask, url_for

app = Flask(__name__)


@app.route('/carousel')
def form_sample():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                            <title>Пейзажи Марса</title>
                          </head>
                          <body>
                              <div id="carouselExample" class="carousel slide">
                                  <div class="carousel-inner">
                                    <div class="carousel-item active">
                                      <img src="{url_for('static', filename='img/Mars_foto_1.jpg')}" class="d-block w-100" alt="...">
                                    </div>
                                    <div class="carousel-item">
                                      <img src="{url_for('static', filename='img/Mars_foto_2.jpg')}" class="d-block w-100" alt="...">
                                    </div>
                                    <div class="carousel-item">
                                      <img src="{url_for('static', filename='img/Mars_foto_3.jpg')}" class="d-block w-100" alt="...">
                                    </div>
                                  </div>
                                  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Previous</span>
                                  </button>
                                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span class="visually-hidden">Next</span>
                                  </button>
                              </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
