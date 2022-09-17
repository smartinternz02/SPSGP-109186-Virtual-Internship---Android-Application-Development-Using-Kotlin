from operator import itemgetter
from flask import (
    Blueprint, request, abort, jsonify
)
from app.model import db, Item, ItemSchema

bp = Blueprint('api', __name__, url_prefix='/list')


@bp.route('/', methods=["POST"])
def create_item():
    data = request.get_json()
    if 'content' not in data.keys():
        abort(400)
    item = Item(content=data['content'])
    db.session.add(item)
    db.session.commit()
    return ItemSchema().jsonify(item)


@bp.route('/', methods=["GET"])
def read_items():
    items = ItemSchema(many=True).dump(Item.query.all()).data
    return jsonify(sorted(items, key=itemgetter('done')))


@bp.route('/<int:id>', methods=["GET"])
def read_item(id):
    item = Item.query.filter_by(id=id).first()
    if not item:
        return abort(404)
    return ItemSchema().jsonify(item)


@bp.route('/<int:id>', methods=["PUT"])
def update_item(id):
    print("Entrou no PUT")
    item = Item.query.filter_by(id=id).first()
    print(item)
    if not item:
        return abort(404)
    data = request.get_json()
    print(data)
    if 'content' not in data.keys() or 'done' not in data.keys():
        return abort(400)
    item.content = data['content']
    item.done = data['done']
    db.session.commit()
    return ItemSchema().jsonify(item)


@bp.route('/<int:id>', methods=["DELETE"])
def delete_item(id):
    item = Item.query.filter_by(id=id).first()
    if not item:
        return abort(404)
    db.session.delete(item)
    db.session.commit()
    return "", 204
