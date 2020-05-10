import uuid
#import speechrecognition

#import pyaudio
from datetime import datetime

from flask import Flask, session
from src.models.blog import  Blog

from src.common.database import Database

class User(object):
    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
        self._id= uuid.uuid4().hex if _id is None else _id
    @classmethod
    def get_by_email(cls,email):
        user_data= Database.find_one(collection='user',query={'email':email})
        if user_data is not None:
            return cls(**user_data)

    @classmethod
    def get_by_idl(cls, id):
        user_data = Database.find_one(collection='user', query={'_id': id})
        if user_data is not None:
            return cls(**user_data)
        return None

    @staticmethod
    def login_valid(email,password):
        print("user email {} in loginvalid".format(email))

        user=User.get_by_email(email)
        print("user email {}")
        if user is not None:
            print("user is not none  {} and password {}".format(user.email,user.password))
            #check Password
            if user.password==password:
                return True
        print("user email is None")
        return False
    @classmethod
    def register(cls, email,password):
        user= cls.get_by_email(email)
        if user is  None:
            new_user=  User(email,password)
            new_user.save_to_mongo()
            session['email']=email
            return True
        else:
            return False

    def login(user_email):
        #login valid is already called
        session['email']=user_email

    def logout(self):
        session['email']=None

    def new_blog(self,title,description):
        new_blogs= Blog(self.email,title,self._id,description)
        new_blogs.save_to_mongo()

    def new_post(self,blog_id,title , content, date = datetime.utcnow()):
        blog= Blog.from_mongo(blog_id)
        blog.new_post(title= title,
                      content=content,
                      date=date)




    def get_blogs(self):
        return  Blog.from_mongo_by_author(self._id)
    def save_to_mongo(self):
        Database.insert(collection='user',data=self.json())

    def json(self):
        return {
            'email':self.email
            ,'_id':self._id
            ,'password':self.password
        }

