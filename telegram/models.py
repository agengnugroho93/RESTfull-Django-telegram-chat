from __future__ import unicode_literals

from django.db import models


class Adminlog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contextid = models.IntegerField(db_column='ContextID')  # Field name made lowercase.
    date = models.IntegerField(db_column='Date')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    # mediaid1 = models.ForeignKey('Media', related_name="MediaID1", db_column='MediaID1', blank=True, null=True)  # Field name made lowercase.
    # mediaid2 = models.ForeignKey('Media', related_name="MediaID2", db_column='MediaID2', blank=True, null=True)  # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AdminLog'
        unique_together = (('id', 'contextid'),)


class Channel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateupdated = models.IntegerField(db_column='DateUpdated')  # Field name made lowercase.
    about = models.TextField(db_column='About', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    pictureid = models.ForeignKey('Media', models.DO_NOTHING, db_column='PictureID', blank=True, null=True)  # Field name made lowercase.
    pinmessageid = models.IntegerField(db_column='PinMessageID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Channel'
        unique_together = (('id', 'dateupdated'),)

    def __str__(self):
        return self.title


class Chat(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateupdated = models.IntegerField(db_column='DateUpdated')  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    migratedtoid = models.IntegerField(db_column='MigratedToID', blank=True, null=True)  # Field name made lowercase.
    pictureid = models.ForeignKey('Media', models.DO_NOTHING, db_column='PictureID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Chat'
        unique_together = (('id', 'dateupdated'),)


class Chatparticipants(models.Model):
    contextid = models.IntegerField(db_column='ContextID')  # Field name made lowercase.
    dateupdated = models.IntegerField(db_column='DateUpdated')  # Field name made lowercase.
    added = models.TextField(db_column='Added')  # Field name made lowercase.
    removed = models.TextField(db_column='Removed')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ChatParticipants'
        unique_together = (('contextid', 'dateupdated'),)


class Forward(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    originaldate = models.IntegerField(db_column='OriginalDate')  # Field name made lowercase.
    fromid = models.IntegerField(db_column='FromID', blank=True, null=True)  # Field name made lowercase.
    channelpost = models.IntegerField(db_column='ChannelPost', blank=True, null=True)  # Field name made lowercase.
    postauthor = models.TextField(db_column='PostAuthor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Forward'


class Media(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    mimetype = models.TextField(db_column='MimeType', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    thumbnailid = models.ForeignKey('self', models.DO_NOTHING, db_column='ThumbnailID', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    localid = models.IntegerField(db_column='LocalID', blank=True, null=True)  # Field name made lowercase.
    volumeid = models.IntegerField(db_column='VolumeID', blank=True, null=True)  # Field name made lowercase.
    secret = models.IntegerField(db_column='Secret', blank=True, null=True)  # Field name made lowercase.
    extra = models.TextField(db_column='Extra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Media'
    
    def __str__(self):
        return self.name


class Message(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  #   Field name made lowercase.
    contextid = models.IntegerField(db_column='ContextID')  # Field name made lowercase.
    date = models.IntegerField(db_column='Date')  # Field name made lowercase.
    fromid = models.IntegerField(db_column='FromID', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message', blank=True, null=True)  # Field name made lowercase.
    replymessageid = models.IntegerField(db_column='ReplyMessageID', blank=True, null=True)  # Field name made lowercase.
    forwardid = models.ForeignKey(Forward, models.DO_NOTHING, db_column='ForwardID', blank=True, null=True)  # Field name made lowercase.
    postauthor = models.TextField(db_column='PostAuthor', blank=True, null=True)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True)  # Field name made lowercase.
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='MediaID', blank=True, null=True)  # Field name made lowercase.
    formatting = models.TextField(db_column='Formatting', blank=True, null=True)  # Field name made lowercase.
    serviceaction = models.TextField(db_column='ServiceAction', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.message

    class Meta:
        managed = True
        db_table = 'Message'
        unique_together = (('id', 'contextid'),)


class Resume(models.Model):
    contextid = models.IntegerField(db_column='ContextID', unique=True, primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    date = models.IntegerField(db_column='Date')  # Field name made lowercase.
    stopat = models.IntegerField(db_column='StopAt')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Resume'


class Resumeentity(models.Model):
    contextid = models.IntegerField(db_column='ContextID', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    accesshash = models.IntegerField(db_column='AccessHash', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResumeEntity'
        unique_together = (('contextid', 'id'),)


class Resumemedia(models.Model):
    mediaid = models.IntegerField(db_column='MediaID', unique=True)  # Field name made lowercase.
    contextid = models.IntegerField(db_column='ContextID')  # Field name made lowercase.
    senderid = models.IntegerField(db_column='SenderID', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ResumeMedia'


class Selfinformation(models.Model):
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SelfInformation'


class Supergroup(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateupdated = models.IntegerField(db_column='DateUpdated')  # Field name made lowercase.
    about = models.TextField(db_column='About', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    pictureid = models.ForeignKey(Media, models.DO_NOTHING, db_column='PictureID', blank=True, null=True)  # Field name made lowercase.
    pinmessageid = models.IntegerField(db_column='PinMessageID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Supergroup'
        unique_together = (('id', 'dateupdated'),)


class User(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateupdated = models.IntegerField(db_column='DateUpdated')  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio', blank=True, null=True)  # Field name made lowercase.
    bot = models.IntegerField(db_column='Bot', blank=True, null=True)  # Field name made lowercase.
    commonchatscount = models.IntegerField(db_column='CommonChatsCount')  # Field name made lowercase.
    pictureid = models.ForeignKey(Media, models.DO_NOTHING, db_column='PictureID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'
        unique_together = (('id', 'dateupdated'),)
    
    def __str__(self):
        return self.firstname

class Version(models.Model):
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Version'