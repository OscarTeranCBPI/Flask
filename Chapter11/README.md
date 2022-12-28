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
For this chapter there is an error.
```python
The function 
pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    error_out=False)
```
requires that the term page be passed as an explicit argument.
This correction must be made in all calls to the function.
