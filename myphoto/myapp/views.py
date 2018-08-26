from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Myphotos
from django.views.decorators.csrf import csrf_exempt
import time,os
from PIL import Image
from django.core.paginator import Paginator
# Create your views here.

# 主页
def index(request):
	return render(request,"myapp/index.html")

# 图片展示页面
def show(request,pIndex):
    list = Myphotos.objects.all()
    p = Paginator(list,4)
    # 默认看第一页数据
    if pIndex == "":
    	pIndex="1"
    list2 = p.page(int(pIndex))
    plist = p.page_range
    context = {"ulist":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request, 'myapp/show.html',context)

# 加载图片上传
def add(request):
	return render(request,"myapp/add.html")

# 取消POST验证
@csrf_exempt 

# 执行上传操作
def insert(request):
	'''执行图片的上传'''
	try:
	    myfile = request.FILES.get("mypic",None)
	    print(myfile)
	    if not myfile:
	        return HttpResponse("没有上传文件信息")
	    filename = str(time.time())+"."+myfile.name.split('.').pop()
	    destination = open("./static/pics/"+filename,"wb+")
	    for chunk in myfile.chunks():      # 分块写入文件  
	        destination.write(chunk)  
	    destination.close()

	    # 执行图片缩放
	    im = Image.open("./static/pics/"+filename)
	    # 缩放到75*75(缩放后的宽高比例不变):
	    im.thumbnail((75, 75))
	    # 把缩放后的图像用jpeg格式存: 
	    im.save("./static/pics/s_"+filename,None)
	    name = filename
	    # 将图片信息上传到数据库中
	    photo = Myphotos()
	    photo.title = myfile
	    photo.name = name
	    photo.save()
	    context = {"info":"添加成功"}
	except:
	    context = {"info":"添加失败"}
	return render(request,"myapp/info.html",context)	
	

# 删除操作
def delphoto(request,uid):
	try:
		ob = Myphotos.objects.get(id=uid)
		# 删除图片
		os.remove("./static/pics/"+ob.name)
		os.remove("./static/pics/s_"+ob.name)
		# 删除数据库中图片的信息
		ob.delete()
		context = {'info':'删除成功'}
	except Exception as err:
		print(err)
		context = {'info':'删除失败'}
	return render(request,"myapp/info.html",context)


# 加载编辑表单
def editphoto(request,uid):
	try:
		ob = Myphotos.objects.get(id=uid)
		context = {"photo":ob}
		return render(request,"myapp/edit.html",context)
	except Exception as err:
		print(err)
		context = {"info":"未找到要修改的图片"}
		return render(request,"myapp/info.html",context)

# 执行编辑操作
def updatephoto(request):
	try:
		ob = Myphotos.objects.get(id=request.POST['id'])
		ob.title = request.POST['title']
		ob.save()
		context = {"info":"修改成功"}
	except Exception as err:
		print(err)
		context = {"info":"修改成功"}
	return render(request,"myapp/info.html",context)