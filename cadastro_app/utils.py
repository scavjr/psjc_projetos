from django.apps import apps


def modelo(tabela):
    app_label, model_name = tabela.split('.')
    model_class = apps.get_model(app_label, model_name)
    return model_class
    

def obter_todos(tabela):
    model_class = modelo(tabela)
    todos_registros = model_class.objects.all()
    return todos_registros
