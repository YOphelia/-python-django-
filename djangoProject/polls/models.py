# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agency(models.Model):
    ano = models.CharField(primary_key=True, max_length=8)
    aname = models.CharField(max_length=8, blank=True, null=True)
    asex = models.CharField(max_length=1, blank=True, null=True)
    aphone = models.CharField(max_length=12, blank=True, null=True)
    aremark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agency'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    publisher = models.CharField(max_length=45, blank=True, null=True)
    introduce = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Clinet(models.Model):
    cno = models.CharField(primary_key=True, max_length=10)
    cname = models.CharField(max_length=8, blank=True, null=True)
    csex = models.CharField(max_length=1, blank=True, null=True)
    cage = models.IntegerField(blank=True, null=True)
    caddress = models.CharField(max_length=50, blank=True, null=True)
    cphone = models.CharField(max_length=12, blank=True, null=True)
    csymptom = models.CharField(max_length=50, blank=True, null=True)
    mno = models.ForeignKey('Medicine', models.DO_NOTHING, db_column='mno', blank=True, null=True)
    ano = models.ForeignKey(Agency, models.DO_NOTHING, db_column='ano', blank=True, null=True)
    cdate = models.DateTimeField(blank=True, null=True)
    cremark = models.CharField(max_length=50, blank=True, null=True)
    cmcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clinet'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Medicine(models.Model):
    mno = models.IntegerField(primary_key=True)
    mname = models.CharField(max_length=50, blank=True, null=True)
    mmode = models.CharField(max_length=2, blank=True, null=True)
    mefficacy = models.CharField(max_length=50, blank=True, null=True)
    mcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'


class Root(models.Model):
    rootname = models.CharField(primary_key=True, max_length=45)
    rootpassword = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'root'


class User(models.Model):
    username = models.CharField(max_length=45)
    userphone = models.CharField(primary_key=True, max_length=12)
    password = models.CharField(max_length=20)
    userid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
