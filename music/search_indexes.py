"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django.utils import timezone
from haystack import indexes
from .models import Album


class AlbumIndex(indexes.SearchIndex, indexes.Indexable):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        text (:obj): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return Album

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated.

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
        return self.get_model().objects.all()
