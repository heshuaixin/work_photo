from django.conf.urls import url
from . import views
urlpatterns = [
	# 首页
    url(r'^$', views.index,name="index"),
	# 相册管理路由
    # 图片信息浏览
    url(r'^photos/(?P<pIndex>[0-9]+)$',views.show,name="show"),
    # 上传图片
    	# 加载上传表单
    url(r'^photos/add$',views.add,name="add"),
    	# 执行上传操作
    url(r'^photos/insert$',views.insert,name="insert"),    
    # 删除图片
    url(r'^photos/del/(?P<uid>[0-9]+)$',views.delphoto,name="delphoto"),
    # 编辑图片信息
    	# 加载编辑表单
    url(r'^photos/edit/(?P<uid>[0-9]+)$',views.editphoto,name="editphoto"),
    	# 执行编辑操作
    url(r'^photos/update$',views.updatephoto,name="updatephoto"),
]
