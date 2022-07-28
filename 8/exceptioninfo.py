# -*- encoding: utf-8 -*-
# Author: li_colin

class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        default_message = 'This is a default message!'

        # if no arguments are passed set the first positional argument
        # to be the default message. To do that, we have to replace the
        # 'args' tuple with another one, that will only contain the message.
        # (we cannot do an assignment since tuples are immutable)
        # If you inherit from the exception that takes message as a keyword
        # maybe you will need to check kwargs here
        if not args: args = (default_message,)

        # Call super constructor
        super().__init__(*args, **kwargs)


raise CustomException({"1001": "password wrong!"})
