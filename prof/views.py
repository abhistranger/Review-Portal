from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import View
from .models import departments,professors,reviews
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ReviewForm,ReviewUpdateForm
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



def index(request):
    all_departments=departments.objects.all()
    all_profs=professors.objects.all()
    context={
        'all_profs':all_profs,
        'all_departments':all_departments,
    }
    return render(request,'prof/index.html',context)

def detail(request,professor_id):
    professor = get_object_or_404(professors,pk=professor_id)
    all_reviews=professor.reviews_set.all()
    context={
        'professor':professor,
        'all_reviews':all_reviews
    }
    return render(request,'prof/detail.html',context)


class ReviewFormView(View):
    form_class = ReviewForm
    template_name ='prof/reviews_form.html'

    def get(self,request,professor_id):
        if not request.user.is_authenticated:
            messages.info(request, 'Please Login to Review ')
            return redirect('/accounts/login/')
        form=self.form_class(None)
        professor=professors.objects.get(pk=professor_id)
        return render(request,self.template_name,{'form':form,'professor':professor})

    def post(self,request,professor_id):
        if not request.user.is_authenticated:
            messages.info(request, 'Please Login to Review ')
            return redirect('/accounts/login/')
        professor=professors.objects.get(pk=professor_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            rating= form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            anonymous=form.cleaned_data['anonymous']
            if anonymous:
                reviewer='Anonymous'
            else:
                reviewer=request.user.username
            review=reviews(prof=professor,reviewer=reviewer,rating=rating,comment=comment)
            review.save()
            messages.info(request, 'you reviewed '+str(professor))
            return redirect('/professor/')
        return render(request, self.template_name, {'form': form,'professor':professor})

class ReviewFormUpdate(View):
    form_class=ReviewUpdateForm
    template_name = 'course/update_form.html'

    def get(self,request,review_id,professor_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        form=self.form_class(None)
        review=reviews.objects.get(pk=review_id)
        professor=professors.objects.get(pk=professor_id)
        return render(request,self.template_name,{'form':form,'review':review,'professor':professor})

    def post(self,request,review_id,professor_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
        professor=professors.objects.get(pk=professor_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            review.rating = form.cleaned_data['rating']
            review.comment = form.cleaned_data['comment']
            anonymous = form.cleaned_data['anonymous']
            if anonymous:
                reviewer = 'Anonymous'
            else:
                reviewer = request.user.username
            review.reviewer=reviewer
            review.save()
            messages.info(request, 'You updated your review')
            return redirect('/course/')
        return render(request, self.template_name, {'form': form,'review':review,'professor':professor})

class ReviewFormDelete(View):
    template_name='course/reviews_confirm_delete.html'
    def get(self,request,review_id,professor_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
        professor=professors.objects.get(pk=professor_id)
        return render(request,self.template_name,{'professor':professor,'review':review})
    def post(self,request,review_id,professor_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
        professor=professors.objects.get(pk=professor_id)
        review.delete()
        messages.info(request, 'You deleted your review')
        return redirect('/course/')



class SearchView(ListView):
    model=professors
    template_name='prof/seach.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = professors.objects.filter(prof_name__startswith=query)
            result = postresult
        else:
            result = None
        return result

