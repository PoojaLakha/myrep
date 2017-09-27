from peewee import (CharField, IntegerField, Model, TextField, SqliteDatabase,
                    ForeignKeyField, TimestampField)

db = SqliteDatabase('instagram.db')


class InstaUser(Model):
    user_id = IntegerField(unique=True)
    User_name = CharField()
    email = TextField()
    bio = TextField()
    Posts = IntegerField()
    Followers = IntegerField()
    Following = IntegerField()


class InstaTag(Model):
    tag_id = IntegerField(unique=True)
    tag = CharField()


class InstaComment(Model):
    comment_id = IntegerField(unique=True)
    comment = TextField()
    tag_id = ForeignKeyField(InstaTag)


class InstaPhoto(Model):
    user_id = ForeignKeyField(InstaUser)
    Photo_id = IntegerField()
    photo = CharField()
    comment_id = ForeignKeyField(InstaComment)
    tag_id = ForeignKeyField(InstaTag)
    likes = IntegerField()


class InstaMsg(Model):
    send_id = ForeignKeyField(InstaUser)
    receive_id = ForeignKeyField(InstaUser)
    message = TextField()
    timestamp = TimestampField()


class InstaStory(Model):
    story_id = IntegerField()
    user_id = ForeignKeyField(InstaUser)
    story = TextField()
    tag_id = ForeignKeyField(InstaTag)
    s_comment = ForeignKeyField(InstaMsg)


class InstaVideo(Model):
    user_id = ForeignKeyField(InstaUser)
    views = IntegerField()
    comment_id = ForeignKeyField(InstaComment)
    likes = IntegerField()
