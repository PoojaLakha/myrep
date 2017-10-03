from peewee import (CharField, IntegerField, Model, TextField, SqliteDatabase,
                    ForeignKeyField, TimestampField)

DB = SqliteDatabase('instagram.db')


class InstaUser(Model):
    User_name = CharField(unique=True)
    email = TextField()
    bio = TextField()
    Posts = IntegerField()
    Followers = IntegerField()
    Following = IntegerField()


class InstaPhoto(Model):
    user = ForeignKeyField(InstaUser)
    photo = CharField()
    comment = TextField()
    tag = TextField()
    likes = IntegerField()


class InstaMsg(Model):
    send_id = ForeignKeyField(InstaUser)
    receive_id = ForeignKeyField(InstaUser)
    message = TextField()
    timestamp = TimestampField()


class InstaStory(Model):
    user = ForeignKeyField(InstaUser)
    story = TextField()
    tag = TextField()
    s_comment = ForeignKeyField(InstaMsg)


class InstaVideo(Model):
    user = ForeignKeyField(InstaUser)
    video = TextField()
    views = IntegerField()
    comment = TextField()
    likes = IntegerField()
