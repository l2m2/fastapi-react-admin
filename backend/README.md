
## Setup virtual environment
### Use virtualenv on Windows
**install**
```bash
$ python -m pip install --user virtualenv
$ python -m virtualenv --help
```
**create virtual env**
```bash
$ virtualenv .venv
```
**remove virtual env**
```bash
$ rm -rf .venv
```
**Windows venv activation**
```bash
$ .venv\Scripts\activate.bat
```
**Windows venv deactivate**
```bash
$ .venv\Scripts\deactivate.bat
```
### [Use pyenv + virtualenvwrapper on MacOS](https://l2m2.top/2020/03/31/2020-03-31-right-way-to-set-python3-on-macos/)

### install requirements
```bash
$ cd backend
$ pip install -r requirement.txt
```

## Alembic

first, modify the SQL Model in backend/app/app/models.

second, generate scripts and upgrade to database.

```bash
$ cd backend\app
$ alembic revision --autogenerate -m "xxx" # generate migrate scripts
$ alembic upgrade head # upgrade to real database
```

## Generate a random JWT secret
```bash
$ node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

## Prepare to start backend
```bash
$ cd backend
$ prestart.bat # Windows
```

## Start backend
```bash
$ cd backend
$ start.bat # Windows
```