from flask import Blueprint, render_template

pages_blueprint = Blueprint('pages', __name__, static_url_path='/static')

@pages_blueprint.route('/', methods=['GET'])
def healthcheck():
    return render_template('index.html', name='pedrito')