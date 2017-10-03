from peewee import (Model, SqliteDatabase, TextField, CharField, IntegerField,
                    ForeignKeyField, TimestampField, DoubleField)

DB = SqliteDatabase('Goodreads.db')


class User(Model):
    email = TextField(unique=True)
    password = CharField()
    user_name = CharField()
    details = TextField()


class Book(Model):
    book_id = IntegerField(unique=True)
    book_title = CharField()


class Author(Model):
    author_id = IntegerField(unique=True)
    author_name = CharField()


class BookAuthor(Model):
    book_id = ForeignKeyField(Book)
    author_id = ForeignKeyField(Author)
    genre = CharField()


class User_Book_Review(Model):
    user = ForeignKeyField(User)
    book = ForeignKeyField(Book)
    rating = DoubleField()
    comment = TextField()


class Message(Model):
    sender_id = ForeignKeyField(User)
    receiver_id = ForeignKeyField(User)
    subject = TextField()
    message = TextField()
    timestamp = TimestampField()
