from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse
from django.db.models import Count, When, IntegerField, Case
from django.contrib.auth.decorators import login_required
from sol_app.models import Solicitacao


def consulta_status():
    contagens = Solicitacao.objects.aggregate(
        total_finalizadas=Count(Case(When(status='FI', then=1), output_field=IntegerField())),
        total_abertas=Count(Case(When(status='AB', then=1), output_field=IntegerField())),
        total_em_andamento=Count(Case(When(status='EA', then=1), output_field=IntegerField())),
        total_canceladas=Count(Case(When(status='CA', then=1), output_field=IntegerField())),
        )
    return contagens


@login_required
def dashboard_view(request):

    query = Solicitacao.objects.all().count()
    query2 = Solicitacao.objects.filter(tipoos=1).count()
    total_solicitacoes = query
    contagens = consulta_status()
    labels = ['Abertas', 'Em andamento', 'Finalizadas', "Canceladas"]
    print(contagens['total_abertas'])
    data = [contagens['total_abertas'], contagens['total_em_andamento'], contagens['total_finalizadas'], contagens['total_canceladas']]
    return render(
        request,
        "dashboard/dashboard.html",
        {
            "total_solicitacoes": total_solicitacoes,
            "total_tipoos": query2,
            "labels": labels,
            "data": data,
        },
    )


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
    # Redirect to a success page.
