### Large Application Structure

**Basic multiple-file Flask application structure**

```bash
|-flasky
    |-app/
        |-templates/
        |-static/
        |-main/
            |-__init__.py
            |-errors.py
            |-forms.py
            |-views.py
        |-__init__.py
        |-email.py
        |-models.py
    |-migrations/
    |-tests/
        |-__init__.py
        |-test*.py
    |-venv/
    |-requirements.txt
    |-config.py
    |-flasky.py
```

*Notes about imports*
The from . import some-module syntax is used in Python to
represent relative imports. The . in this statement represents the
current package. You are going to see another very useful relative
import soon that uses the form from .. import some-module,
where .. represents the parent of the current package.

Because the main script of the application changed from hello.py to flasky.py, the
FLASK_APP environment variable needs to be updated accordingly so that the flask
command can locate the application instance. It is also useful to enable Flask’s debug
mode by setting FLASK_DEBUG=1. For Linux and macOS, this is all done as follows:
```bash
(venv) $ export FLASK_APP=flasky.py
(venv) $ export FLASK_DEBUG=1
```

The unit tests can be executed as follows:
```bash
(venv) $ flask test
```

#### Running the Application
```bash
(venv) $ flask run
```

**NOTE 1:**
This chapter does not mention in such a clear way the totality of the files and the code. 
For this we cloned the repo located at [Link](https://github.com/miguelgrinberg/flasky) and type the following command to change the branch of the repo to the one where the files are located:
```bash
git checkout 7a
```


