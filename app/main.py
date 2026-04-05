from flask import Flask
from app.routes.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)

    # 🔥 REGISTRA AS ROTAS
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return {"message": "Meu Caixa Financeiro rodando"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
