# Flipkart Clone

A backend clone of Flipkart with basic functionalities like for users, products, categories, orders, wishlist, etc.

# Guides & Processes

## Getting Started

Please follow the steps for running the Flask application.

- Create a virtual environment by `virtualenv`
- Install the dependencies in `requirements.txt` by `pip install -r requirements.txt`
- Export the Flask variables
    - `export FLASK_ENV=development`
    - `export FLASK_APP=[server.py](http://server.py/)`
    - `flask run`

## How does the application work?

The application is using Flask and MySQL as database. 

There are 3 types of users: owners, user and admin. The functionalities of each users are shown below:

- only owner can edit, delete, add products owned by the same person.
- admin can edit/delete any item or remove any user/owner
- categories can be nested as tree structure (use closure tables)
- user can view all the products
- user can use search and filters with categories and Sub-categories
- user can add the item to Wishlist
- user can add products to cart and order
- users can comment on the item and other users can upvote or downvote the comment

JWT is used for sessions. Followed MVC structure and ORM to connect MySQL.
