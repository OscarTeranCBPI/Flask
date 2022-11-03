### Authentication Extensions for Flask

This is the list of packages that will be used, and what they’re used for:
- Flask-Login: Management of user sessions for logged-in users
- Werkzeug: Password hashing and verification
- itsdangerous: Cryptographically secure token generation and verification


The password hashing functionality is now complete and can be tested in the shell:

```
(venv) $ flask shell
>>> u = User()
>>> u.password = 'cat'
>>> u.password_hash
>>> u.verify_password('cat')
True
>>> u.verify_password('cat')
False
```

To begin, the extension needs to be installed in the virtual environment:
```bash
(venv) $ pip install flask-login
```
