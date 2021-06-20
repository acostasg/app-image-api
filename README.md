#Project structure
Desktop application for managing images.

This project used DDD:
- https://en.wikipedia.org/wiki/Domain-driven_design

And flask for generate aip:
- https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/

<pre>
app-image-api/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   └── config.yml
│   │ 
│   ├── templates/
│   │   └── index.html
│   │ 
│   ├── applicaciton/
│   │   ├── __init__.py
│   │   ├── use_case
│   │   └── controller
│   │
│   ├── dominio/
│   │   ├── __init__.py
│   │   ├── entity
│   │   │   ├── __init__.py
│   │   │   └── image.py
│   │   ├── exception
│   │   ├── value_object
│   │   ├── services
│   │   └── respository
│   │
│   ├── infrastucture/
│   │   ├── __init__.py
│   │   ├── entity
│   │   ├── value_object
│   │   ├── services
│   │   └── respository
│   └──   
│
├── tests/
│   ├──applicaciton
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   ├── dominio/
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   └── infrastucture/
│       ├── helpers_tests.py
│       └── world_tests.py
│
├── .gitignore
├── LICENSE
├── requeriments.txt
├── README.md
├── setup.py
└── docker-compose.yml
</pre>

This api is used for app desktop:
```
https://github.com/acostasg/app-image-desktop/blob/master/README.md
```

# Run Application

Option 1)

If you use PyCharm, simply open the file setup.py, and PyCharm will ask you to install the dependencies, it answers yes, and then with the Run -> Run or the Run button you will be able to execute the application.
www.jetbrains.com/pycharm/download/

Option 2)

First application dependency:
```python
python -m pip install -r requirements.txt
```
Execute application:
```python
export FLASK_APP=api/main.py
python api/main.py
```

Execute test: #TODO
```python
python -m unittest
```