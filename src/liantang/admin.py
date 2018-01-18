# encoding:utf-8

from __future__ import unicode_literals
from django.contrib import admin
from helpers.director.shortcut import TablePage,ModelTable,page_dc,FormPage,ModelFields,model_dc,regist_director,TabGroup
from .models import JianFangInfo,CunWei,Policy,ApplyTable,YinJiZhengGai
# Register your models here.
class JianFangInfoTablePage(TablePage):
    class JianFangInfoTable(ModelTable):
        model = JianFangInfo
        exclude=[]

class JianFangInfoFormPage(FormPage):
    ex_js=('/static/js/inputs_uis.pack.js',)
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


class YinJiTablePage(TablePage):
    class YinjiTable(ModelTable):
        model=YinJiZhengGai
        exclude=[]

class JianFangGroup(TabGroup):
    def get_tabs(self):
        pk =self.request.GET.get('pk')
        if pk:
            tabs =[{'name':'blockgroup_normal','label':'基本信息','page_cls':JianFangInfoFormPage},
                   {'name':'blockgroup_map','label':'应急整改','page_cls':YinJiTablePage}
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
    ex_js=('/static/js/inputs_uis.pack.js',)
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
    ex_js=('/static/js/inputs_uis.pack.js',)
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

page_dc.update({
    'liantang.jianfanginfo':JianFangInfoTablePage,
    'liantang.jianfanginfo.edit':JianFangGroup, #JianFangInfoFormPage,
    
    'liantang.cunwei':CunWeiTablePage,
    'liantang.cunwei.edit':CunWeiFormPage,
    'liantang.policy':PolicyTablePage,
    'liantang.policy.edit':PolicyFormPage,
    'liantang.applytable':ApplyTableTablePage,
    'liantang.applytable.edit':ApplyTableFormPage,
})