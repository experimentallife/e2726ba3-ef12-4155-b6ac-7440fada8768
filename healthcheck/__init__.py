from flask import Blueprint

healthcheck_blueprint = Blueprint('healthcheck', __name__)

@healthcheck_blueprint.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'OK'