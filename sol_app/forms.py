from django import forms
from .models import Solicitacao
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column


class SolForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SolForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = 'AB'  # Defina o valor padrão aqui
        self.fields['status'].widget = forms.HiddenInput()
        self.fields['nome_equipe'].widget = forms.HiddenInput()
        self.fields['data_sol'].widget = forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'})
        self.helper = FormHelper(self)
        print('form')
        self.helper.layout = Layout(
            Row(
                Column('nome_referencia', css_class='col-md-4'),
                Column('nome_reduzido', css_class='col-md-4'),
            ),
            Row(
                Column('doc_sol', css_class='col-md-4'),
                Column('data_sol', css_class='col-md-4'),
            ),
            Row(
                Column('endereco', css_class='col-md-4'),
                Column('bairro', css_class='col-md-4'),
                Column('regiao', css_class='col-md-4'),
            ),
            Row(
                Column('setor', css_class='col-md-4'),
                Column('responsavel', css_class='col-md-4'),
                Column('contato', css_class='col-md-4'),
            ),
            Row(
                Column('tipoos', css_class='col-md-4'),
                Column('equipe_dpo', css_class='col-md-4'),
                # Column('nome_equipe', css_class='col-md-4'),
            ),
            # Row(
            #     Column('status', css_class='col-md-4'),
               
            # ),
        )