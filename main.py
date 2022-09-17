from flask import (
    Blueprint, render_template, send_from_directory, url_for
)
import os

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title=os.environ.get('INDEX_TITLE') or "Grocery App")
