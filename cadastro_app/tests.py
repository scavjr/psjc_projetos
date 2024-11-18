from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from cadastro_app.models import Cargos, Fases, Regioes, Setores

class CadastroViewsTest(TestCase):
    def setUp(self):
        # Criação de usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        # Criação de alguns registros para teste
        self.cargo = Cargos.objects.create(nome="Cargo 1", sigla="CG1")
        self.fase = Fases.objects.create(nome="Fase 1", sigla="F1")
        self.regiao = Regioes.objects.create(nome="Região 1", sigla="RG1")
        self.setor = Setores.objects.create(nome="Setor 1", sigla="ST1")

    def test_cadastros_list_view_status_code(self):
        """Teste para verificar se a página de lista de cadastros está acessível"""
        url = reverse('cadastros_list')  # Ajuste o nome da URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastro_app/cadastro_lista.html")

    def test_cadastro_view_get_existing_record(self):
        """Teste para verificar a renderização do formulário com um registro existente"""
        url = reverse('cadastro', kwargs={'id': self.cargo.id, 'nome_model': 'Cargos'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastro_app/cadastro.html")
        self.assertContains(response, self.cargo.nome)

    def test_cadastro_view_get_list(self):
        """Teste para verificar a lista de registros quando não há id fornecido"""
        url = reverse('cadastro', kwargs={'nome_model': 'Cargos'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cadastro_app/lista.html")
        self.assertContains(response, self.cargo.nome)