# encoding:utf-8

from __future__ import unicode_literals
from django.contrib import admin
from helpers.director.shortcut import TablePage,ModelTable,page_dc,FormPage,ModelFields,model_dc,regist_director,TabGroup,RowFilter
from .models import JianFangInfo,CunWei,Policy,ApplyTable,YinJiZhengGai
from helpers.maintenance.update_static_timestamp import js_stamp
# Register your models here.

class JianFangInfoTablePage(TablePage):
    template='liantang/jianfang.html'
    class JianFangInfoTable(ModelTable):
        model = JianFangInfo
        exclude=['shenqing','xieyi']
        def dict_row(self, inst):
            
            return {
                'cunwei':unicode(inst.cunwei),
                'yinji':inst.yinjizhenggai_set.last().get_state() if inst.yinjizhenggai_set.last() else ""
            }
        def get_heads(self):
            heads = super(self.__class__,self).get_heads()
            heads.append({
                'name':'yinji',
                'label':'应急整改'
                
            })
            return heads
        
    class JianfangFilter(RowFilter):
        model=JianFangInfo
        names=['cunwei','state','zhenggai']   
        range_fields =[{'name':'date','type':'date'}]
        
        def get_context(self):
            ls=super(self.__class__,self).get_context()
            option=[{'value':'has_zhenggai','label':'有违章'},
                    {'value':'no_zhenggai','label':'无违章'}]
            ls.append({'name':'zhenggai','label':'违章状态','options':option})
            return ls    
        
        def get_query(self, query):
            yinji = self.filter_args.pop('zhenggai',None)
            if yinji=='has_zhenggai':
                query = query.filter(yinjizhenggai__isnull=False)
            elif yinji=='no_zhenggai':
                query = query.filter(yinjizhenggai__isnull=True)
            return super(self.__class__,self).get_query(query)
        
    
    JianFangInfoTable.filters=JianfangFilter


class JianFangInfoFormPage(FormPage):
    ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
    template = 'liantang/jianfang_form.html'
    class JianFangInfoForm(ModelFields):
        class Meta:
            model = JianFangInfo
            exclude=[]
        
        def get_heads(self):
            heads = super(self.__class__,self).get_heads()
            heads.append({
                'name':'yinji',
                'type':'linetext',
                'label':'应急整改'
            })
            return heads
        
        def dict_head(self, head):
            if head['name']=='date':
                head['type']='date'
            elif head['name'] == 'state':
                head['orgin_order']=True
            return head


class YinJiTablePage(TablePage):
    template='liantang/yingji_tab.html'
    class YinjiTable(ModelTable):
        model=YinJiZhengGai
        exclude=['jianfang']
        # def __init__(self, *args,**kws):
            # super(self.__class__,self).__init__(*args,**kws)
        
        def inn_filter(self, query):
            jianfang_pk = self.kw.get('pk')
            jianfang = JianFangInfo.objects.get(pk = jianfang_pk)
            return query.filter(jianfang=jianfang)
            

class YinJiFormPage(FormPage):
    ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
    class YinjiForm(ModelFields):
        class Meta:
            model = YinJiZhengGai
            exclude =['jianfang']
        
        def __init__(self, *args,**kws):
            super(self.__class__,self).__init__(*args,**kws)
            if not(self.instance.pk):
                jianfang_pk = self.kw.get('jianfang_pk')
                jianfang = JianFangInfo.objects.get(pk = jianfang_pk)
                self.instance.jianfang = jianfang
            
        def dict_head(self, head):
            if head['name']=='date':
                head['type']='date'
            elif head['name']=='file':
                head['type'] = 'field-file-uploader'
            return head
        # def save_form(self):
            # self.kw

class JianFangGroup(TabGroup):
    def get_tabs(self):
        pk =self.request.GET.get('pk')
        if pk:
            jianfanginfo = JianFangInfo.objects.get(pk=pk)
            count = jianfanginfo.yinjizhenggai_set.count()
            tabs =[{'name':'blockgroup_normal','label':'基本信息','page_cls':JianFangInfoFormPage},
                   {'name':'blockgroup_map','label':'应急整改(%s)'%count,'page_cls':YinJiTablePage}
              ]
        else:
            tabs=[{'name':'blockgroup_normal','label':'基本信息','page_cls':JianFangInfoFormPage},]
        return tabs


class CunWeiTablePage(TablePage):
    class CunWeiTable(ModelTable):
        model = CunWei
        exclude = []

class CunWeiFormPage(FormPage):
    class CunWeiForm(ModelFields):
        class Meta:
            model = CunWei
            exclude =[]

class PolicyTablePage(TablePage):
    class PolicyTable(ModelTable):
        model = Policy
        exclude=[]
        
        def dict_row(self, inst):
            dc={
                'file':'<a href="%s" target="_blank">详情</a>'%inst.file if inst.file else ''
            }
            return dc        
        
class PolicyFormPage(FormPage):
    ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
    class PolicyForm(ModelFields):
        class Meta:
            model = Policy
            exclude = []
        def dict_head(self, head):
            if head['name'] == 'file':
                head['type'] = 'field-file-uploader'
                head['config']={
                    'accept':'.pdf',
                    'sortable':False,
                    'multiple':False
                }
            return head        

class ApplyTableTablePage(TablePage):
    class ApplyTable(ModelTable):
        model = ApplyTable
        exclude =[]
        
        def dict_row(self, inst):
            dc={
                'file':'<a href="%s" target="_blank">详情</a>'%inst.file if inst.file else ''
            }
            return dc
    

class ApplyTableFormPage(FormPage):
    ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
    class ApplyTableForm(ModelFields):
        class Meta:
            model = ApplyTable
            exclude = []
        def dict_head(self, head):
            if head['name'] == 'file':
                head['type'] = 'field-file-uploader'
                head['config']={
                    'accept':'.pdf',
                    'sortable':False,
                    'multiple':False
                }
            return head


model_dc[JianFangInfo] = {'fields':JianFangInfoFormPage.JianFangInfoForm}
model_dc[CunWei] = {'fields':CunWeiFormPage.CunWeiForm}
model_dc[Policy]={'fields':PolicyFormPage.PolicyForm}
model_dc[ApplyTable]={'fields':ApplyTableFormPage.ApplyTableForm}
model_dc[YinJiZhengGai]={'fields':YinJiFormPage.YinjiForm}

page_dc.update({
    'liantang.jianfanginfo':JianFangInfoTablePage,
    'liantang.jianfanginfo.edit':JianFangGroup, #JianFangInfoFormPage,
    
    'liantang.cunwei':CunWeiTablePage,
    'liantang.cunwei.edit':CunWeiFormPage,
    'liantang.policy':PolicyTablePage,
    'liantang.policy.edit':PolicyFormPage,
    'liantang.applytable':ApplyTableTablePage,
    'liantang.applytable.edit':ApplyTableFormPage,
    
    'liantang.yinji.edit':YinJiFormPage,
})