# encoding:utf-8
from __future__ import unicode_literals
from django.contrib import admin
from helpers.director.shortcut import page_dc
from liantang.models import JianFangInfo,YinJiZhengGai,JIAN_STATE,YINGJI_STATE
from django.utils.timezone import datetime
# Register your models here.
class HomePage(object):
    template='hello/home.html'
    def __init__(self,*args,**kw):
        pass
    
    def get_context(self):
        jianfang_total = JianFangInfo.objects.exclude(state=10).count()
        
        yinji_total = YinJiZhengGai.objects.count()
        yinji_wait = YinJiZhengGai.objects.filter(state=1).count()
        yinji_over = YinJiZhengGai.objects.filter(state=2).count()
        
        this_month = datetime.strftime(datetime.now(),'%Y-%m')
        yinji_this_month= YinJiZhengGai.objects.filter(date__startswith=this_month)
        yinji_this_month_total=yinji_this_month.count()
        
        state_list=[]
        yingji_state_list=[]
        
        for k,v in JIAN_STATE:
            if k==0 or k == 10:
                continue
            count = JianFangInfo.objects.filter(state=k).count()
            state_list.append({'label':v,'count':count,'key':k})
            
        for k,v in YINGJI_STATE:
            count = yinji_this_month.filter(state=k).count()
            yingji_state_list.append({'label':v,'count':count })
            
        dc = {
            'jianfang_total':jianfang_total,
            'name':'hello',
            'state_list':state_list,
            
            'yinji':{
                'total':yinji_total,
                'state_list':[
                    {'label':'待处理','count':yinji_wait,},
                    {'label':'已处理','count':yinji_over}
                    ],
                
                'this_month_total':yinji_this_month_total,
                'this_month_state_list':yingji_state_list
            }
            
        }
        return dc
    

page_dc.update({
    'home':HomePage
})