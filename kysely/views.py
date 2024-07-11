from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Kysymys


# Create your views here.
def index(request):
    viimeisin_kysymys = Kysymys.objects.order_by('julkaisu_pvm')[:5]

    context = {
        'viimeisin_kysymys': viimeisin_kysymys
    }
    return render(request, "kysely/index.html", context)

def detail(request, question_id):
    kysymys = get_object_or_404(Kysymys, pk=question_id)
    return render(request, 'kysely/detail.html', {'kysymys': kysymys})

def results(request, question_id):
    kysymys= get_object_or_404(Kysymys, pk=question_id)
    return render(request, 'kysely/results.html', {'kysymys': kysymys})
def vote(request, question_id):
    kysymys = get_object_or_404(Kysymys, pk=question_id)
    try:
        valittu_vaihtoehto = kysymys.vaihtoehto_set.get(pk=request.POST['vaihtoehto'])
    except:
        return render(request, 'kysely/detail.html', {'kysymys': kysymys, 'error_message': 'Please, select a choice'})
    else:
        valittu_vaihtoehto.valinta += 1
        valittu_vaihtoehto.save()

        return HttpResponseRedirect(reverse('kysely:results', args=(kysymys.id,)))

