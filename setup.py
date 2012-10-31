from maps import app
from settings.settings import configs

app.config.update(configs)


if __name__ == '__main__':
    app.run()
