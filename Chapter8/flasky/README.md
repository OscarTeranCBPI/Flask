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

#### Protecting Routes
To protect a route so that it can only be accessed by authenticated users, Flask-Login provides a login_required decorator.

Because no user registration functionality has been built, a new user can only be reg‐
istered from the shell at this time:
```bash
(venv) $ $ flask shell
>>> u = User(email='john@example.com', username='john', password='cat')
>>> db.session.add(u)
>>> db.session.commit()
```

The following is a short shell session that shows how itsdangerous can generate a
signed token that contains a user id inside:
```bash
(venv) $ flask shell
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer(app.config['SECRET_KEY'], expires_in=3600)
>>> token = s.dumps({ 'confirm': 23 })
>>> token
'eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4MTcxODU1OCwiaWF0IjoxMzgxNzE0OTU4fQ.ey ...'
>>> data = s.loads(token)
>>> data
{'confirm': 23}
```
