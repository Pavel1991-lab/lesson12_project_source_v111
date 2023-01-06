from flask import Blueprint, render_template, request
from main.utils import PostHendler
import logging
main_blueprint = Blueprint("main_blueprint", __name__,)

logging.basicConfig(filename='basic.log', encoding='utf-8', level=logging.INFO)


"""Создаем вьюшку которая выведет нас на главную страницу"""
@main_blueprint.route('/')
def index_page():
    return render_template("index.html")

"""Вьюшка которая будет находить посты по запросу"""
@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    "Лог который будет показывать когда мы ищем пост"
    logging.info(f'Поиск {substr}')
    post_handler = PostHendler('posts.json')
    posts = post_handler.search_posts(substr)
    return render_template("post_list.html", posts = posts, substr = substr)


