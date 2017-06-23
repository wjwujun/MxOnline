from django.db import models
from datetime import datetime
from organization.models import CourseOrg
# Create your models here.

class Courses(models.Model):
    course_org=models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True)
    name=models.CharField(max_length=50,verbose_name="课程名")
    desc=models.CharField(max_length=300,verbose_name="课程描述")
    detail=models.TextField(verbose_name="课程详情")
    degree=models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),verbose_name="课程难度",max_length=30)
    learn_time=models.IntegerField(default=0,verbose_name="学习时长(分钟数)")
    statudens=models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums=models.IntegerField(default=0,verbose_name="搜藏数")
    image=models.ImageField(upload_to="courses/%Y/%m",verbose_name="封面图",max_length=100)
    click_num=models.IntegerField(default=0,verbose_name="点击数")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    category=models.CharField(default='web后台',verbose_name="课程类型",max_length=300)

    class Meta:
        verbose_name="课程"
        verbose_name_plural=verbose_name
    #课程章节数
    def get_lession_num(self):
        return self.lession_set.all().count()

    #学习用户
    def get_learn_num(self):
        return self.usercourese_set.all()

    def __str__(self):
         return  self.name

class Lession(models.Model):
        courses=models.ForeignKey(Courses,verbose_name="课程")
        name=models.CharField(max_length=100,verbose_name="章节名")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

        class Meta:
            verbose_name = "章节"
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.name


class video(models.Model):
    lession = models.ForeignKey(Lession, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视屏名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "视屏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    courses = models.ForeignKey(Courses, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download=models.FileField(upload_to="courses/resource/%Y/%m",verbose_name="资源文件",max_length=100)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name






