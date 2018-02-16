import datetime

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import Schema, fields, post_load

app = Flask(__name__)
api = Api(app)


##########################################################################
# object will be serialized from and deserialize to
##########################################################################
class ResObj(object):
    """
    ResObj is resource object
    which stores resource information and data object which is ResDataObj instance
    """
    def __init__(self, name, phone=None, email=None, data=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.data = data
        self.created_at = self.check_created_at_exist_or_not()
        self.updated_at = datetime.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
    
    def check_created_at_exist_or_not(self):
        # here we can do some real check
        # if object already exist, return the original created_at
        # if not, return the time now
        return datetime.datetime.now()

class ResDataObj(object):
    """
    ResDataObj is resource data object
    which stores resource data belongs to ResObj
    """
    def __init__(self, school, class_num):
        self.school = school
        self.class_num = class_num


##########################################################################
# schema is the pipe function to serialize and deserialize
##########################################################################
class ResDataSchema(Schema):
    school = fields.Str()
    class_num = fields.Str(dump_to="class", load_from="class")

    class Meta():
        ordered = True



class ResSchema(Schema):
    # when set "required=True", An error will be stored if the the value is
    # missing from the input to Schema.load().
    name = fields.Str(
        required=True,
        error_messages={'required': {'message': 'name required', 'code': 400}}
        )
    phone = fields.Integer()
    email = fields.Email()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    data = fields.Nested(ResDataSchema)

    class Meta():
        ordered = True

    @post_load
    def new(self, data):
        return ResObj(**data)


##########################################################################
# Resource is flask-restful's class which can provide different
# function fitting to specified http method
##########################################################################
class Res(Resource):
    def __init__(self):
        super(Res, self).__init__()

    def get(self):
        schema = ResSchema()
        result = schema.dump(res_obj)
        return result
    
    def post(self):
        # schema = ResSchema(exclude=("created_at",))
        schema = ResSchema()
        result = schema.load(request.json)
        if result.errors:
            result = result.errors
        result = schema.dump(result.data)
        return result


api.add_resource(Res, '/res')


if __name__ == '__main__':
    # prepare data to be dump
    res_obj = ResObj(
            "Bob",
            phone="93578746",
            email="bobtest@email.com",
            data={
                "school": "some school",
                "class_num": "some class1"
                }
        )
    
    # run server
    app.run(host="0.0.0.0", port=80, debug=True)