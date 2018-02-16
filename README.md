## flask-restful-with-marshmallow
- [marshmallow docs](https://marshmallow.readthedocs.io/en/latest/index.html)  
marshmallow surpport load and dump method to switch between python data and http request data.
- [marshmallow require=True misunderstand](https://github.com/marshmallow-code/marshmallow/issues/736)  
when set `require=True`, Schema().load() will store error messages in error section
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/index.html)
flask-restful provide a easy way to build restful api for us

### marshmallow
#### dump vs dumps
- `dump` return dict
- `dumps` return json string

#### filtering output
`Schema(only=("name","age"))`, when we pass `only` args, we can specify which filed we want to output
> you can also use `exclude` to exclude fileds

> note: set it this format 'only/exclude=("filed",)' when only filter one filed

#### set the result ordered
``` python
# create schema's meta class and set order=true
class SomeSchema(Schema):
    ...
    
    class Meta():
        ordered = True
```

### test
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
