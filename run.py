from config import app
from views.view import analysis

app.register_blueprint(analysis, url_prefix="/")

if __name__ == '__main__':
    app.run()

