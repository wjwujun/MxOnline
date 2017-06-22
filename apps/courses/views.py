from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import Courses
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class CourseListView(View):
    def get(self,request):
        all_course=Courses.objects.all()

        #排序
        sort=request.POST.get('sort',"")
        if sort:
             if sort=='students':
                all_course=all_course.order_by("-statudens")
             elif sort=='hot':
                 all_course=all_course.order_by("-click_num")

        #热门课程推荐
        all_hot = all_course.order_by("-click_num")[:2]

        # 对所有课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 3, request=request)
        orgs = p.page(page)

        return render(request,'course-list.html',{
            'all_course':orgs,
            'sort':sort,
            'all_hot':all_hot
        })

class CourseDetaileView(View):
    def get(self, request,course_id):
        course=Courses.objects.get(id=course_id)

        return  render(request,'course-detail.html',{
            'course':course
        })






