from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from sol_app.models import Solicitacao

@login_required
def dashboard_view(request ):

    query = Solicitacao.objects.all().count()
    query2 = Solicitacao.objects.filter(tipoos=1).count()
    total_solicitacoes = query
    return render(request, 'dashboard/dashboard.html', {'total_solicitacoes': total_solicitacoes, 'total_tipoos':query2})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
    # Redirect to a success page.
