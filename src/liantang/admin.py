# encoding:utf-8

from __future__ import unicode_literals
from django.contrib import admin
from helpers.director.shortcut import TablePage,ModelTable,page_dc,FormPage,ModelFields,model_dc,\
     regist_director,TabGroup,RowFilter,permit_list,has_permit
from .models import JianFangInfo,CunWei,Policy,ApplyTable,YinJiZhengGai
from helpers.maintenance.update_static_timestamp import js_stamp

# Register your models here.

class JianFangInfoTablePage(TablePage):
    template='liantang/jianfang.html'
    def get_path(self):
        path = [
            {'label':'建房信息','url':'/pc/xxx'}
        ]
        return path
    
    class JianFangInfoTable(ModelTable):
        model = JianFangInfo
        exclude=['shenqing','xieyi','xiugai','other']
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
            option=[
                    {'value':'no_zhenggai','label':'无整改'},
                    {'value':'zhenggai_ing','label':'整改中'},
                    {'value':'zhenggai_over','label':'已整改'},
            ]
            ls.append({'name':'zhenggai','label':'应急整改','options':option})
            for dc in ls:
                if dc['name']=='state':
                    dc['config']={
                        'orgin_order':True
                    }
                
            return ls    
        
        def get_query(self, query):
            yinji = self.filter_args.pop('zhenggai',None)
            if yinji=='no_zhenggai':
                query = query.filter(yinjizhenggai__isnull=True)
            elif yinji=='zhenggai_ing':
                query = query.filter(yinjizhenggai__isnull=False)
                query= query.filter(yinjizhenggai__state=1).distinct()
            elif yinji=='zhenggai_over':
                query = query.filter(yinjizhenggai__isnull=False)
                query = query.exclude(yinjizhenggai__state=1).distinct()
            # if yinji=='zhenggai_ing':
                # query = query.filter(yinjizhenggai__isnull=False)
                
            # if yinji=='has_zhenggai':
                # query = query.filter(yinjizhenggai__isnull=False)
            # elif yinji=='no_zhenggai':
                # query = query.filter(yinjizhenggai__isnull=True)
            return super(self.__class__,self).get_query(query)
        
    
    JianFangInfoTable.filters=JianfangFilter


class JianFangInfoFormPage(FormPage):
    # ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
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
                head['config']={
                    'orgin_order':True
                }
            return head
        
        def get_readonly_fields(self):
            readonly_fields = ModelFields.get_readonly_fields(self)
            # 只能首次修改
            if self.instance.pk and has_permit(self.crt_user,'liantang.-only_first_edit'):
                readonly_fields.extend(['name','date','cunwei','addr','phone','state'])
            return readonly_fields
        
        def get_context(self):
            ctx = ModelFields.get_context(self)
            if has_permit(self.crt_user,'liantang.-only_add'):
                ctx['only_add']=True
            return ctx
            
    

class YinJiTablePage(TablePage):
    template='liantang/yingji_tab.html'
    page_label='应急整改'

    class YinjiTable(ModelTable):
        model=YinJiZhengGai
        exclude=['jianfang','file']
        def __init__(self, *args,**kws):
            ModelTable.__init__(self,*args,**kws)
            jianfang_pk = self.kw.get('pk')
            self.jianfang = JianFangInfo.objects.get(pk = jianfang_pk)            
        
        def inn_filter(self, query):
            
            return query.filter(jianfang=self.jianfang)
            

class YinJiFormPage(FormPage):
    #ex_js=('/static/js/inputs_uis.pack.js?t=%s'%js_stamp.inputs_uis_pack_js,)
    template='liantang/yinji_form.html'
    class YinjiForm(ModelFields):
        class Meta:
            model = YinJiZhengGai
            exclude =['jianfang']
        
        def __init__(self, *args,**kws):
            super(self.__class__,self).__init__(*args,**kws)
            if not self.instance.pk and self.kw.has_key('jianfang_pk'):
                jianfang_pk = self.kw.get('jianfang_pk')
                jianfang = JianFangInfo.objects.get(pk = jianfang_pk)
                self.instance.jianfang = jianfang
            
        def dict_head(self, head):
            if head['name']=='date':
                head['type']='date'
            elif head['name']=='file':
                head['type'] = 'field-file-uploader'
            return head
        
        def get_readonly_fields(self):
            readonly_fields = ModelFields.get_readonly_fields(self)
            # 只能首次修改
            if self.instance.pk and has_permit(self.crt_user,'liantang.-only_first_edit'):
                readonly_fields.extend(['state','date','desp'])
            return readonly_fields  
        
        def get_context(self):
            ctx = ModelFields.get_context(self)
            if has_permit(self.crt_user,'liantang.-only_add'):
                ctx['only_add']=True
            return ctx
        

class JianFangGroup(TabGroup):
    def __init__(self, request):
        pk =request.GET.get('pk')
        if pk:
            self.jianfanginfo = JianFangInfo.objects.get(pk=pk)
        else:
            self.jianfanginfo =None
        TabGroup.__init__(self,request)
            
    def get_tabs(self):
        if self.jianfanginfo:
            count = self.jianfanginfo.yinjizhenggai_set.count()
            tabs =[{'name':'blockgroup_normal','label':'基本信息','page_cls':JianFangInfoFormPage},
                   {'name':'blockgroup_map','label':'应急整改(%s)'%count,'page_cls':YinJiTablePage}
              ]
        else:
            tabs=[{'name':'blockgroup_normal','label':'基本信息','page_cls':JianFangInfoFormPage},]
        return tabs
    
    def get_label(self):
        if self.jianfanginfo:
            return unicode(self.jianfanginfo)
        else:
            return '新建建房申请'


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
                'file':'<a href="%s" target="_blank">查看</a>'%inst.file if inst.file else ''
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
                'file':'<a href="%s" target="_blank">查看</a>'%inst.file if inst.file else ''
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

permit_list.append(CunWei)
permit_list.append(JianFangInfo)
permit_list.append(YinJiZhengGai)
permit_list.append(Policy)
permit_list.append(ApplyTable)
permit_list.append({'name':'liantang','label':'建房信息乱改约束',
                    'fields':[
                        {'name':'-only_add','label':'只能添加建房信息文件','type':'bool'},
                        {'name':'-only_first_edit','label':'只能首次编辑建房信息','type':'bool'},
                    ]
})

