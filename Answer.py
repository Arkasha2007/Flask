from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Агента претендента</h1>
                            <h3 align="center"> на участие в миссии</h3>
                            <div>
                                <form  class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" aria-describedby="emailHelp" placeholder="Введите фамилию" name="text">
                                    <input type="text" class="form-control" id="text_2" placeholder="Введите имя" name="text">
                                    <div class="text-block">  
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email"> 
                                    </div>
                                    <div class="text-block2"> 
                                    <label>Какое у Вас образование?</label>
                                    </div>
                                    <div class="sub-title"> 
                                    <select class='box' name="student_courses">
                                        <option value="Начальное">Начальное</option>
                                        <option value="Среднее">Среднее</option>
                                        <option value="Высшее">Высшее</option>
                                    </select>
                                    </div>
                                    <div class="text-block3">
                                    <label>Какие у Вас есть профессии?</label>
                                    </div>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Инженер-исследователь</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Пилот</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Строитель</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Экзобиолог</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Врач</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Инженер по терраформированию</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Метеоролог</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Киберинженер</label><br>
                                    <input type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Пилот дронов</label><br>
                                    <div class="text-block3">
                                    <label>Укажите пол</label>
                                    </div>
                                    <input type="radio" id="under_16" value="under_16" name="user_age"><label for="under_16" class="light">Мужской</label><br>
                                    <input type="radio" id="over_16" value="over_16" name="user_age"><label for="over_16" class="light">Женский</label><br>
                                    <div class="text-block3">
                                    <label>Почему вы хотите принять участие в миссии?</label>
                                    </div>
                                    <textarea class="size-fields" id="bio" name="student_bio"></textarea>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <input class="text-block3" type="checkbox" id="engineering" value="interest_engineering" name="user_interest"><label class="light" for="engineering">Готовы остаться на Марсе?</label><br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')