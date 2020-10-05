from flask_restful import fields

# Pet API model
pet = {
    'name': fields.String,
    'age': fields.String,
    'kind': fields.String,
    'name': fields.String,
    # 'created_at': fields.String(attribute='ts')# renaming attributes example
}
