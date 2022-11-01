This chapter was uploaded completely in one commit.
You only need to perform a git pull and you will have all the changes.

In this chapter it is necessary to download and install extra packages related to databases.

The commands are:

```bash
(venv) $ pip3 install flask-sqlalchemy
```

```bash
pip install flask-migrate
```
To observe the behavior of flask and the databases we must type the following commands:

```bash
(venv) $ export FLASK_APP=hello.py
```

```bash
(venv) $ flask shell
```

With this we have an active interpreter in which we can perform the necessary operations on the database.
NOTE: For this example we worked with SQLite.

Commands examples:
```bash
- from hello import db
- db.create_all()
- db.drop_all()
- app
- db
```
### Migrate
```bash
flask db upgrade
```
