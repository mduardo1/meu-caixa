from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if email == "admin@email.com" and password == "123456":
        return jsonify({"message": "Login realizado com sucesso"}), 200

    return jsonify({"message": "Credenciais inválidas"}), 401
