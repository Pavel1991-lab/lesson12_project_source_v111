'''Ипмортируем нужные функции, классы, из Флакска блюпринт, создаем блипринт лоадер'''
import logging

from flask import Blueprint, render_template, request
from main.utils import PostHendler
from loader.utils import save_picture


loader_blueprint = Blueprint("loader_blueprint", __name__)
logging.basicConfig(filename='basic.log', encoding='utf-8', level=logging.INFO)

"""создаем вьюшку которая будет на экран выводит шабло для добавление поста"""
@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template("post_form.html")

"""создаем вьюшку которая будет добавлять каритнку и контент"""
@loader_blueprint.route('/post', methods=['POST'])
def create_post():
    picture = request.files.get('picture')
    content = request.form.get("content")

    "Создаем лог который будет выводить ошбику при некоректном заполнении формы"
    if not picture or not content:
        logging.info(f'eror')
        return 'Не все поля заполнены'

    "Создаем лог который будет выводить ошбику если мы загружаем не изображение"
    picture_path = save_picture(picture)
    if not picture_path:
        logging.info(f'Загружено не изображение')
        return 'Загружено не изображение'

    post_hendler = PostHendler('posts.json')
    new_post = {'pic': picture_path, 'content' : content}
    post_hendler.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content )

