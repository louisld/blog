import re

from wtforms.validators import StopValidation

class Slug:
    """
    Check that the input is a valid slug.

    This validator check that the ``data`` attribute on the field contains
    only lower case letter and dash character.

    :param message
        Error message raise in case of a validation error.
    """

    def __init__(self, message=None):
        self.message = message
    
    def __call__(self, form, field):
        if field.data and isinstance(field.data, str):
            d = field.data.strip()
            if re.match(r'^(?!.*--)[a-z-]+$', d):
                return
            
        if self.message is None:
            message = field.gettext("This is not a valid slug.")
        else:
            message= self.message

        field.errors[:] = []
        raise StopValidation(message)
