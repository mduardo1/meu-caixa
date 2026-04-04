import hashlib
from app.models.user_model import User


class AuthService:
    def __init__(self):
        self.users = []

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, email: str, password: str):
        if not email or not password:
            return {"message": "Email e senha são obrigatórios"}, 400

        for user in self.users:
            if user.email == email:
                return {"message": "Usuário já existe"}, 409

        password_hash = self.hash_password(password)
        new_user = User(email=email, password_hash=password_hash)
        self.users.append(new_user)

        return {"message": "Usuário cadastrado com sucesso"}, 201

    def login_user(self, email: str, password: str):
        if not email or not password:
            return {"message": "Email e senha são obrigatórios"}, 400

        password_hash = self.hash_password(password)

        for user in self.users:
            if user.email == email and user.password_hash == password_hash:
                return {"message": "Login realizado com sucesso"}, 200

        return {"message": "Credenciais inválidas"}, 401
