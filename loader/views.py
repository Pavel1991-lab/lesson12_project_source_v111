from flask import Blueprint, render_template, request
from main.utils import PostHendler
from loader.utils import save_picture

loader_blueprint = Blueprint("loader_blueprint", __name__)

@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template("post_form.html")





@loader_blueprint.route('/post', methods=['POST'])
def create_post():
    picture = request.files.get('picture')
    content = request.form.get("content")

    if not picture or not content:
        return  'Не все поля заполнены'

    picture_path = save_picture(picture)
    if not picture_path:
        return 'Загружено не изображение'

    post_hendler = PostHendler('posts.json')
    new_post = {'pic': picture_path, 'content' : content}
    post_hendler.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content )

