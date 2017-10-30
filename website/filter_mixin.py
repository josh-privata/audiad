"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView


class ListFilteredMixin(object):
    """Mixin that adds support for django-filter

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring

    filter_set = None

    def get_filter_set(self):
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
        if self.filter_set:
            return self.filter_set
        else:
            raise ImproperlyConfigured(
                "ListFilterMixin requires either a definition of "
                "'filter_set' or an implementation of 'get_filter()'")

    def get_filter_set_kwargs(self):
        """ Returns the keyword arguments for instanciating the filterset. """
        # todo Finish docstring
        return {
            'data': self.request.GET,
            'queryset': self.get_base_queryset(),
        }

    def get_base_queryset(self):
        """We can decided to either alter the queryset before or after applying the"""
        # todo Finish docstring
        return super(ListFilteredMixin, self).get_queryset()

    def get_constructed_filter(self):
        """We need to store the instantiated FilterSet cause we use it in
            get_queryset and in get_context_data
        """
        # todo Finish docstring
        if getattr(self, 'constructed_filter', None):
            return self.constructed_filter
        else:
            f = self.get_filter_set()(**self.get_filter_set_kwargs())
            self.constructed_filter = f
            return f

    def get_queryset(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return self.get_constructed_filter().qs

    def get_context_data(self, **kwargs):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        kwargs.update({'filter': self.get_constructed_filter()})
        return super(ListFilteredMixin, self).get_context_data(**kwargs)


class ListFilteredView(ListFilteredMixin, ListView):
    """A list view that can be filtered by django-filter

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

        """
    # todo Finish docstring
