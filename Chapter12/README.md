## Chapter 12
### Followers

This chapter describes the relationships that exist to store the necessary information in a database with a many-to-many relationship between tables.

No extra libraries are required for this chapter. The requirements of the previous chapter are sufficient.

For this chapter there is an error.
```python
The function 
pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    error_out=False)
```
requires that the term page be passed as an explicit argument.
This correction must be made in all calls to the function.
