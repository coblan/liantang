from django.contrib import admin
from helpers.director.shortcut import page_dc
from liantang.models import JianFangInfo,YinJiZhengGai,JIAN_STATE,YINGJI_STATE
# Register your models here.
class HomePage(object):
    template='hello/home.html'
    def __init__(self,*args,**kw):
        pass
    
    def get_context(self):
        jianfang_total = JianFangInfo.objects.count()
        yinji_total=YinJiZhengGai.objects.count()
        state_list=[]
        yingji_state_list=[]
        for k,v in JIAN_STATE:
            count = JianFangInfo.objects.filter(state=k).count()
            state_list.append({'label':v,'count':count})
        for k,v in YINGJI_STATE:
            count = YinJiZhengGai.objects.filter(state=k).count()
            yingji_state_list.append({'label':v,'count':count })
        dc = {
            'jianfang_total':jianfang_total,
            'name':'hello',
            'state_list':state_list,
            'yinji_total':yinji_total,
            'yingji_state_list':yingji_state_list
        }
        return dc
    

page_dc.update({
    'home':HomePage
})