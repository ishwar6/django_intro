from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet

def home(request):
    context = {
        'a' : 'Homepage',
        'q' : 'Hey! we welcome you here'
    }

    return render(request, 'list/home.html', context )


def contact(request):
    context = {
        'a' : 'Contactpage',
        'q' : 'Hello! In case of any query feel free to connect with us'
    }
    return render(request, 'list/home.html', context)



class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course,
        data=data)
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course,
        id=pk,
        owner=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course,
                                    'formset': formset})
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course,
        'formset': formset})

    class ContentCreateUpdateView(TemplateResponseMixin, View):
        module = None
        model = None
        obj = None
        template_name = 'courses/manage/content/form.html'
        def get_model(self, model_name):
            if model_name in ['text', 'video', 'image', 'file']:
                return apps.get_model(app_label='courses',
            model_name=model_name)
            return None
        
        def get_form(self, model, *args, **kwargs):
            Form = modelform_factory(model, exclude=['owner',
                                                    'order',
                                                    'created',
                                                    'updated'])
            return Form(*args, **kwargs)
       
