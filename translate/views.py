from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.http import JsonResponse
from tensorboard import program

from .models import InferForm
# from . import inference
from . import test


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'


class TranslateView(FormView):
    template_name = 'translate/index.html'
    form_class = InferForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


def translate(request):
    if request.method == 'POST':
        form = InferForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            return render(request, 'translate/index.html', context)
    else:
        form = InferForm()
        context = {'form': form}
        return render(request, 'translate/index.html', context)


def analysis(request):
    form = InferForm()
    context = {'form': form}
    return render(request, 'analysis/index.html', context)


def video(request):
    return redirect("https://www.youtube.com/watch?v=r9cDrA9BiU0&feature=youtu.be&ab_channel=H%C3%B9ngB%C3%B9iThanh")


# def getVal(request):
#     form = InferForm(request.GET)
#     form.data_infer = request.GET.get('infer')
#     result = inference.inference_word(None, None, None, None, form.data_infer)
#     data = {'trans': result}
#     return JsonResponse(data)


def testApi(request):
    form = InferForm(request.GET)
    form.data_infer = request.GET.get('infer')
    result = test.get_transalte(form.data_infer)
    data = {'trans': result}
    return JsonResponse(data)