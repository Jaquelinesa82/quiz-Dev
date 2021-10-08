from django.shortcuts import render, redirect

from base.forms import AlunoForm
from base.models import Pergunta, Aluno


def home(request):
    if request.method == 'POST':
        # Usúario já existe
        email = request.POST['email']
        try:
            aluno = Aluno.objects.get(email=email)
        except Aluno.DoesNotExist:
            # Usúario não existe
            formulario = AlunoForm(request.POST)
            if formulario.is_valid():
                aluno = formulario.save()
                return redirect('/perguntas/1')
            else:
                contexto = {'formulario': formulario}
                return render(request, 'base/home.html', contexto)
        else:
            request.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')
    return render(request, 'base/home.html')


def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(request, 'base/game.html', context=contexto)


def classificacao(request):
    return render(request, 'base/classificacao.html')
