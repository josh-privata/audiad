"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from .models import Album
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Album)
def index_post(sender, instance, **kwargs):
    """docstring

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    # todo Finish docstring
    instance.indexing()
