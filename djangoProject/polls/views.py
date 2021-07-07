from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .import module2


def toLogin_view(request):
    return render(request,'login.html')
# def Login_view(request):
#     u=request.POST.get("user",'')
#     p=request.POST.get("pwd", '')
#
#     if u and p :
#         c=PollsStudentinfo.objects.filter(stu_name=u,stu_pwd=p).count()
#         if c>=1:
#             return HttpResponse("登录成功！")
#         else:
#             return HttpResponse("账号密码错误！")
#     else:
#         return HttpResponse("请输入正确的账号密码！")

# def toregister_view(request):
#     return render(request,'register.html')

def register_view(request):
    u = request.POST.get("username", '')
    p = request.POST.get("password", '')
    ph = request.POST.get("phone" ,'')
    id = request.POST.get("ID", '')
    agency=Agency.objects.filter(aname=u)
    print(u)
    print(p)
    print(ph)
    print(id)

    if agency and id=='agency':
        if User.objects.filter(username=u):
            context = {
                "hobby": "注册失败：重复用户名！"
            }
            return render(request, 'login.html', context=context)
        else:
            use = User(username=u, userphone=ph, password=p, userid=id)
            use.save()
            print("注册成功")
            context = {
                "hobby": "注册成功！"
            }
            return render(request, 'login.html', context=context)
    else:
        print("注册失败")
        context = {
            "hobby": "无此经办人！"
        }
    if id=='purchaser' :
        if User.objects.filter(username=u):
            context = {
                "hobby": "注册失败：重复用户名！"
            }
            return render(request, 'login.html', context=context)
        else:
            use=User(username=u,userphone=ph,password=p,userid=id)
            use.save()
            print("注册成功")
            context={
                "hobby":"注册成功！"
            }
            return render(request, 'login.html',context=context)
    else:
        print("注册失败")
        context = {
            "hobby": "请输入完整信息！"
        }
    return render(request, 'login.html', context=context)


def get_agency(request):
    s=request.POST.get("wd",'')          #从前端获取数据
    # print(s)
    agencys=Agency.objects.filter(ano=s)    #在数据库查找数据行
    uname = module2.b
    if agencys:                 #找到数据
        context = {
            "hobby": " 查到了",        #把数据传递给前端
            "username": uname,
            "agencys": agencys,
        }
    else:                   #没找到数据
        context = {
            "hobby": " 查无此人！",       #把数据传递给前端
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request, 'Agency.html', context=context)   #返回html界面
def MedicineSearch(request):
    p=request.POST.get("wb",'')
    # print(s)
    medicines=Medicine.objects.filter(mno=p)
    uname = module2.b
    if medicines:
        context1 = {
            "hobby": " 查到了",
            "username": uname,
            "medicines": medicines,
        }
    else:
        context1 = {
            "hobby": " 没找到！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'MedicineSearch.html',context=context1)
def ClinetSearch(request):
    p=request.POST.get("wa",'')
    # print(s)
    clinets=Clinet.objects.filter(cno=p)
    uname = module2.b
    if clinets:
        context1 = {
            "hobby": " 查到了",
            "clinets": clinets,
            "username": uname
        }
    else:
        context1 = {
            "hobby": " 没找到！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'Clinet.html',context=context1)
def Homepage(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'index.html',context=context)
def SearchAgency(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'SearchAgency.html',context=context)
def about(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'about.html',context=context)
def ToMedicine(request):
    uname = module2.b
    medicines=Medicine.objects.all().order_by("mno")
    context2={
        "hobby":"以下是所以药品信息",
        "medicines":medicines,
        "username": uname
    }
    return render(request, 'MedicineSearch.html',context=context2)
def ToAgencys(request):
    agencys=Agency.objects.order_by('ano')
    uname = module2.b
    for agency in agencys:
        print(agency.ano)
    context={
        "hobby":"以下是经办人信息",
        "agencys":agencys,
        "username": uname
    }
    return render(request, 'Agency.html', context=context)
def ToClinet(request):
    clinets=Clinet.objects.all().order_by("cno")
    uname = module2.b
    context={
        "hobby":"以下是顾客信息",
        "clinets":clinets,
        "username": uname
    }
    return render(request,'Clinet.html',context=context)
def SetAgency(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'SetAgency.html',context=context)
def Setagency(request):
    an = request.POST.get("ano", '')
    asx = request.POST.get("asex", '')
    anme = request.POST.get("aname", '')
    apone = request.POST.get("aphone", '')
    amark= request.POST.get("aremark", '')
    agencys=Agency.objects.order_by()
    uname = module2.b
    if an and asx and anme and apone and amark :
            for agency in agencys :
                print(agency.ano)
                if agency.ano==an:
                    context={
                        "hobby":"经办人编号重复！",
                        "username":uname
                    }
                    return render(request,'SetAgency.html',context=context)

            atu = Agency(ano=an, asex=asx, aname=anme, aphone=apone, aremark=amark)
            atu.save()
            context = {
                 "hobby": "添加成功！",
                 "username": uname
             }
            return render(request, 'SetAgency.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'SetAgency.html', context=context)
def SetClient(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'SetClient.html',context=context)
def Setclient(request):
    cn = request.POST.get("cno", '')
    csx = request.POST.get("csex", '')
    cnme = request.POST.get("cname", '')
    cpone = request.POST.get("cphone", '')
    cge = request.POST.get("cage", '')
    cdess = request.POST.get("caddress", '')
    csy = request.POST.get("csymptom", '')
    mn = request.POST.get("mno", '')
    an = request.POST.get("ano", '')
    cd = request.POST.get("cdate", '')
    cmark = request.POST.get("cremark", '')
    cou=request.POST.get("cmcount", '')
    uname = module2.b
    medicines = Medicine.objects.filter(mno=mn)
    clients=Clinet.objects.order_by()
    if an and csx and cnme and cpone and cmark and cn and cge and csy and cdess and mn and cd and cou:
            for client in clients :
                print(client.cno)
                if client.cno==cn:
                    context={
                        "hobby":"顾客编号重复！",
                        "username": uname
                    }
                    return render(request,'SetClient.html',context=context)
                if medicines.mcount < cou:
                    context = {
                        "hobby": "药品库存不足！",
                        "username": uname
                    }
                    return render(request, 'SetClient.html', context=context)
            atu = Clinet(cno=cn,cname=cnme,csex=csx,cphone=cpone,cage=cge,caddress=cdess,csymptom=csy,mno=mn,ano=an,cdate=cd,cremark=cmark,cmcount=cou)
            atu.save()
            context = {
                 "hobby": "添加成功！",
                "username": uname
             }
            return render(request, 'SetClient.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'SetClient.html', context=context)

def SetMedicine(request):
    uname = module2.b
    context={
        "username":uname
    }
    return render(request, 'SetMedicine.html',context=context)
def Setmedicine(request):
    mn = request.POST.get("mno", '')
    uname = module2.b
    mnme = request.POST.get("mname", '')
    mmod = request.POST.get("mmode", '')
    mef= request.POST.get("mefficacy", '')
    mcou=request.POST.get("mcount", '')
    medicines=Medicine.objects.order_by('mno')
    if mn and mnme and mmod and mef and mcou   :
            for medicine in medicines :
                print(medicine.mno)
                if medicine.mno==mn:
                    context={
                        "hobby":"药品编号重复！",
                        "username": uname
                    }
                    return render(request,'SetMedicine.html',context=context)

            atu = Medicine(mno=mn,mname=mnme,mmode=mmod,mefficacy=mef,mcount=mcou)
            atu.save()
            context = {
                 "hobby": "添加成功！",
                 "username": uname

             }
            return render(request, 'SetMedicine.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'SetMedicine.html', context=context)
def PolishAgency(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'PolishAgency.html',context=context)
def get_Agency(request):

    s=request.POST.get("wd",'')
    print("执行查询")
    module2.print_a(s)
    print("s=",s)
    uname = module2.b
    agencys=Agency.objects.filter(ano=s)



    if agencys:
        context = {
            "hobby": " 查到了",
            "agencys": agencys,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'PolishAgency.html',context=context)

def Polishagency(request):

    p_ano=request.POST.get("p_ano",'')
    p_aname = request.POST.get("p_aname", '')
    p_asex = request.POST.get("p_asex", '')
    p_aphone = request.POST.get("p_aphone", '')
    p_aremark = request.POST.get("p_aremark", '')
    print("执行修改")
    print(p_ano)
    print(p_aname)
    print(p_asex)
    print(p_aphone)
    print(p_aremark)
    p= module2.a
    uname = module2.b
    print("p=",p)
    if p_ano:
        Agency.objects.filter(ano=p).update(ano=p_ano)
        if p_aname:
            Agency.objects.filter(ano=p_ano).update(aname=p_aname)
        if p_asex:
            Agency.objects.filter(ano=p_ano).update(asex=p_asex)
        if p_aphone:
            Agency.objects.filter(ano=p_ano).update(aphone=p_aphone)
        if p_aremark:
            Agency.objects.filter(ano=p_ano).update(aremark=p_aremark)
    if p_aname:
        Agency.objects.filter(ano=p).update(aname=p_aname)
    if p_asex:
        Agency.objects.filter(ano=p).update(asex=p_asex)
    if p_aphone:
        Agency.objects.filter(ano=p).update(aphone=p_aphone)
    if p_aremark:
        Agency.objects.filter(ano=p).update(aremark=p_aremark)
    context={
        "hobby": "修改成功",
        "username":uname
    }
    return render(request, 'PolishAgency.html', context=context)


def PolishMedicine(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'PolishMedicine.html',context=context)


def get_Medicine(request):
    s = request.POST.get("wd", '')
    print("执行查询")
    module2.print_a(s)
    print("s=", s)
    uname = module2.b
    medicines = Medicine.objects.filter(mno=s)

    if medicines:
        context = {
            "hobby": " 查到了",
            "medicines": medicines,
            "username": uname
        }
    else:
        context = {
            "hobby": " 无药品信息！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return render(request, 'PolishMedicine.html', context=context)


def Polishmedicine(request):
    p_mno = request.POST.get("p_mno", '')
    p_mname = request.POST.get("p_mname", '')
    p_mmode = request.POST.get("p_amode", '')
    p_mefficacy = request.POST.get("p_mefficacy", '')
    p_mcount= request.POST.get("p_mcount", '')
    uname = module2.b
    print("执行修改")

    p = module2.a

    print("p=", p)
    if p_mno:
        Medicine.objects.filter(mno=p).update(mno=p_mno)
        if p_mname:
            Medicine.objects.filter(mno=p_mno).update(mname=p_mname)
        if p_mmode:
            Medicine.objects.filter(mno=p_mno).update(mmode=p_mmode)
        if p_mefficacy:
            Medicine.objects.filter(mno=p_mno).update(mefficacy=p_mefficacy)
        if p_mcount:
            Medicine.objects.filter(mno=p_mno).update(mcount=p_mcount)

    if p_mname:
        Medicine.objects.filter(mno=p).update(mname=p_mname)
    if p_mmode:
        Medicine.objects.filter(mno=p).update(mmode=p_mmode)
    if p_mefficacy:
        Medicine.objects.filter(mno=p).update(mefficacy=p_mefficacy)
    if p_mcount:
        Medicine.objects.filter(mno=p).update(mcount=p_mcount)
    context = {
        "hobby": "修改成功",
        "username": uname
    }
    return render(request, 'PolishMedicine.html', context=context)

def PolishClient(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'PolishClient.html',context=context)


def get_Client(request):
    p=request.POST.get("wd",'')
    # print(s)
    clinets=Clinet.objects.filter(cno=p)
    uname = module2.b
    if clinets:
        context1 = {
            "hobby": " 查到了",
            "clinets": clinets,
            "username": uname
        }
    else:
        context1 = {
            "hobby": " 没找到！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'PolishClient.html',context=context1)


def Polishclient(request):
    p_cno = request.POST.get("p_cno", '')
    p_cname = request.POST.get("p_cname", '')
    p_csex = request.POST.get("p_csex", '')
    p_cage = request.POST.get("p_cage", '')
    p_caddress = request.POST.get("p_caddress", '')
    p_cphone = request.POST.get("p_phone", '')
    p_csymptom = request.POST.get("p_csymptom", '')
    p_mno = request.POST.get("p_mno", '')
    p_ano = request.POST.get("p_ano", '')
    p_cdate = request.POST.get("p_cdate", '')
    p_cremark = request.POST.get("p_cremark", '')
    p_cmcount=request.POST.get("p_cmcount", '')
    print("执行顾客信息修改")

    p = module2.a
    uname = module2.b
    print("p=", p)
    if p_cno:
        Medicine.objects.filter(cno=p).update(cno=p_mno)
        if p_cname:
            Clinet.objects.filter(cno=p_cno).update(cname=p_cname)
        if p_csex:
            Clinet.objects.filter(cno=p_cno).update(csex=p_csex)
        if p_cage:
            Clinet.objects.filter(cno=p_cno).update(cage=p_cage)
        if p_caddress:
            Clinet.objects.filter(cno=p_cno).update(caddress=p_caddress)
        if p_cphone:
            Clinet.objects.filter(cno=p_cno).update(cphone=p_cphone)
        if p_csymptom:
            Clinet.objects.filter(cno=p_cno).update(csymptom=p_csymptom)
        if p_mno:
            Clinet.objects.filter(cno=p_cno).update(mno=p_mno)
        if p_ano:
            Clinet.objects.filter(cno=p_cno).update(ano=p_ano)
        if p_cdate:
            Clinet.objects.filter(cno=p_cno).update(cdate=p_cdate)
        if p_cremark:
            Clinet.objects.filter(cno=p_cno).update(cremark=p_cremark)
        if p_cmcount:
            Clinet.objects.filter(cno=p_cno).update(cmcount=p_cmcount)

    if p_cname:
        Clinet.objects.filter(cno=p).update(cname=p_cname)
    if p_csex:
        Clinet.objects.filter(cno=p).update(csex=p_csex)
    if p_cage:
        Clinet.objects.filter(cno=p).update(cage=p_cage)
    if p_caddress:
        Clinet.objects.filter(cno=p).update(caddress=p_caddress)
    if p_cphone:
        Clinet.objects.filter(cno=p).update(cphone=p_cphone)
    if p_csymptom:
        Clinet.objects.filter(cno=p).update(csymptom=p_csymptom)
    if p_mno:
        Clinet.objects.filter(cno=p).update(mno=p_mno)
    if p_ano:
        Clinet.objects.filter(cno=p).update(ano=p_ano)
    if p_cdate:
        Clinet.objects.filter(cno=p).update(cdate=p_cdate)
    if p_cremark:
        Clinet.objects.filter(cno=p).update(cremark=p_cremark)
    if p_cmcount:
        Clinet.objects.filter(cno=p).update(cmcount=p_cmcount)
    context = {
        "hobby": "修改成功",
         "username":uname

    }
    return render(request, 'PolishClient.html', context=context)





def DeleteAgency(request):
    agencys = Agency.objects.order_by('ano')
    uname = module2.b
    for agency in agencys:
        print(agency.ano)
    context = {
        "hobby": "以下是经办人信息",
        "agencys": agencys,
        "username": uname
    }
    return render(request, 'DeleteAgency.html', context=context)
def Deleteagency(request):
    agencys = Agency.objects.order_by('ano')
    ags = request.POST.getlist('ag', [])
    clients=Clinet.objects.all()
    uname = module2.b
    for agency in agencys:
        for ag in ags:
            for client in clients:
                if Clinet.objects.filter(ano=ag):
                    context={
                        "hobby":"非法删除！该经办人曾服务过顾客",
                        "username":uname
                    }
                    return render(request, 'DeleteAgency.html',context=context)
                if( Agency.objects.filter(ano=ag).delete()):

                    context={
                        "hobby":"删除成功",
                        "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                        "username": uname

                    }
    return render(request, 'DeleteAgency.html',context=context)
def get_DeleteAgency(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)
    uname = module2.b

    agencys=Agency.objects.filter(ano=s)



    if agencys:
        context = {
            "hobby": " 查到了",
            "agencys": agencys,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'DeleteAgency.html',context=context)
def DeleteMedicine(request):
    medicines= Medicine.objects.order_by('mno')
    uname = module2.b
    # for agency in agencys:
    #     print(agency.ano)
    context = {
        "hobby": "以下是药品信息",
        "medicines": medicines,
        "username": uname
    }
    return render(request, 'DeleteMedicine.html', context=context)
def Deletemedicine(request):
    medicines = Medicine.objects.order_by('mno')
    mes = request.POST.getlist('me', [])
    clients=Clinet.objects.all()
    uname = module2.b
    for medicine in medicines:
        for me in mes:
            for client in clients:
                if Clinet.objects.filter(mno=me):
                    context={
                        "hobby":"非法删除！该药品已经被顾客购买"
                    }
                    return render(request,  'DeleteMedicine.html',context=context)
                if( Medicine.objects.filter(mno=me).delete()):

                    context={
                        "hobby":"删除成功",
                        "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                        "username":uname
                    }
    return render(request, 'DeleteMedicine.html',context=context)
def get_DeleteMedicine(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)
    uname = module2.b

    medicines=Medicine.objects.filter(mno=s)



    if medicines:
        context = {
            "hobby": " 查到了",
            "medicines": medicines,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此药！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'DeleteMedicine.html',context=context)
def DeleteClient(request):
    clients = Clinet.objects.order_by('cno')
    uname = module2.b
    # for client in clients:
    #     print(client.cno)
    context = {
        "hobby": "以下是顾客信息",
        "clinets": clients,
        "username": uname

    }
    return render(request, 'DeleteClient.html', context=context)
def Deleteclient(request):
    clients = Clinet.objects.order_by('cno')
    ags = request.POST.getlist('ag', [])
    uname = module2.b
    for client in clients:
        for ag in ags:
                if( Clinet.objects.filter(cno=ag).delete()):

                    context={
                        "hobby":"删除成功",
                         "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                         "username":uname
                    }
    return render(request, 'DeleteClient.html',context=context)
def get_DeleteClient(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)

    uname = module2.b
    clients=Clinet.objects.filter(cno=s)



    if clients:
        context = {
            "hobby": " 查到了",
            "clinets": clients,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'DeleteClient.html',context=context)
def AgencyPrint(request):
    uname = module2.b
    agencys = Agency.objects.order_by('ano')
    sex=0
    sex1=0
    count=0
    for agency in agencys:
        count=count+1
        if(agency.asex=='男'):
         sex=sex+1
    sex1=count-sex
    context = {
            "hobby": "以下是经办人信息",
            "agencys": agencys,
            "count":count,
            "sex":sex,
            "sex1":sex1,
            "username": uname
        }

    return render(request, 'AgencyPrint.html',context=context)
def ClientPrint(request):
    uname = module2.b
    clients = Clinet.objects.order_by('cno')
    sex=0
    sex1=0
    count=0
    for client in clients:
        count=count+1
        if(client.csex=='男'):
         sex=sex+1
    sex1=count-sex
    context = {
            "hobby": "以下是顾客信息",
            "clinets": clients,
            "count":count,
            "sex":sex,
            "sex1":sex1,
            "username": uname
        }

    return render(request, 'ClientPrint.html',context=context)
def MedicinePrint(request):
    uname = module2.b
    medicines = Medicine.objects.order_by('mno')
    sex=0
    sex1=0
    count=0
    for medicine in medicines:
        count=count+1
        if(medicine.mmode=='外用'):
         sex=sex+1
    sex1=count-sex
    context = {
            "hobby": "以下是药品信息",
            "medicines": medicines,
            "count":count,
            "sex":sex,
            "sex1":sex1,
            "username": uname
        }

    return render(request, 'MedicinePrint.html',context=context)
def Search_Agency(request):
    s=request.POST.get("wb1",'')
    w = request.POST.get("wb2", '')
    uname=module2.b
    if s:
        agencys=Agency.objects.filter(ano=s)
        print("s")
        if agencys:
            context = {
                "hobby": " 查到了",
                "agencys": agencys,
                "username": uname
            }
        else:
            context = {
                "hobby": " 查无此人！",
                "username": uname
            }
        return render(request, 'SearchAgency.html', context=context)
    if w:
        print("w")
        agencys = Agency.objects.filter(aname=w)

        if agencys:
            context = {
                "hobby": " 查到了",
                "agencys": agencys,
            }
        else:
            context = {
                "hobby": " 查无此人！",
            }
        return render(request, 'SearchAgency.html', context=context)
    # return HttpResponse("信息表")
def Search_Medicine(request):
    s=request.POST.get("wb1",'')
    w = request.POST.get("wb2", '')
    uname = module2.b
    if s:
        medicines=Medicine.objects.filter(mno=s)
        print("s")
        if medicines:
            context = {
                "hobby": " 查到了",
                "medicines": medicines,
                "username": uname
            }
        else:
            context = {
                "hobby": " 没有找到！",
                "username": uname
            }
        return render(request, 'SearchMedicine.html', context=context)
    if w:
        print("w")
        medicines=Medicine.objects.filter(mname=w)

        if medicines:
            context = {
                "hobby": " 查到了",
                "medicines": medicines,
            }
        else:
            context = {
                "hobby": " 没有找到！",
            }
        return render(request, 'SearchMedicine.html', context=context)
    # return HttpResponse("信息表")
def SearchMedicine(request):
    uname=module2.b
    context={
        "username":uname
    }
    return render(request, 'SearchMedicine.html',context=context)
def Search_Client(request):
    s=request.POST.get("wb1",'')
    w = request.POST.get("wb2", '')
        # print(s)
    uname = module2.b

    if s:
        clients=Clinet.objects.filter(cno=s)
        print("s")
        if clients:
            context = {
                "hobby": " 查到了",
                "clinets": clients,
                "username": uname
            }
        else:
            context = {
                "hobby": " 没有找到！",
                "username": uname
            }
        return render(request, 'SearchClient.html', context=context)
    if w:
        print("w")
        clients=Clinet.objects.filter(cname=w)

        if clients:
            context = {
                "hobby": " 查到了",
                "clinets": clients,
            }
        else:
            context = {
                "hobby": " 没有找到！",
            }
        return render(request, 'SearchClient.html', context=context)
    # return HttpResponse("信息表")
def SearchClient(request):
    uname=module2.b
    context={
        "username":uname
    }
    return render(request, 'SearchClient.html',context=context)
def login(request):
    u=request.POST.get("username" ,'')
    p = request.POST.get("password", '')
    ph=request.POST.get("phone", '')
    use=request.POST.get("ID", '')
    module2.print_use(u)
    uname=module2.b
    if use=='root':
        if u and p:
            if Root.objects.filter(rootname=u,rootpassword=p,):
                context={
                    "username":uname
                }
                return render(request, 'index.html',context=context)
            else:
                context={
                    "hobby":"该用户不存在或密码错误"
                }
            return render(request, 'login.html',context=context)

    if use=='purchaser':
        if u and p :
            if User.objects.filter(username=u,password=p):
                context = {
                    "username": uname
                }
                return redirect("http://127.0.0.1:8000/purchaser")
            else:
                context={
                    "hobby":"该用户不存在或密码错误"
                }
            return render(request, 'login.html',context=context)
    if use == 'agency':
            if u and p:
                if User.objects.filter(username=u, password=p):
                    context = {
                        "username": uname
                    }
                    return render(request, 'AgencyHomepage.html', context=context)
                else:
                    context = {
                        "hobby": "该用户不存在或密码错误"
                    }
                return render(request, 'login.html', context=context)
        # if u and p and use:
        #     if User.objects.filter(username=u,password=p,userid=use):
        #         return render(request, 'index.html')
        #     else:
        #         print("该用户不存在或密码错误")
        # if (ph and p and use):
        #     if User.objects.filter(userphone=ph,password=p,userid=use):
        #         return render(request, 'index.html')
        #     else:
        #         print("该用户不存在或密码错误")
def MedicineSearch1(request):
    p=request.POST.get("wb",'')
    # print(s)
    medicines=Medicine.objects.filter(mno=p)
    uname = module2.b
    if medicines:
        context1 = {
            "hobby": " 查到了",
            "username": uname,
            "medicines": medicines,
        }
    else:
        context1 = {
            "hobby": " 没找到！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'PurchaserHomepage.html',context=context1)
def purchaser(request):

    medicines= Medicine.objects.order_by('mno')
    uname=module2.b


    # for count in counts:
    #     print(count)
    # # for medicine in medicines:
    context={
        "medicines": medicines,
        "username":uname
    }
    return render(request,'PurchaserHomepage.html',context=context)
def Topurchaser(request):
    CountList=request.POST.getlist("med",'[]')
    List=list(CountList)
    print(List)
    medicines = Medicine.objects.order_by('mno')
    print("执行购买操作!")
    context={
        "hobby":"购买完成！"
    }
    temp=0

    i=0
    for medicine in medicines:

        print(type(List[i]))
        print("3")
        print(type(medicine.mcount))
        f=int(List[i])
        print(f)
        medicine.mcount=f+medicine.mcount

        medicine.save()

        i=i+1
        print(i)



    return render(request,'PurchaserHomepage.html',context=context )
def AgencyHomepage(request):
    uname=module2.b
    context={
        "username":uname
    }
    return render(request, 'AgencyHomepage.html', context=context)
def DeleteClient1(request):
    clients = Clinet.objects.order_by('cno')
    uname = module2.b
    # for client in clients:
    #     print(client.cno)
    context = {
        "hobby": "以下是顾客信息",
        "clinets": clients,
        "username": uname

    }
    return render(request, 'ADeleClient.html', context=context)
def Deleteclient1(request):
    clients = Clinet.objects.order_by('cno')
    ags = request.POST.getlist('ag', [])
    uname = module2.b
    for client in clients:
        for ag in ags:
                if( Clinet.objects.filter(cno=ag).delete()):

                    context={
                        "hobby":"删除成功",
                         "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                         "username":uname
                    }
    return render(request, 'ADeleClient.html', context=context)
def get_DeleteClient1(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)

    uname = module2.b
    clients=Clinet.objects.filter(cno=s)



    if clients:
        context = {
            "hobby": " 查到了",
            "clinets": clients,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return render(request, 'ADeleClient.html', context=context)
def PolishClient1(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'PClient.html',context=context)

def get_Client1(request):
    p=request.POST.get("wd",'')
    # print(s)
    clinets=Clinet.objects.filter(cno=p)
    uname = module2.b
    if clinets:
        context1 = {
            "hobby": " 查到了",
            "clinets": clinets,
            "username": uname
        }
    else:
        context1 = {
            "hobby": " 没找到！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'PClient.html',context=context1)


def Polishclient1(request):
    p_cno = request.POST.get("p_cno", '')
    p_cname = request.POST.get("p_cname", '')
    p_csex = request.POST.get("p_csex", '')
    p_cage = request.POST.get("p_cage", '')
    p_caddress = request.POST.get("p_caddress", '')
    p_cphone = request.POST.get("p_phone", '')
    p_csymptom = request.POST.get("p_csymptom", '')
    p_mno = request.POST.get("p_mno", '')
    p_ano = request.POST.get("p_ano", '')
    p_cdate = request.POST.get("p_cdate", '')
    p_cremark = request.POST.get("p_cremark", '')
    p_cmcount=request.POST.get("p_cmcount",'')
    print("执行顾客信息修改")

    p = module2.a
    uname = module2.b
    print("p=", p)
    if p_cno:
        Medicine.objects.filter(cno=p).update(cno=p_mno)
        if p_cname:
            Clinet.objects.filter(cno=p_cno).update(cname=p_cname)
        if p_csex:
            Clinet.objects.filter(cno=p_cno).update(csex=p_csex)
        if p_cage:
            Clinet.objects.filter(cno=p_cno).update(cage=p_cage)
        if p_caddress:
            Clinet.objects.filter(cno=p_cno).update(caddress=p_caddress)
        if p_cphone:
            Clinet.objects.filter(cno=p_cno).update(cphone=p_cphone)
        if p_csymptom:
            Clinet.objects.filter(cno=p_cno).update(csymptom=p_csymptom)
        if p_mno:
            Clinet.objects.filter(cno=p_cno).update(mno=p_mno)
        if p_ano:
            Clinet.objects.filter(cno=p_cno).update(ano=p_ano)
        if p_cdate:
            Clinet.objects.filter(cno=p_cno).update(cdate=p_cdate)
        if p_cremark:
            Clinet.objects.filter(cno=p_cno).update(cremark=p_cremark)
        if p_cremark:
            Clinet.objects.filter(cno=p_cno).update(cmcount=p_cmcount)

    if p_cname:
        Clinet.objects.filter(cno=p).update(cname=p_cname)
    if p_csex:
        Clinet.objects.filter(cno=p).update(csex=p_csex)
    if p_cage:
        Clinet.objects.filter(cno=p).update(cage=p_cage)
    if p_caddress:
        Clinet.objects.filter(cno=p).update(caddress=p_caddress)
    if p_cphone:
        Clinet.objects.filter(cno=p).update(cphone=p_cphone)
    if p_csymptom:
        Clinet.objects.filter(cno=p).update(csymptom=p_csymptom)
    if p_mno:
        Clinet.objects.filter(cno=p).update(mno=p_mno)
    if p_ano:
        Clinet.objects.filter(cno=p).update(ano=p_ano)
    if p_cdate:
        Clinet.objects.filter(cno=p).update(cdate=p_cdate)
    if p_cremark:
        Clinet.objects.filter(cno=p).update(cremark=p_cremark)
    if p_cremark:
        Clinet.objects.filter(cno=p_cno).update(cmcount=p_cmcount)

    context = {
        "hobby": "修改成功",
         "username":uname

    }
    return render(request, 'PClient.html', context=context)
def SetClient1(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'ASetClient.html',context=context)
def Setclient1(request):
    cn = request.POST.get("cno", '')
    csx = request.POST.get("csex", '')
    cnme = request.POST.get("cname", '')
    cpone = request.POST.get("cphone", '')
    cge = request.POST.get("cage", '')
    cdess = request.POST.get("caddress", '')
    csy = request.POST.get("csymptom", '')
    mn = request.POST.get("mno", '')
    an = request.POST.get("ano", '')
    cd = request.POST.get("cdate", '')
    cmark = request.POST.get("cremark", '')
    ccount=request.POST.get("cmcount", '')
    uname = module2.b
    clients=Clinet.objects.order_by('cno')
    medicines=Medicine.objects.filter(mno=mn)
    if an and csx and cnme and cpone and cmark and cn and cge and csy and cdess and mn and cd and ccount:
            for client in clients :
                print(client.cno)
                if client.cno==cn:
                    context={
                        "hobby":"顾客编号重复！",
                        "username": uname
                    }
                    return render(request,'ASetClient.html',context=context)
            if medicines.mcount<ccount:
                context = {
                    "hobby": "药品库存不足！",
                    "username": uname
                }
                return render(request, 'ASetClient.html', context=context)
            atu = Clinet(cno=cn,cname=cnme,csex=csx,cphone=cpone,cage=cge,caddress=cdess,csymptom=csy,mno=mn,ano=an,cdate=cd,cremark=cmark,cmcount=ccount)
            atu.save()
            medicines.mcount=medicines.mcount-ccount
            medicines.save()
            context = {
                 "hobby": "添加成功！",
                "username": uname
             }
            return render(request, 'ASetClient.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'ASetClient.html', context=context)
def DeleteMedicine1(request):
    medicines= Medicine.objects.order_by('mno')
    uname = module2.b
    # for agency in agencys:
    #     print(agency.ano)
    context = {
        "hobby": "以下是药品信息",
        "medicines": medicines,
        "username": uname
    }
    return render(request, 'ADeleMedicine.html', context=context)
def Deletemedicine1(request):
    medicines = Medicine.objects.order_by('mno')
    mes = request.POST.getlist('me', [])
    clients=Clinet.objects.all()
    uname = module2.b
    for medicine in medicines:
        for me in mes:
            for client in clients:
                if Clinet.objects.filter(mno=me):
                    context={
                        "hobby":"非法删除！该药品已经被顾客购买"
                    }
                    return render(request,  'ADeleMedicine.html',context=context)
                if( Medicine.objects.filter(mno=me).delete()):

                    context={
                        "hobby":"删除成功",
                        "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                        "username":uname
                    }
    return render(request, 'ADeleMedicine.html',context=context)
def get_DeleteMedicine1(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)
    uname = module2.b

    medicines=Medicine.objects.filter(mno=s)



    if medicines:
        context = {
            "hobby": " 查到了",
            "medicines": medicines,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此药！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'ADeleMedicine.html',context=context)
def PolishMedicine1(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'APolishMedicine.html',context=context)


def get_Medicine1(request):
    s = request.POST.get("wd", '')
    print("执行查询")
    module2.print_a(s)
    print("s=", s)
    uname = module2.b
    medicines = Medicine.objects.filter(mno=s)

    if medicines:
        context = {
            "hobby": " 查到了",
            "medicines": medicines,
            "username": uname
        }
    else:
        context = {
            "hobby": " 无药品信息！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return render(request, 'APolishMedicine.html', context=context)


def Polishmedicine1(request):
    p_mno = request.POST.get("p_mno", '')
    p_mname = request.POST.get("p_mname", '')
    p_mmode = request.POST.get("p_amode", '')
    p_mefficacy = request.POST.get("p_mefficacy", '')
    p_mcount=request.POST.get("p_mcount", '')

    uname = module2.b
    print("执行修改")

    p = module2.a

    print("p=", p)
    if p_mno:
        Medicine.objects.filter(mno=p).update(mno=p_mno)
        if p_mname:
            Medicine.objects.filter(mno=p_mno).update(mname=p_mname)
        if p_mmode:
            Medicine.objects.filter(mno=p_mno).update(mmode=p_mmode)
        if p_mefficacy:
            Medicine.objects.filter(mno=p_mno).update(mefficacy=p_mefficacy)
        if p_mcount:
            Medicine.objects.filter(mno=p_mno).update(mcount=p_mcount)

    if p_mname:
        Medicine.objects.filter(mno=p).update(mname=p_mname)
    if p_mmode:
        Medicine.objects.filter(mno=p).update(mmode=p_mmode)
    if p_mefficacy:
        Medicine.objects.filter(mno=p).update(mefficacy=p_mefficacy)
    if p_mcount:
        Medicine.objects.filter(mno=p).update(mcount=p_mcount)
    context = {
        "hobby": "修改成功",
        "username": uname
    }
    return render(request, 'APolishMedicine.html', context=context)
def SetMedicine1(request):
    uname = module2.b
    context = {
        "username": uname
    }

    return render(request, 'ASetMedicine.html',context=context)
def Setmedicine1(request):
    mn = request.POST.get("mno", '')
    uname = module2.b
    mnme = request.POST.get("mname", '')
    mmod = request.POST.get("mmode", '')
    mef= request.POST.get("mefficacy", '')
    mc=request.POST.get("mcount", '')
    medicines=Medicine.objects.order_by()
    if mn and mnme and mmod and mef and mc  :
            for medicine in medicines :
                print(medicine.mno)
                if medicine.mno==mn:
                    context={
                        "hobby":"药品编号重复！",
                        "username": uname
                    }
                    return render(request,'ASetMedicine.html',context=context)

            atu = Medicine(mno=mn,mname=mnme,mmode=mmod,mefficacy=mef,mcount=mc)
            atu.save()
            context = {
                 "hobby": "添加成功！",
                 "username": uname

             }
            return render(request, 'ASetMedicine.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'ASetMedicine.html', context=context)


def PolishUser(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'PolishUser.html', context=context)


def get_User(request):
    s = request.POST.get("wd", '')
    print("执行查询")
    module2.print_a(s)
    print("s=", s)
    uname = module2.b
    users=User.objects.filter(username=s)

    if users:
        context = {
            "hobby": " 查到了",
            "users": users,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return render(request, 'PolishUser.html', context=context)


def Polishuser(request):

    p_name = request.POST.get("p_username", '')

    p_phone = request.POST.get("p_phone", '')
    p_password = request.POST.get("p_password", '')
    p_id = request.POST.get("p_id", '')

    print("执行修改")

    p = module2.a
    uname = module2.b
    print("p=", p)
    if p_name:
        User.objects.filter(username=p_name).update(username=p_name)
        if p_password:
            User.objects.filter(username=p_name).update(userpassword=p_password)
        if p_phone:
            User.objects.filter(username=p_name).update(userphone=p_phone)
        if p_id:
            User.objects.filter(username=p_name).update(userid=p_id)
    if p_password:
        User.objects.filter(username=p).update(userpassword=p_password)
    if p_phone:
        User.objects.filter(username=p).update(userphone=p_phone)
    if p_id:
        User.objects.filter(username=p).update(userid=p_id)
    context = {
        "hobby": "修改成功",
        "username": uname
    }
    return render(request, 'Polishser.html', context=context)
def DeleteUser(request):
    users=User.objects.all()
    uname = module2.b

    context = {
        "hobby": "以下是用户信息",
        "users": users,
        "username": uname
    }
    return render(request, 'DeleteUser.html', context=context)
def Deleteuser(request):
    users=User.objects.all()
    ags = request.POST.getlist('us', [])

    uname = module2.b
    for user in users:
        for ag in ags:

                if(User.objects.filter(username=ag).delete()):

                    context={
                        "hobby":"删除成功",
                        "username":uname
                    }
                else:
                    context={
                        "hobby":"删除失败",
                        "username": uname

                    }
    return render(request, 'DeleteUser.html',context=context)
def get_DeleteUser(request):

    s=request.POST.get("wd",'')

    module2.print_a(s)
    uname = module2.b

    users=User.objects.filter(username=s)



    if users:
        context = {
            "hobby": " 查到了",
            "users": users,
            "username": uname
        }
    else:
        context = {
            "hobby": " 查无此人！",
            "username": uname
        }

    # return HttpResponse("信息表")
    return  render(request,'DeleteUser.html',context=context)
def SetUser(request):
    uname = module2.b
    context = {
        "username": uname
    }
    return render(request, 'SetUser.html',context=context)
def Setuser(request):
    name = request.POST.get("username", '')

    phone = request.POST.get("phone", '')
    pas= request.POST.get("password", '')
    ID = request.POST.get("id", '')
    users=User.objects.all()
    uname = module2.b
    if name and phone and pas and ID  :
            for user in users :

                if user.username==name:
                    context={
                        "hobby":"用户名重复！",
                        "username":uname
                    }
                    return render(request,'SetUser.html',context=context)

            atu = User(username=name,userphone=phone,password=pas,userid=ID)
            atu.save()
            context = {
                 "hobby": "添加成功！",
                 "username": uname
             }
            return render(request, 'SetUser.html', context=context)
    else:
        context = {
            "hobby": "请输入完整信息！",
            "username": uname
        }
        return render(request, 'SetUser.html', context=context)