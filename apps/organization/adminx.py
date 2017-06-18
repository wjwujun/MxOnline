import  xadmin

from .models import CityDicrt,CourseOrg,Teacher

class CityDicrtAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'city', 'location', 'image', 'desc', 'has_auth', 'Click_nums', 'fav_nums', 'address', 'add_time']
    search_fields = ['name', 'city', 'location', 'image', 'desc', 'has_auth', 'Click_nums', 'fav_nums', 'address']
    list_filter = ['name', 'city', 'location', 'image', 'desc', 'has_auth', 'Click_nums', 'fav_nums', 'address', 'add_time']

class TeacherAdmin(object):


    list_display = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums', 'add_time']
    search_fields =  ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums']
    list_filter =  ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'fav_nums', 'add_time']


xadmin.site.register(CityDicrt,CityDicrtAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)




