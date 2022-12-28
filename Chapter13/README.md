## Chapter 13
### User comments

Here we detail and apply the new representation of the comments in the database.

For this chapter there is an error.
```python
The function 
pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    error_out=False)
```
requires that the term page be passed as an explicit argument.
This correction must be made in all calls to the function.
