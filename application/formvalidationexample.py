class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.        UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')
    def validate_username(self, username):
        username = username.data.lower()
        for x in ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', ',', '.', '/']:
            for char in username:
                if char == x:
                    raise ValidationError('Cannot user special characters in username')



class CharCheck:
    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.        self.banned = banned        if not message:
            message = 'Unable to use special characters' # If no message chosen, then this default message is returned.        self.message = message    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.        for x in field.data.lower():
            if x in (word.lower() for word in self.banned):
                raise ValidationError(self.message)
class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.        UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        CharCheck(message="Username cannot contain special chars", banned = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', ',', '.', '/']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')