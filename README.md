# a cookiecutter for flask project

## usage

install cookiecutter
```
pip install cookiecutter
```

setup the project
```
cookiecutter https://github.com/amirsalmanii/my-flask-template.git
```

install requirements
```
pip install -r requirements/local.txt
```

docker-compose
```
docker-compose -f ./docker-compose.dev.yml up -d
```

flask run
```
export FLASK_APP=main.py
flask run
```