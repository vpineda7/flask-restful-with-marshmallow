import datetime

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import Schema, fields, post_load

app = Flask(__name__)
api = Api(app)

class ResObj(object):
    def __init__(self, name, created_at, phone=None, email=None, data=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.data = data
        self.created_at = created_at
        self.updated_at = datetime.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)
    
    @classmethod
    def make_resobj(cls, *args, **kwargs):
        created_at = datetime.datetime.now
        args = list(args)
        args[:-1].append(created_at)
        print (args)
        return cls(*args, **kwargs)


class ResSchema(Schema):
    name = fields.Str(
        required=True,
        error_messages={'required': {'message': 'name required', 'code': 400}}
        )
    phone = fields.Integer()
    email = fields.Email()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    data = fields.Dict()

    @post_load
    def make_res(self, data):
        return ResObj(**data)


class Res(Resource):
    def __init__(self):
        super(Res, self).__init__()

    def get(self):
        schema = ResSchema()
        result = schema.dump(res_obj)
        return result
    
    def post(self):
        schema = ResSchema(exclude=("created_at"))
        result = schema.load(request.json)
        if result.errors:
            result = result.errors
        result = schema.dump(result.data)
        return result


api.add_resource(Res, '/res')


if __name__ == '__main__':
    res_obj = ResObj.make_resobj(
            "Bob",
            datetime.datetime.now(),
            phone="93578746",
            email="bobtest@email.com",
            data={
                "school": "some school",
                "class": "some class"
                }
        )
    app.run(host="0.0.0.0", port=80, debug=True)