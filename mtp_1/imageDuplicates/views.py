from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from imageDuplicates.models import Entity_hi,entitySurfaceNames_hi,surfaceNames_hi,Mention_hi

# from .models import Question
# Create your views here.
class IndexView(generic.ListView):
    template_name='imageDuplicates/index2.html'
    # context_object_name = 'latest_question_list'
    def get_queryset(self):
        """return the last five published questions."""
        return Entity_hi.objects.order_by()[:]



# class ResultsView(generic.DetailView):
#     model=Question
#     template_name='imageDuplicates/results.html'    

# def vote(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice=question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         #redisplay the question voting form.
#         return render(request,'imageDuplicates/detail.html',{
#             'question' : question,
#             'error_message' : "you didn't select a choice."
#         })
#     else:
#         selected_choice.votes +=1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('imageDuplicates:results',args=(question.id,)))

def DetailView(request,pk):
    correct=entitySurfaceNames_hi.objects.select_related().filter(entityId=pk,label=0)
    wrong=entitySurfaceNames_hi.objects.select_related().filter(entityId=pk,label=1)
    # correct = entitySurfaceNames_hi.objects.select_related('surfaceNames_hi', 'Entity_hi').filter(entityId=1)
    context={'correct':correct, 'wrong':wrong}
    return render(request,"imageDuplicates/detail.html",context)

def search(request):
    query = request.GET['query']
    allEntity = Entity_hi.objects.filter(entityName__icontains=query)
    context = {'allEntity':allEntity}
    return render(request,"imageDuplicates/search.html",context)
    # return HttpResponse("this is my search page")

def VoteView(request,pk1,pk2):
    mapp=Mention_hi.objects.select_related().filter(dest_eid=pk1,mention_sid=pk2)
    context={'mention':mapp}
    return render(request,"imageDuplicates/vote.html",context)