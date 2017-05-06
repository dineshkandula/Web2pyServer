# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def signup():
    emailid = request.vars.email
    userid = request.vars.username
    Password = request.vars.password
    name = request.vars.name
    gender = request.vars.gender
    phno = request.vars.phno
    age = request.vars.age

    db.users.insert(
    email = emailid,
    username=userid,
    password =Password,
    Name=name,
    Gender=gender,
    PhoneNumber=phno,
    Age=age,
    )
    return dict(Success = True)

def login():
    userid = request.vars.username
    password = request.vars.password
    user = auth.login_bare(userid,password)
    return dict(success=False if not user else True, user=user)

def logged_in():
    return dict(success=auth.is_logged_in(), user=auth.user)

def logout():
    return dict(success=True, loggedout=auth.logout())

def profile():
    username = auth.user.username
    profile = db(db.users.username==username).select()
    return dict(Profile = profile)
