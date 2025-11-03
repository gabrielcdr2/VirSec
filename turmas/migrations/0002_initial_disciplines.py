from django.db import migrations

def create_initial_disciplines(apps, schema_editor):
    Disciplina = apps.get_model('turmas', 'Disciplina') # Substitua 'curriculo' pelo nome da sua app
    
    disciplines = [
        "História",
        "Língua Portuguesa",
        "Matemática",
        "Geografia",
        "Ciências",
    ]
    
    for name in disciplines:
        Disciplina.objects.create(nome=name)

class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
        ('turmas', '0003_disciplina'), 

        ]

    operations = [
        migrations.RunPython(create_initial_disciplines),
    ]
