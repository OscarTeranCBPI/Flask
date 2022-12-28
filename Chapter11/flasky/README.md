## Chapter 11
### Blog Posts

This chapter describes how to store and the logic behind the creation of a post system. To facilitate the creation of these messages we make use of the faker library.

```bash
(venv) $ pip install faker
```

Using the faker library, we easily create a random list of posts and users.

```bash
(venv) $ flask shell
from app import fake
fake.users(100)
fake.posts(100)
```

For the best visualization and reading of the posts, we use the following libraries

```bash
(venv) $ pip install flask-pagedown markdown bleach
```
