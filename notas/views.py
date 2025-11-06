from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.db.models import F
from turmas.models import Disciplina # Assumindo que Disciplina está em turmas.models
from alunos.models import Aluno # Assumindo que Aluno está em alunos.models
from .models import Nota

def lancar_notas(request):
    # 1. Obter todas as disciplinas e alunos
    disciplinas = Disciplina.objects.all().order_by('nome')
    alunos = Aluno.objects.all().order_by('nome')
    
    # 2. Lógica de processamento do formulário (POST)
    if request.method == 'POST':
        disciplina_id = request.POST.get('disciplina_selecionada')
        
        if not disciplina_id:
            messages.error(request, "Por favor, selecione uma disciplina.")
            return redirect('notas:lancar_notas')

        try:
            disciplina = Disciplina.objects.get(pk=disciplina_id)
        except Disciplina.DoesNotExist:
            messages.error(request, "Disciplina não encontrada.")
            return redirect('notas:lancar_notas')

        # Usamos uma transação para garantir que todas as notas sejam salvas ou nenhuma seja
        with transaction.atomic():
            for aluno in alunos:
                # O nome do campo no POST será 'nota_aluno_ID'
                nota_str = request.POST.get(f'nota_aluno_{aluno.pk}', '').replace(',', '.')
                
                if nota_str:
                    try:
                        valor_nota = float(nota_str)
                        
                        # 3. Criar ou Atualizar a nota
                        # O get_or_create é ideal para garantir que só haja uma nota por aluno/disciplina
                        nota, created = Nota.objects.get_or_create(
                            aluno=aluno,
                            disciplina=disciplina,
                            defaults={'valor': valor_nota}
                        )
                        
                        if not created:
                            # Se a nota já existe, apenas atualiza o valor
                            nota.valor = valor_nota
                            nota.save()
                            
                    except ValueError:
                        messages.warning(request, f"Nota inválida para {aluno.nome}. Use números.")
                        # Continua para o próximo aluno
                        continue
                    except Exception as e:
                        messages.error(request, f"Erro ao salvar nota de {aluno.nome}: {e}")
                        # Continua para o próximo aluno
                        continue

        messages.success(request, f"Notas da disciplina '{disciplina.nome}' salvas com sucesso!")
        return redirect('notas:lancar_notas')

    # 4. Lógica de exibição do formulário (GET)
    
    # Para pré-preencher o formulário com notas existentes
    notas_existentes = {}
    if 'disciplina_selecionada' in request.GET:
        disciplina_id = request.GET.get('disciplina_selecionada')
        try:
            disciplina_selecionada = Disciplina.objects.get(pk=disciplina_id)
            
            # Busca todas as notas para a disciplina selecionada
            notas = Nota.objects.filter(disciplina=disciplina_selecionada)
            for nota in notas:
                notas_existentes[nota.aluno.pk] = nota.valor
                
        except Disciplina.DoesNotExist:
            pass # Ignora se a disciplina não existir

    context = {
        'disciplinas': disciplinas,
        'alunos': alunos,
        'notas_existentes': notas_existentes,
        'disciplina_selecionada_id': request.GET.get('disciplina_selecionada')
    }
    
    return render(request, 'notas/lancar_notas.html', context)

