from flask import Blueprint, render_template, request
from main.utils import PostHandler
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    logging.info(f'Поиск: {substr}')
    post_handler = PostHandler('posts.json')
    posts, error = post_handler.search_posts(substr)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка!'
    return render_template('post_list.html', posts=posts, substr=substr)