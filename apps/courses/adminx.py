import  xadmin

from .models import Courses,Lession,video,CourseResource

class CoursesAdmin(object):
    list_display=['name','desc','detail','degree','learn_time','statudens','fav_nums','image','click_num','add_time']
    search_fields=['name','desc','detail','degree','learn_time','statudens','fav_nums','image','click_num']
    list_filter=['name','desc','detail','degree','learn_time','statudens','fav_nums','image','click_num','add_time']


class LessionAdmin(object):
    list_display = ['courses', 'name', 'add_time']
    search_fields = ['courses', 'name']
    list_filter = ['courses__name', 'name', 'add_time']

class videoAdmin(object):

    list_display = ['lession', 'name', 'add_time']
    search_fields = ['lession', 'name']
    list_filter = ['lession', 'name', 'add_time']

class CourseResourceAdmin(object):

    list_display = ['courses', 'name', 'download']
    search_fields = ['courses', 'name']
    list_filter = ['courses', 'name', 'download']


xadmin.site.register(Courses,CoursesAdmin)
xadmin.site.register(Lession,LessionAdmin)
xadmin.site.register(video,videoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)



