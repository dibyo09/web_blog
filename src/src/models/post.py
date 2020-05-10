_author_='Dibya Ganguly'

from src.common.database import Database
import uuid
import datetime

# noinspection PyStatementEffect
class Post(object):
    #title="without init"

    def custom_init(self):
        self.title= "This is my custom title "
        self.content= "This is my costom content "



    def __init__(self,blog_id , title,content,author,created_date=datetime. datetime.today() ,_id=None):
        self.blog_id=blog_id
        self.author=author
        self.content=content
        self.title= title
        self.id= uuid.uuid4().hex if _id is None else _id
        self.created_date=created_date

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'blog_id': self.blog_id,
            'created_date': self.created_date
        }
    @classmethod
    def from_mogo(cls,id):
        post_data= Database.find_one(collection='posts',query={'id':id})
       # return cls(blog_id =post_data['blog_id'],
       #            title=post_data['title'],
       #            content=post_data['content'],
       #            author=post_data['author'],
       #            created_date=post_data['created_date'] ,
       #            _id=post_data['_id'])
        return cls(**post_data)
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]
