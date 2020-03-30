from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import View
from .models import courses,reviews
from .forms import ReviewForm,ReviewUpdateForm
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.decorators import permission_required,login_required


def index(request):
    all_courses=courses.objects.all()
    context={
        'all_courses':all_courses,
    }
    return render(request,'course/index.html',context)
def detail(request,course_id):
    course=get_object_or_404(courses,pk=course_id)
    all_reviews = course.reviews_set.all()
    return render(request,'course/detail.html',{'course':course,'all_reviews':all_reviews})

class ReviewFormView(View):
    form_class = ReviewForm
    template_name ='course/reviews_form.html'

    def get(self,request,course_id):
        if not request.user.is_authenticated:
            messages.info(request, 'Please Login to Review ')
            return redirect('/accounts/login/')
        form=self.form_class(None)
        course=courses.objects.get(pk=course_id)
        return render(request,self.template_name,{'form':form,'course':course})

    def post(self,request,course_id):
        if not request.user.is_authenticated:
            messages.info(request, 'Please Login to Review ')
            return redirect('/accounts/login/')
        course = courses.objects.get(pk=course_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            anonymous = form.cleaned_data['anonymous']
            if anonymous:
                reviewer = 'Anonymous'
            else:
                reviewer = request.user.username
            review=reviews(course_name=course,reviewer=reviewer,rating=rating,comment=comment)
            review.save()
            messages.info(request, 'You reviewed '+str(course))
            return redirect('/course/')
        return render(request, self.template_name, {'form': form,'course':course})


class ReviewFormUpdate(View):
    form_class=ReviewUpdateForm
    template_name = 'course/update_form.html'

    def get(self,request,review_id,course_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        form=self.form_class(None)
        review=reviews.objects.get(pk=review_id)
        course=courses.objects.get(pk=course_id)
        return render(request,self.template_name,{'form':form,'course':course,'review':review})

    def post(self,request,review_id,course_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
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
        return render(request, self.template_name, {'form': form,'review':review})

class ReviewFormDelete(View):
    template_name='course/reviews_confirm_delete.html'
    def get(self,request,review_id,course_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
        course=courses.objects.get(pk=course_id)
        return render(request,self.template_name,{'course':course,'review':review})
    def post(self,request,review_id,course_id):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        review=reviews.objects.get(pk=review_id)
        course=courses.objects.get(pk=course_id)
        review.delete()
        messages.info(request, 'You deleted your review')
        return redirect('/course/')


class SearchView(ListView):
    model=courses
    template_name='course/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = courses.objects.filter(course_code__startswith=query)
            result = postresult
        else:
            result = None
        return result