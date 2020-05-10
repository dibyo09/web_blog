from datetime import datetime

from pymongo import collection

from src.common.database import Database

import uuid



_author_='Dibya Ganguly'
from src.models.post import  Post

class Blog(object):
    def __init__(self, author, title, author_id, description, _id=None):
        self.title=title
        self.author_id=author_id
        self.author=author
        self.description=description
        self.id= uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,date=datetime.utcnow()):
        if date =="":
            date=datetime.utcnow()
        else:
             date=datetime.strptime(date, '%d%m%Y')
        post = Post( blog_id=self._id
                     ,title=title
                     ,content=content
                     ,author=self.author
                     ,created_date=date
                     )
        post.save_to_mongo()


    def get_posts(self):
        print(" Fetching post for blog id {} ".format(self._id))
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'author': self.author,
            'description':self.description,
            'author_id':self.author_id
        }
    @classmethod
    def from_mongo(cls,id):
        blog_data= Database.find_one(collection='blogs',query={'id': id})
        if blog_data==None :
            print('None')
        else :
            print(blog_data['description'])
           # return  Blog(author= blog_data['author'],
            #             title= blog_data['title'],
             #            description= blog_data['description'],
              #           _id= blog_data['_id'])
        return cls(**blog_data)

    @classmethod
    def from_mongo_by_author(cls, author_id):
        blog_data = Database.find_one(collection='blogs', query={'author_id': author_id})
        #return cls(author=blog_data['author'],
        #           title=blog_data['title'],
        #           description=blog_data['description'],
        #           _id=blog_data['_id'])
        return [cls(**blog) for blog in blog_data]



