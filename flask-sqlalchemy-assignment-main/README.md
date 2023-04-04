# ITSC 3155 Module 11 Assignment

This movie app is very similar to the one you worked on in a team in Module 9. Here, I have started the application for you and you only need to write code in the `TODO` sections.

## Python Version

You must have Python 3.10.* installed to run this application.

## Instructions

1. Clone your GitHub Classrooms repository.
2. Create your virtual environment, make sure it is included in the `.gitignore`.
3. Install the existing project dependencies with `pip install -r requirements.txt` after you activated your virtual environment.
4. Install any other dependencies you need for Flask SQLAlchemy and update your `requirements.txt` file.
5. Run the SQL script in `movies_schema.sql` in pgAdmin to generate your database and the single table.
5. Complete all the `TODO` comments throughout the codebase (search for the `TODO` comment with the VSCode search feature) for a total of 10 points.
    1. Configure the app to connect to your locally running DB, create your SQLAlchemy DB object, initialize your SQLAlchemy DB object, and create your Movie model (**2pts**).
    2. Fill in the `get_all_movies` method of the `MovieRepository` class (**1pt**).
    3. Fill in the `get_movie_by_id` method of the `MovieRepository` class (**1pt**).
    4. Fill in the `create_movie` method of the `MovieRepository` class (**1pt**).
    5. Fill in the `search_movies` method of the `MovieRepository` class (**3pts**).
    6. Make a table to display your movies in `list_all_movies.html` with the title column serving as a link to the individual movie pages (**2pts**).

_**IMPORTANT NOTE:**_ Do **NOT** commit your DB password, delete it out of `app.py` before making any commits and pushing to GitHub, especialy if you reuse that password elsewhere (which is its own problem, use a password manager and unique passwords everywhere).


*This assignment was created for the ITSC 3155 Software Engineering course, taught by Jacob Kedar Krevat, at the College of Computing and Informatics at UNC Charlotte*
