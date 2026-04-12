from flask import Flask
from flask_cors import CORS
from app.routes.auth_routes import auth_bp
from app.database import create_tables


def create_app():
    app = Flask(__name__)

    CORS(app)  # 🔥 LIBERA O FRONTEND ACESSAR O BACKEND

    create_tables()
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return {"message": "Meu Caixa Financeiro rodando"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)