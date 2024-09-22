## Overview

This is a simple blog project built using the Django web framework. The project allows users to create blog posts, log in and log out, as well as update or delete their posts. The blog offers basic CRUD (Create, Read, Update, Delete) functionality with user authentication.

## Features

Create posts: Authenticated users can create blog posts with a title and body.
View posts: All users (including non-authenticated users) can view blog posts.
Update posts: Authenticated users can update their own blog posts.
Delete posts: Authenticated users can delete their own blog posts.
User authentication: Users can register, log in, and log out of the application.

## How to run :

1 - Install dependencies: Ensure all the required packages are installed by running:

```
pip install -r requirements.txt
```
2 - Run migrations: Create the necessary tables by running the database migrations:

```
python manage.py migrate
```

3 - Create a superuser: Set up an admin user:

```
python manage.py createsuperuser
```

4 - Start the server: Run the Django development server:

```
python manage.py runserver
```

5- Access the app: Visit http://localhost:8000 to access the app.