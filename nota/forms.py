from django.forms import inlineformset_factory
from .custom_layout_object import *
from django import forms
from .models import Pai, Filho
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, Fieldset, MultiField


class PaiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset('Pessoa',
                     Row(
                         Column('nome', css_class='form-group col-md-6 mb-0'),
                         Column('telefone', css_class='form-group col-md-6 mb-0'),
                         css_class='form-row'
                     ),
                     'endereco'),
            Fieldset('Add Intems',
                     Formset('produtos')),
            Fieldset('Pagamento',
                     Field('pagamento'),
                     Field('total')),
            Submit('submit', 'Salvar')
        )

    class Meta:
        model = Pai
        fields = '__all__'


class FilhoFormSet(forms.ModelForm):
    class Meta:
        model = Filho
        fields = '__all__'


FilhoFormSet = inlineformset_factory(Pai, Filho, form=FilhoFormSet,
                                     fields=['produto', 'quantidade', 'valor', 'subtotal'],
                                     extra=2, can_delete=True)
