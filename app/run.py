from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    # Entry the application
    flask_app = create_app()
    flask_app.run(host='0.0.0.0', port=5000, threaded=True)
