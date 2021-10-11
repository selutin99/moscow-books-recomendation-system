# moscow-books-recomendation-system

### Table of contents
- [Overview](#Overview)
- [Documentation](#Documentation)
- [Git info](#Git-info)
- [Development](#Development)
	- [Local Development](#Local-development)
	- [Docker](#Docker)
- [Testing](#Testing)
	- [Code style](#Code-style)
	- [Unit tests](#Unit-tests)
- [Other useful info](#Other-useful-info)
	- [Authors](#Authors)
	- [Contributing](#Contributing)
	- [Code of Conduct](#Code-of-Conduct)
	- [License](#License)
	- [DI container](#DI-container)

## Overview
Recommendation system for users of Moscow libraries via Flask framework.

## Documentation
...

## Git info
* For each issue, a separate branch is created with the name "feature/[name_of_feature]" (without []);
* After the work is completed, a pull request is created to the master branch;
* Make sure that all CI & CD validations are passed successful.

## Development
### Local development
* Check you have Python 3.7 installed by typing on commandline `python --version`
* Install environment
```
pip install virtualenv
virtualenv venv
CALL venv/Scripts/activate.bat (on Windows)
source venv/bin/activate (on Linux)
pip install -r requirements.txt
```

* Run server `python manage.py runserver`
* Point your web browser to http://localhost:5000/

### Docker
```
docker build -t moscow-books-recomendation-system:latest .
docker run -d -p 5000:5000 moscow-books-recomendation-system:latest
```

## Testing

### Code style
* Run `pycodestyle --exclude=venv,flask_inject.py,container.py --max-line-length=120 .`

### Unit tests

* Run `pytest`

## Other useful info
### Authors
* Aleksandr Seliutin - [selutin99](https://github.com/selutin99)
* Mayya Kotyga - [Kotyga](https://github.com/Kotyga)
* Michael Bolshepopov - [Michael](https://vk.com/big____foot)
* Valeria Beria - [Beria](https://vk.com/hackergod707)

### Contributing
Please, follow [Contributing](CONTRIBUTING.md) page.

### Code of Conduct
Please, follow [Code of Conduct](CODE_OF_CONDUCT.md) page.

### License
This project is Apache License 2.0 - see the [LICENSE](LICENSE) file for details

### DI container
This template uses the `flask_inject` module to implement a dependency injection container. 
It is assumed that the services you create will be added to the container manually, 
and your routes will inject services from the context.