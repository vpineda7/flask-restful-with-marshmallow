import datetime

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)

class ResObj(object):
    def __init__(self, name, phone=None, email=None, data=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.data = data
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class ResSchema(Schema):
    name = fields.Str(
        required=True,
        error_messages={'required': {'message': 'name required', 'code': 400}}
        )
    phone = fields.Integer()
    email = fields.Email()
    create_at = fields.DateTime()
    data = fields.Dict()


class Res(Resource):
    def __init__(self):
        super(Res, self).__init__()
        self.res = ResObj(
            "Bob",
            phone="93578746",
            email="bobtest@email.com",
            data={
                "school": "some school",
                "class": "some class"
                }
        )

    def get(self):
        schema = ResSchema()
        result = schema.dump(self.res)
        return result
    
    def post(self):
        schema = ResSchema()
        result = schema.load(request.json)
        if result.errors:
            result = result.errors
        return result


api.add_resource(Res, '/res')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)