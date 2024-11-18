from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class FormSuccessViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_get_creation_context(self):
        response = self.client.get(reverse('form_success') + '?tipo_acao=Criado')
        self.assertContains(response, 'Criação')

    def test_get_alteration_context(self):
        response = self.client.get(reverse('form_success') + '?tipo_acao=Alteração')
        self.assertContains(response, 'Alteração')

class SolListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_list_view_context(self):
        response = self.client.get(reverse('sol_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('agora', response.context)
        self.assertEqual(response.context['agora'].date(), timezone.now().date())

class FormErrorViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_form_error_view(self):
        response = self.client.get(reverse('form_error'))
        self.assertContains(response, "Solicitação não pode ser excluída")

class FormSuccessDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_delete_success_view(self):
        response = self.client.get(reverse('delete_success') + '?tipo_acao=deletado')
        self.assertContains(response, 'Exclusão')


