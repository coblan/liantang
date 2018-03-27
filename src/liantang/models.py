# encoding:utf-8

from __future__ import unicode_literals

from django.db import models
from helpers.base.jsonfield import JsonField

# Create your models here.
class CunWei(models.Model):
    """
    村委
    """
    name = models.CharField('村委',max_length=200)
    zhureng=models.CharField('主任',max_length=100,blank=True)
    phone=models.CharField('电话号码',max_length=100,blank=True)
    
    def __unicode__(self):
        return self.name or '未命名村委'
    class Meta:
        verbose_name='村委信息表'

JIAN_STATE=(
    (-1,'----'),
    (11,'村委会预审'),
    (1,'镇规保办初审'),
    (2,'联席会议审核'),
    (3,'联合审批(规保办)'),
    (4,'联合审批(规土所)'),
    (5,'联合审批(镇政府)'),
    (6,'联合审批(区规土所)'),
    (7,'镇村公示'),
    (8,'在建'),
    (9,'竣工审核'),
    (10,'完结')
)


class JianFangInfo(models.Model):
    """
    建房信息
    """
    name = models.CharField('姓名',max_length=100)
    date = models.DateField(verbose_name='申请日期', blank=True,null=True)
    cunwei = models.ForeignKey(CunWei,verbose_name='村委',on_delete=None,blank=True,null=True)
    addr = models.CharField('地址',max_length=500,blank=True)
    phone=models.CharField('电话号码',max_length=100,blank=True)
    state = models.IntegerField('当前流程',blank=True,choices=JIAN_STATE,default=-1)
    shenqing = models.TextField(verbose_name='申请材料',blank=True,default='{}')
    xieyi = models.TextField(verbose_name='协议',blank=True,help_text='支持PDF和图片')
    xiugai=models.TextField(verbose_name='申请修改',blank=True,help_text='支持PDF和图片')
    other =models.TextField(verbose_name='其他',blank=True,help_text='支持PDF和图片')
    
    def __unicode__(self):
        return "%s(建房申请)"%self.name
    class Meta:
        verbose_name='建房信息表'

    
YINGJI_STATE=(
    (1,'待处理'),
    (2,'已处理')
)

class YinJiZhengGai(models.Model):
    """
    应急整改
    """
    state = models.IntegerField('整改状态',blank=True,choices=YINGJI_STATE)
    date = models.DateField(verbose_name='日期',blank=True,null=True)
    desp = models.TextField(verbose_name='违规项目',blank=True)
    file = models.CharField('核定证明',max_length=500,blank=True)
    jianfang = models.ForeignKey(JianFangInfo,verbose_name='建房信息')

    def get_state(self):
        for k,v in YINGJI_STATE:
            if k==self.state:
                return v
    def __unicode__(self):
        return unicode(self.jianfang)+'.应急整改'
    class Meta:
        verbose_name='应急整改表'
            
class Policy(models.Model):
    """
    政策协议
    """
    name = models.CharField('名称',max_length=200,blank=True)
    desp = models.TextField(verbose_name='描述',blank=True)
    file = models.CharField('文件材料',max_length=500,blank=True,help_text='请选择PDF文件上传')
    
    def __unicode__(self):
        return self.name  or '未命名协议'
    class Meta:
        verbose_name='申请协议表'


class ApplyTable(models.Model):
    """
    申请表格
    """
    name = models.CharField('名称',max_length=200,blank=True)
    desp = models.TextField(verbose_name='描述',blank=True)
    file = models.CharField('文件材料',max_length=500,blank=True,help_text='请选择PDF文件上传')
    
    def __unicode__(self):
        return self.name   or '未命名表格'
    class Meta:
        verbose_name='申请表格表'
    
