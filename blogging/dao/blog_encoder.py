from json import JSONEncoder
from blogging.blog import Blog

class BlogEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Blog):
            return {'__type__': 'Blog',
                    'counter': obj.counter,
                    'id': obj.id, 'name': obj.name,
                    'url': obj.url, 'email': obj.email
            }
        
        return super().default(obj)