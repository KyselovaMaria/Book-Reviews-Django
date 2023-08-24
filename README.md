# Book-Reviews-Django
Making a book review website using Django and MySql

# Environment 
PyCharm (takes care of creating specific directory structure and files required for a Django application, and providing the correct settings)

XAMPP for easy MySQL connection 

# Description
The site must have user registration. 

Editors (user subspecies) are assigned separately.

The editor can add a book to the site by filling in all the information about it - title, short description, authors, genre (perhaps also the cover).

The user can view information about books.

The user can add books to the personal category of favorite books and view this list.

For each book, the user can give a personal rating (from 1 to 5), which is based on the general rating of the book, which is part of the information about it (arithmetic average of all ratings).

Each user can rate only one book.

The main page of the site shows a list of all books.

In addition, there should be a book filter by genre and a search by title or author.

# How to start
$ python manage.py makemigrations

$ python manage.py migrate

python manage.py createsuperuser
(http://127.0.0.1:8008/admin/)

python manage.py runserver 8008
(http://127.0.0.1:8008/book/all_books)

# Examples
![image](https://github.com/KyselovaMaria/Book-Reviews-Django/assets/88087036/cd2de9ec-58b8-4b70-95ff-9ee44c8c7894)
![image](https://github.com/KyselovaMaria/Book-Reviews-Django/assets/88087036/3d9be479-fce1-4dec-849d-93454fff5260)
![image](https://github.com/KyselovaMaria/Book-Reviews-Django/assets/88087036/642987b4-4f10-4835-9e94-cdf13d7bd5e5)
![image](https://github.com/KyselovaMaria/Book-Reviews-Django/assets/88087036/c1ca6901-84f5-4d86-90fe-010a8b1accb2)

