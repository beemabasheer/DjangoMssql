from django.shortcuts import get_object_or_404, redirect, render


from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView)
from SalesTeam.models import SalesTeam
from django.views.generic import TemplateView
from SalesTeam.forms import SalesTeamForm
from django.http import HttpResponseRedirect
from django.urls import reverse


from SalesTeam.serializers import SalesSerializers

class SalesList(ListAPIView):
    serializer_class = SalesSerializers
    def get_queryset(self):
        queryset = SalesTeam.objects.all()
        return queryset

class SalesCreate(CreateAPIView):
    serializer_class = SalesSerializers

    def perform_create(self,serializer):
        data = {}
        try:
            if serializer.is_valid(): 
                serializer.save()
                data['status'] = 'Sucess'
                data['message'] = 'Sales request created'
        except Exception as e:
            data['status'] = 'failed'
            data['message'] = 'something wrong'
        return Response(data)

def home(request):
    return render(request,'index.html')


class SalesTeamFormView(TemplateView):
    template_name = 'index.html'
    form_class = SalesTeamForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print(context)
        if context['form'].is_valid() :
            id = self.kwargs.get('id') or None
            obj_data = get_object_or_404(
                SalesTeam, pk=id) if id else None
            data = context['form'].save(SalesTeamForm,commit=False)
            # instance = form.save(commit=False)
            data.save(using='master')
           
            if self.kwargs.get('id'):
                message = 'Saved Successfully'
            else:
                message = 'Created Successfully'
            
            # return JsonResponse(
            #     {'status': 'success', 'message': message,},
            #     status=201, safe=False)
            return HttpResponseRedirect(reverse('sales.team.list'))

        print(context)
        return super(SalesTeamFormView, self).render(context)

    def get_context_data(self, **kwargs):
        context = super(SalesTeamFormView, self).get_context_data(**kwargs)

        # check id is present or not
        id = self.kwargs.get('id') or None

        obj = get_object_or_404(
            SalesTeam, pk=id) if id else None
        form = SalesTeamForm(self.request.POST or None,
                               instance=obj)
        context["form"] = form
        if 'id' in self.kwargs:
            context['id'] = self.kwargs.get('id')

        return context


def sales_team_view(request):

    columns_names = [f.name for f in SalesTeam._meta.get_fields()]
    queryset = SalesTeam.objects.using('master').all()
    context = { 
        'columns_names': columns_names,
        'queryset': queryset
    }
    return render(request, 'list.html', context)
