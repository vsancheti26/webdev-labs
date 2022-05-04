from flask import Response, request
from flask_restful import Resource
from models import Post, db, Following
from views import get_authorized_user_ids

import json

def get_path():
    return request.host_url + 'api/posts/'

class PostListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        # get posts created by one of these users:
        
        args=request.args
        user_ids=get_authorized_user_ids(self.current_user)
        
        try:
            limit=int(args.get('limit') or 20)
            
        
        except:
            return Response(json.dumps({"message": "the limit parameter is invalid"}), mimetype="application/json", status=400) 
        
        if limit>50:
            return Response(json.dumps({"message": "the limit parameter is invalid"}), mimetype="application/json", status=400)
        

        posts=Post.query.filter(Post.user_id.in_(user_ids)).limit(limit).all()
        posts_json=[post.to_dict() for post in posts]
        return Response(json.dumps(posts_json), mimetype="application/json", status=200)

    def post(self):
        # create a new post based on the data posted in the body 
        body = request.get_json() 
        
        if not body.get('image_url'):
            return Response(json.dumps({'message':"'image_url' is required. "}), mimetype="application/json", status=400)
            
        #insert whatever was added to db
        new_post=Post(
            image_url=body.get('image_url'),
            user_id=self.current_user.id,
            caption=body.get('caption'),
            alt_text=body.get('alt_text')
        )
        db.session.add(new_post)
        db.session.commit()
        
        return Response(json.dumps( new_post.to_dict()), mimetype="application/json", status=201)
        
class PostDetailEndpoint(Resource):
   
    def __init__(self, current_user):
        self.current_user = current_user
        

    def patch(self, id):
        # update post based on the data posted in the body 
        body = request.get_json()
        print(body)       
        post=Post.query.get(id)
        
        if not post:
            return Response(json.dumps({"message":"id={0} is invalid"}), mimetype="application/json", status=404)
        
        
        if post.user_id !=self.current_user.id:
            return Response(json.dumps({"message":"id={0} is invalid"}), mimetype="application/json", status=404)
        
        if body.get('image_url'):
            post.image_url=body.get('image_url')
        if body.get('caption'):
            post.caption=body.get('caption')
        if body.get('alt_text'):
             post.alt_text=body.get('alt_text')
        db.session.commit()
        return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)


    def delete(self, id):
        # delete post where "id"=id
        post=Post.query.get(id)
        if not post:
            return Response(json.dumps({"message":"id={0} is invalid".format(id)}),  mimetype="application/json", status=404)
        
        if post.user_id!=self.current_user.id:
            return Response(json.dumps({"message":"id={0} is invalid".format(id)}),  mimetype="application/json", status=404)
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return Response(json.dumps({"message":"Post id={0} was successfully deleted"}), mimetype="application/json", status=200)


    def get(self, id):
        # get the post based on the id
        post=Post.query.get(id)
        if not post:
            return Response(json.dumps({"message":"id={0} is invalid".format(id)}), mimetype="application/json", status=404)    
        
        user_ids=get_authorized_user_ids(self.current_user)
        if post.user_id not in user_ids:
            return Response(json.dumps({"message":"id={0} is invalid".format(id)}), mimetype="application/json", status=404)
        return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)
 
def initialize_routes(api):
    api.add_resource(
        PostListEndpoint, 
        '/api/posts', '/api/posts/', 
        resource_class_kwargs={'current_user': api.app.current_user}
    )
    api.add_resource(
        PostDetailEndpoint, 
        '/api/posts/<int:id>', '/api/posts/<int:id>/',
        resource_class_kwargs={'current_user': api.app.current_user}
    )