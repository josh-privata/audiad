"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from digg_paginator import DiggPaginator as Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, CreateView
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from music.models import Label
from music.tables import LabelTable
from music.forms import LabelForm


class Labels(View):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    def get(self, request, filter_by='all'):
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
        if not request.user.is_authenticated():
            return render(request, 'music/auth/login.html')
        else:
            page = request.GET.get('page', 1)
            try:
                label_ids = []
                labels = []
                for label in Label.objects.all():
                    label_ids.append(label.pk)
                    labels = Label.objects.filter(pk__in=label_ids)
                if filter_by == 'favorites':
                    labels = labels.filter(fav=True)
                paginate_labels = Paginator(labels, 20, body=3, margin=1, tail=1)
                try:
                    labels = paginate_labels.page(page)
                except PageNotAnInteger:
                    labels = paginate_labels.page(1)
                except EmptyPage:
                    labels = paginate_labels.page(paginate_labels.num_pages)
            except Label.DoesNotExist:
                labels = []
            return render(request, 'music/label/labels.html', {
                'label_list': labels,
                'filter_by': filter_by,
            })


class LabelList(ListView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/label/label_table.html'
    model = Label

    def get_context_data(self, **kwargs):
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
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            user = self.request.user
            context = super(LabelList, self).get_context_data(**kwargs)
            table = LabelTable(Label.objects.all())
            table.paginate(page=self.request.GET.get('page', 1), per_page=25)
            RequestConfig(self.request).configure(table)
            export_format = self.request.GET.get('_export', None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response('table.{}'.format(export_format))
            context['user'] = user
            context['table'] = table
            return context


class LabelDetailView(DetailView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    template_name = 'music/label/label_detail.html'
    model = Label

    def get_context_data(self, **kwargs):
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
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            user = self.request.user
            label = self.object
            context = super(LabelDetailView, self).get_context_data(**kwargs)
            context['label'] = label
            context['user'] = user
            return context


class LabelUpdate(UpdateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Label
    form_class = LabelForm
    template_name = 'music/label/label_update.html'

    def form_valid(self, form):
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
        label = form.save(commit=False)
        label.user = self.request.user
        label.save()
        return super(LabelUpdate, self).form_valid(form)


class LabelView(FormView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring


    template_name = 'music/label/label_create.html'
    form_class = LabelForm
    success_url = '/index/'

    def form_valid(self, form):
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
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            label = form.save(commit=False)
            label.user = self.request.user
            label.save()
            return super(LabelView, self).form_valid(form)


class LabelDelete(DeleteView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Label
    success_url = reverse_lazy('music:labels_list')
    template_name_suffix = '_delete'
    template_name = 'music/label/label_delete.html'


class LabelCreate(CreateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring

    model = Label
    form_class = LabelForm
    template_name = 'music/label/label_create.html'

    def form_valid(self, form):
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
        if not self.request.user.is_authenticated():
            return render(self.request, 'music/auth/login.html')
        else:
            label = form.save(commit=False)
            label.user = self.request.user
            #label.cover = request.FILES['cover']
            #file_type = label.cover.url.split('.')[-1]
            #file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
            #    context = {
            #        'label': label,
            #        'form': form,
            #        'error_message': 'Image file must be PNG, JPG, or JPEG',
            #    }
            #    return render(request, 'music/label_create.html', context)
            label.save()


def fav_label(request, label_id):
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
    label = get_object_or_404(Label, pk=label_id)
    if label.fav:
        label.fav = False
    else:
        label.fav = True
        label.save()
    labels = Label.objects.all()
    return render(request, 'music/label/labels.html', {'label': labels})
