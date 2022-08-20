# Store Rest API

Store Rest API is an API that helps perform CRUD applications on your syatem. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any package in the requirements.txt file.

## Steps to follow

* The first thing to do is clone the repository

* Then you need to cd into the directory `cd store-restapi`

* Activate virtual environment. `source env/bin/activate`
```bash
source env/bin/activate
```
* Then you need to install requirements.txt file `pip install -r requiremts.txt`
```bash 
pip install -r requirements.txt
```
* Lastly run your server
```bash
# Make migrations
python manage.py makemigrations 

# Migrate
python manage.py migrate

# Start the server
python manage.py runserver
```
## Executing CRUD functionalities

On your browser go to `http://127.0.0.1:8000/api/` to start using it.

To experiment more it is better to us `Postman` because of its many functionalities.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
