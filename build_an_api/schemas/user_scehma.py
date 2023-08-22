from main import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    password = ma.String(validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)