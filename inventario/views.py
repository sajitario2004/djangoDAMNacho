# -*- coding: utf-8 -*-
# vim:ts=4:expandtab:ai
# $Id: views.py 20 2025-11-27 21:10:24Z vic@gssi.es $

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


from .models import Tipo
from .models import Objeto
from .models import Ubicacion


class TipoList(LoginRequiredMixin, ListView):
    model = Tipo


class TipoDetail(LoginRequiredMixin, DetailView):
    model = Tipo


class TipoCreate(LoginRequiredMixin, CreateView):
    model = Tipo
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        form.instance.creadopor = self.request.user
        return super().form_valid(form)


class TipoUpdate(LoginRequiredMixin, UpdateView):
    model = Tipo
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        form.instance.modificadopor = self.request.user
        return super().form_valid(form)


class TipoDelete(LoginRequiredMixin, DeleteView):
    model = Tipo
    success_url = reverse_lazy("inventario:tipo-list")


class ObjetoList(LoginRequiredMixin, ListView):
    model = Objeto


class ObjetoDetail(LoginRequiredMixin, DetailView):
    model = Objeto


class ObjetoCreate(LoginRequiredMixin, CreateView):
    model = Objeto
    fields = ['tipo', 'etiqueta', 'nombre', 'ubicacion',  'descripcion']

    def form_valid(self, form):
        form.instance.creadopor = self.request.user
        return super().form_valid(form)


class ObjetoUpdate(LoginRequiredMixin, UpdateView):
    model = Objeto
    fields = ['tipo', 'etiqueta', 'nombre',  'descripcion']

    def form_valid(self, form):
        form.instance.modificadopor = self.request.user
        return super().form_valid(form)


class ObjetoDelete(LoginRequiredMixin, DeleteView):
    model = Objeto
    success_url = reverse_lazy("inventario:objeto-list")


class UbicacionList(LoginRequiredMixin, ListView):
    model = Ubicacion


class UbicacionDetail(LoginRequiredMixin, DetailView):
    model = Ubicacion


class UbicacionCreate(LoginRequiredMixin, CreateView):
    model = Ubicacion
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        form.instance.creadopor = self.request.user
        return super().form_valid(form)


class UbicacionUpdate(LoginRequiredMixin, UpdateView):
    model = Ubicacion
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        form.instance.modificadopor = self.request.user
        return super().form_valid(form)


class UbicacionDelete(LoginRequiredMixin, DeleteView):
    model = Ubicacion
    success_url = reverse_lazy("inventario:ubicacion-list")


