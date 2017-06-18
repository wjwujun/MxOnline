from django.shortcuts import render
from   django.views.generic import  View

from .models import CourseOrg,CityDicrt

from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class OrgView(View):
    """"
        课程机构列表
    """
    def get(self,request):
        #所有课程机构
        all_orgs=CourseOrg.objects.all()

        #最热门的机构
        hot_orgs=all_orgs.order_by("-Click_nums")[:3]


        #所有城市
        all_citys=CityDicrt.objects.all()

        #筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
                all_orgs=all_orgs.filter(city_id=int(city_id))
        #筛选机构类别
        catgory = request.GET.get('ct', "")
        if catgory:
            all_orgs = all_orgs.filter(catgory=catgory)

        #排序,倒序
        sort= request.GET.get('sort', "")
        if sort:
            if sort=="students":
                all_orgs=all_orgs.order_by("-students")
            elif sort=="courses":
                all_orgs = all_orgs.order_by("-courese_nums")

        # 课程机构数量
        org_nums = all_orgs.count()

        #对课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,5, request=request)
        orgs = p.page(page)


        return  render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'catgory':catgory,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })

