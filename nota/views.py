from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.db import transaction
from django.views.generic import CreateView
from .models import Pai, Filho
from .forms import PaiForm, FilhoFormSet
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
import pdfkit
from django.template.loader import render_to_string
from .process import html_to_pdf


class Base(View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)


class Forms(CreateView):
    model = Pai
    form_class = PaiForm
    template_name = 'form.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        data = super(Forms, self).get_context_data(**kwargs)
        if self.request.POST:
            data['produtos'] = FilhoFormSet(self.request.POST)
        else:
            data['produtos'] = FilhoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        produtos = context['produtos']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if produtos.is_valid():
                produtos.instance = self.object
                produtos.save()
        return super(Forms, self).form_valid(form)


class TestView(View):
    def get(self, *args, **kwargs):
        pais = Pai.objects.all()
        context = {
            "pais": pais,
        }

        return render(self.request, 'invoice-list.html', context)

    def view_pdf(request, id=None):
        pai = get_object_or_404(Pai, id=id)
        filho = pai.pai.all()

        context = {
            "company": {
                "name": "Ibrahim Services",
                "address": "67542 Jeru, Chatsworth, CA 92145, US",
                "phone": "(818) XXX XXXX",
                "email": "contact@ibrahimservice.com",
            },
            "nome": pai.nome,
            "telefone": pai.telefone,
            "endereco": pai.endereco,
            "pagamento": pai.pagamento,
            "total": pai.total,
            "filho": filho,

        }

        pdf = html_to_pdf('gerapdf.html', context)

        return HttpResponse(pdf, content_type='application/pdf')




