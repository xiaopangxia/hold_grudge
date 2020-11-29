from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '记仇社区'
    site_title = '记仇社区管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')

