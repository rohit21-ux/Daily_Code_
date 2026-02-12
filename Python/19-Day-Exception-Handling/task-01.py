class InvalidUsernameError(Exception):
    pass

def validate_username(username):
    if len(username) < 6:
        raise InvalidUsernameError("Username must be less than or equal to 6 characters!")
    return "Valid username"
    
try:
    print(validate_username("Shrinivas"))

except InvalidUsernameError as e:
    print("Invalild Username:",e)
