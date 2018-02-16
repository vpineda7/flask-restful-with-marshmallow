## flask-restful-with-marshmallow
- [marshmallow docs](https://marshmallow.readthedocs.io/en/latest/index.html)  
marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
- [marshmallow require=True misunderstand](https://github.com/marshmallow-code/marshmallow/issues/736)  
when set `require=True`, Schema().load() will store error messages in error section
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/index.html)
flask-restful provide a easy way to build restful api for us

### MARSHMALLOW TIPS
#### dump vs dumps
- `dump` from dict/object to dict
- `dumps` from dict/object to json string

#### load vs loads
- `load` from dict to object
- `loads` from json string to object

#### filtering output
`Schema(only=("name","age"))`, when we pass `only` args, we can specify which filed we want to output
> you can also use `exclude` to exclude fileds

> note: set it this format 'only/exclude=("filed",)' when only filter one filed

#### dump_only and load_only
protect some data, like password(load_only) and creation_time(dump_only)
``` python
    created_at = fields.DateTime(dump_only=True)
    password = fields.Str(load_only=True)
```

#### set the result ordered
``` python
# create schema's meta class and set order=true
class SomeSchema(Schema):
    ...

    class Meta():
        ordered = True
```

#### Pre-processing and Post-processing Methods
- `pre_load`
- `post_load`
- `pre_dump`
- `post_dump`

### HOW TO TEST
``` bash
# GET
http://127.0.0.1/res

# POST
{
    "name": "Bob2",
    "phone": 93578747,
    "email": "bobtest2@email.com",
    "data": {
        "school": "some school2",
        "class": "some class2"
    }
}
http://127.0.0.1/res
```
