from django.db import models
from datetime import  datetime
# Create your models here.


class CityDicrt(models.Model):
        name=models.CharField(max_length=200,verbose_name="城市")
        desc=models.CharField(max_length=200,verbose_name="描述")
        add_time=models.DateTimeField(default=datetime.now)

        class Meta:
                verbose_name="城市"
                verbose_name_plural=verbose_name

        def __str__(self):
            return self.name

class CourseOrg(models.Model):
       name=models.CharField(max_length=100,verbose_name="机构名称")
       desc=models.TextField(verbose_name="机构描述",blank=True,null=True)
       catgory=models.CharField(verbose_name="机构类别",default="pxjg",max_length=20,choices=(('pxjg','培训机构'),('gr','个人'),('gx','高校')))
       Click_nums=models.IntegerField(default=0,verbose_name="点击数")
       fav_nums = models.IntegerField(default=0, verbose_name="搜藏数")
       image=models.ImageField(upload_to="org/%Y/%m",verbose_name="封面图")
       address=models.CharField(max_length=100,verbose_name="机构地址")
       city=models.ForeignKey(CityDicrt,verbose_name="所在城市",blank=True,null=True)
       location=models.CharField(max_length=50,verbose_name="通讯详细地址")
       has_auth=models.BooleanField(verbose_name="是否认证",default=False)
       students=models.IntegerField(default=0,verbose_name="学习人数")
       courese_nums=models.IntegerField(default=0,verbose_name="课程数")
       add_time = models.DateTimeField(default=datetime.now)

       class    Meta:
           verbose_name="课程机构"
           verbose_name_plural=verbose_name

        # 获取教师人数
       def teacher_num(self):
            return self.teacher_set.all().count()

       def __str__(self):
           return self.name

class Teacher(models.Model):
        org=models.ForeignKey(CourseOrg,verbose_name="所属结构")
        image = models.ImageField(upload_to="org/teacher/%Y/%m", verbose_name="教师头像")
        name=models.CharField(max_length=50,verbose_name="教师名")
        work_year=models.IntegerField(default=0,verbose_name="工作年限")
        work_company=models.CharField(max_length=50,verbose_name="公司名称")
        work_position=models.CharField(max_length=50,verbose_name="公司职位")
        points=models.CharField(max_length=50,verbose_name="教学特点")
        fav_nums = models.IntegerField(default=0, verbose_name="搜藏数")
        add_time = models.DateTimeField(default=datetime.now)

        class Meta:
            verbose_name = "教师"
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.name










