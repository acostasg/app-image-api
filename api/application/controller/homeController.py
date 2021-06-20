from flask import render_template, Blueprint

home = Blueprint('homeController', __name__)


@home.route('/')
def index():
    return render_template(
        'index.html',
        title="API Image App",
        text="API for app Image desktop "
    )


@home.route('/about')
def about():
    return 'Page about API for app Image desktop'


@home.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
