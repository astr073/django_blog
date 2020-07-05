from django.shortcuts import render, get_object_or_404, redirect, reverse

class ObjectDetailMixin:
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'object': obj,
                                                       'detail': True})

class ObjectCreateMixin:
    Form = None
    template = None

    def get(self, request):
        form = self.Form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.Form(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    Form = None
    template = None
    model = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.Form(instance=obj)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.Form(request.POST, instance=obj)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse('{}_lists_url'.format(self.model.__name__.lower())))
