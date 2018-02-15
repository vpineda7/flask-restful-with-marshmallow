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
