from flask import Blueprint, request, jsonify
from models.user import db,user

users = Blueprint('users', __name__)

@users.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    if not username :
        return jsonify({"error": "username is required"}), 400

    query = db.text("""
                    INSERT INTO users (username)
                    VALUES (:username)
                    RETURNING *;
                    """)
    result = db.session.execute(query,{"username":username})
    db.session.commit()

    row = result.mappings().first()
    return jsonify(dict(row)), 201

@users.route('/', methods=['GET'])
def get_users():
    # date_param = request.args.get('date')

    query = db.text("""
                    select * from users
                    """)
    result = db.session.execute(query)

    rows = result.mappings().all()  # Converts each row into a dict-like object
    return jsonify([dict(row) for row in rows])