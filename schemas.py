from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    default_currency = fields.Str(validate=validate.Length(equal=3))

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    is_custom = fields.Bool()
    user_id = fields.Int()

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    date_time = fields.DateTime(dump_only=True)
    amount = fields.Float(required=True)
    currency = fields.Str(validate=validate.Length(equal=3))
