"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

module_level_variable2 = 98765
"""int: Module level variable documented inline."""
# todo Finish docstring


def function_with_types_in_docstring(param1, param2):
    """docstring.


    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    # todo Finish docstring


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """docstring.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """
    # todo Finish docstring


def module_level_function(param1, param2=None, *args, **kwargs):
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


def example_generator(n):
    """docstring

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    # todo Finish docstring


class ExampleError(Exception):
    """docstring

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """
    # todo Finish docstring


class ExampleClass(object):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    def __init__(self, param1, param2, param3):
        """__init__ docstring

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """
        # todo Finish docstring

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""
        # todo Finish docstring

    @property
    def readonly_property(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring

        return 'readonly_property'


    def example_method(self, param1, param2):
        """docstring

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        # todo Finish docstring
