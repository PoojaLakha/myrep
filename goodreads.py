from peewee import (CharField, IntegerField, Model, TextField, SqliteDatabase,
                    ForeignKeyField, TimestampField, DoubleField)

db = SqliteDatabase('Goodreads.db')


class User(Model):
    email_id = IntegerField(unique=True)
    email = TextField()
    password = CharField()


class UserDetail(Model):
    user_id = IntegerField()
    user_name = CharField()
    email = ForeignKeyField(User)
    details = TextField()


class Book(Model):
    isbn_number = IntegerField(unique=True)
    book_id = IntegerField()
    book_name = CharField()


class Author(Model):
    isbn_number = ForeignKeyField(Book)
    author_id = IntegerField()
    author_name = CharField()
    genre = CharField()


class Message(Model):
    sender_id = ForeignKeyField(User)
    receiver_id = ForeignKeyField(User)
    subject = TextField()
    message = TextField()
    timestamp = TimestampField()


class Comment(Model):
    book_id = ForeignKeyField(Book)
    user_id = ForeignKeyField(User)
    comment_id = IntegerField()
    comment = TextField()
    likes = IntegerField()


class Book_Rating(Model):
    user_id = ForeignKeyField(User)
    book_id = ForeignKeyField(Book)
    rating = DoubleField()
