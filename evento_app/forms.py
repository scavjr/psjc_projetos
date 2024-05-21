from django import forms
from evento_app.models import EventoRegistro
from sol_app.models import Solicitacao
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column


class EventoForm(forms.ModelForm):
    class Meta:
        model = EventoRegistro
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['data_evento'].widget = forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'})
        self.fields["descricao"].widget.attrs = {"row": 5}
        self.fields["solicitacao"].choices = [
            (item.id, item.nome_referencia) for item in Solicitacao.objects.all()
        ]
        # self.helper = FormHelper(self)
        # self.helper.layout = Layout(
        #     Modal(
        #             # email.help_text was set during the initalization of the django form field
        #             Field('email', placeholder="Email", wrapper_class="mb-0"),
        #             Button(
        #                 "submit",
        #                 "Send Reset Email",
        #                 id="email_reset",
        #                 css_class="btn-primary mt-3",
        #                 onClick="someJavasciptFunction()", # used to submit the form
        #             ),
        #             css_id="my_modal_id",
        #             title="This is my modal",
        #             title_class="w-100 text-center",
        #         )
# )
