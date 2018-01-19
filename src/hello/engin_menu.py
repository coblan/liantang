# encoding:utf-8

from __future__ import unicode_literals

from helpers.director.engine import BaseEngine,page,fa,page_dc

class PcMenu(BaseEngine):
    url_name='liantang'
    brand = '练塘建房管理'
    menu=[
        {'label':'首页','url':page('home'),'icon':fa('fa-home')},
        {'label':'政策','icon':fa('fa-sitemap'),'submenu':[
            {'label':'政策协议','url':page('liantang.policy')},
            {'label':'申请表格','url':page('liantang.applytable')}
            ]},
        {'label':'建房信息','url':page('liantang.jianfanginfo'),'icon':fa('fa-building')},
        # {'label':'GIS区域','url':page('geoinfo.blockpolygon'),'icon':fa('fa-map-o')},
        # {'label':'区域组','url':page('geoinfo.blockgroup'),'icon':fa('fa-map-o')}
        {'label':'村委信息','url':page('liantang.cunwei'),'icon':fa('fa-life-ring')},
        
    ]

PcMenu.add_pages(page_dc)