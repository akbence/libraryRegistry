# libraryRegistry application

This repo contains my very first Django application, where I learned the basics of the framework and created a little library registry software.
As I am (currently) more interested in backend, therefore the frontend part of the application may not be the best, because I didn't care too much about it.

## How to run

You will need Python 3.7 and Django 2.x.x to run this application. You can delete freely the SQLite file, and create your own db.
1. python admin.py makemigrations
2. python admin.py migrate
3. python admin.py runserver
4. Enjoy :sparkles:

## Features

### User handling
You can create your own user to access other features than, the homepage.
After that you can login and logout anytime, when you want to access a restricted page, the application will ask you to login

### Category handling

Each books can have its own Category, which is a standalone model entity. I know there could be an entity for authors as well, but for
learning purposes, its enough. Categories can't be edited right now (without admin access), maybe later

## Book handling

You can watch the list of your own library. After login you can create new books, update existing ones or delete any of them.
If you click on any book link, it will give a detailed view, which will contain the author, title, page number, date of creation to the lib
date of read, and a flag which shows, if it is already read or not.
