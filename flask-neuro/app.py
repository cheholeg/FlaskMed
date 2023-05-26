from flask import Flask, render_template, request,jsonify, redirect, url_for #render_template - позволяет работать с шаблонами
import sqlite3 #библиотека для работы с sqlite3 
from distutils.log import debug
from fileinput import filename
import os
import subprocess
import pandas as pd
from werkzeug.utils import secure_filename
import requests
#-------------------#
#-------------------#


#-------------------#
#-------------------#
app = Flask(__name__) #Создаем экземпляр класса Flask
#-------------------#
#-------------------#


app.config["UPLOAD_FOLDER"] = "static\\" #настраиваем переменную UPLOAD_FOLDER к пути, по которому мы хотим сохранить наши файлы

#-------------------#
#-------------------#

@app.before_request #вызывается перед тем, как запустится рендер шаблонов
def first_request():
    init_db()

#-------------------#
#-------------------#
#----Создаем_маршрут----#
@app.route('/')
def index():
    conn = get_db_connection() #получаем подключение к базе данных
    posts = conn.execute('SELECT * FROM posts').fetchall() #выполняем запрос к таблице и получаем все записи, используя метод fetchall()
    conn.close() #закрываем подключение
    return render_template('index.html', posts=posts) #передаём полученные записи в шаблон используя render_template

@app.route('/<int:post_id>') #задаём новый маршрут, в конце будет номер id поста (целый)
def get_post(post_id): #post_id передаём айдишник поста, который как раз и «встанет» в URL-адрес и добавится к запросу к базе данных
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES ("Why I love Flask", "This is so cool!!!")')
    conn.execute('INSERT INTO posts (title, content) VALUES ("Cats >> Dogs", "It was a joke because they are all so adorable.")')
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone() #берём одну строку функцией fetchone()
    conn.close()
    return render_template('post.html', post=post) #рендерим HTML-шаблон и передаём туда полученный пост


#при методе GET функция просто отображает форму для ввода данных с помощью шаблона add_post.html
#при методе POST, мы достаём заголовок и тело поста из формы, а затем добавляем их в базу данных
@app.route('/new', methods=['GET', 'POST']) 
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_post.html')


@app.route('/arrytmia', methods=['GET', 'POST']) 
def arrytmia():
    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    reply = subprocess.run(["python", 'recognize_all.py'], stdout=subprocess.PIPE)
    for file in files:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    # Uploaded File Path
    data_file_path = 'result.csv'
    # read csv
    uploaded_df = pd.read_csv(data_file_path,
                              encoding='unicode_escape')
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('arrytmia.html',
                           data_var=uploaded_df_html)


@app.route('/dislocation', methods=['GET', 'POST']) 
def dislocation():
    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    reply = subprocess.run(["python", 'recognizing_RF_corrected.py'], stdout=subprocess.PIPE)
    for file in files:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    # Uploaded File Path
    data_file_path = 'RF.csv'
    # read csv
    uploaded_df = pd.read_csv(data_file_path,
                              encoding='unicode_escape')
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('dislocation.html',
                           data_var=uploaded_df_html)


@app.route('/API_PDB', methods=['GET', 'POST']) 
def API_PDB():
    reply = subprocess.run(["python", 'Proteomics.py'], stdout=subprocess.PIPE)
    # Uploaded File Path
    data_file_path = 'proteo.csv'
    # read csv
    uploaded_df = pd.read_csv(data_file_path,
                              encoding='unicode_escape')
    # Converting to html Table
    uploaded_df_html = uploaded_df.to_html()
    return render_template('API_PDB.html',
                           data_var=uploaded_df_html)


@app.route('/API_MED', methods=['POST']) 
def API_MED():
    if(request.method == 'POST'):
        url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"
        querystring = {"drug":request.form['title']}

        headers = {
            "X-RapidAPI-Key": "6ad9a0ef0cmsh70d828d1a24cde1p12aea4jsn9e95d8e33f19",
            "X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
  
        return jsonify(response.json())


#-------------------#
#-------------------#


#-------------------#
#-------------------#
def get_db_connection(): #функция подключающая к БД database и возвращающая объект подключения
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row #.Row делает каждую строку уникальной, стобцы - содержат инфомрацию
    return conn
#-------------------#



def close_db_connection(conn): #функция закрытия подключения к БД
    conn.close()
#-------------------#


def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL)')
    conn.close()

#-------------------#
#-------------------#





#-------------------#
#-------------------#
#Flask будет запущен только в том случае, если файл app.py был запущен напрямую
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)
#-------------------#
#-------------------#