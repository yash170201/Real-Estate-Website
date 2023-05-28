from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Buysell, LegalAdvisor,Addproperty
from .serializers import *
from django.core.files.storage import FileSystemStorage
import base64
from django.core.files.base import ContentFile
from django.conf.urls.static import static
import json

@api_view(['GET', 'POST'])    
def buysell_list(request):
    if request.method == 'GET':
        data = Buysell.objects.all()
        
        serializer = BuysellSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BuysellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST']) 
def legal_check(request):
    parser_classes=(MultiPartParser,FormParser)
    if request.method == 'GET':
        data = LegalAdvisor.objects.all()

        serializer = LegalAdvisorSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        l_user=request.data['Username']
        l_name=request.data['name']
        l_email=request.data['email']
        l_pass=request.data['Password']
        l_city=request.data['City']
        l_phone=request.data['Phone']
        l_licence=request.data['Licence']       
        l_file=request.data['File']
        l_profile=request.data['Profile']
        # print(l_file)

        # decoded_file = base64.b64decode(l_file)
        # print(decoded_file)
        format, imgstr = l_file.split(';base64,') 
        # print(imgstr)
        ext = format.split('/')[-1] 
        # print(ext)
        data1 = ContentFile(base64.b64decode(imgstr), name=l_licence+'.' + ext)
        # print(data)
        name = format.split(":")[-1]
        # print(name)

        # decoded_file = base64.b64decode(l_profile)
        # print(decoded_file)
        format, imgstr = l_profile.split(';base64,') 
        # print(imgstr)
        ext = format.split('/')[-1] 
        # print(ext)
        data2 = ContentFile(base64.b64decode(imgstr), name=l_name+'.' + ext)
        # print(data)
        name = format.split(":")[-1]
        # print(name)

        object=LegalAdvisor.objects.create(Username=l_user,name=l_name,email=l_email,Password=l_pass,City=l_city,Phone=l_phone,License=l_licence,File=data1,file_url=l_file,Profile=data2,profile_url=l_profile)
        object.save()  
        return Response(status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'POST':
        
        u_user = request.data['Username']
        p_user= request.data['Password']
        
        mydata = Buysell.objects.filter(Username=u_user,Password=p_user)
        data=mydata.values()
        print(data)
        if mydata.count()>0:
            return Response( data[0],status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST']) 
def login_legal(request):
    if request.method == 'POST':
        u_legal = request.data['Username']
        p_legal= request.data['Password']
        l_legal=request.data['Licence']
        mydata = LegalAdvisor.objects.filter(Username=u_legal,License=l_legal,Password=p_legal)
        print(mydata)
        if mydata.count()>0:
            data=mydata.values()
            print(data)
            return Response(data[0],status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST']) 

def forget_user(request):
    if request.method == 'POST':
        f_user = request.data['Username']
        f_pass= request.data['Password']
        f_email=request.data['Email']
        mydata = Buysell.objects.filter(Username=f_user,email=f_email).update(Password=f_pass)
        print(mydata)
        # data=mydata.values()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST']) 
def forget_legal(request):
    if request.method == 'POST':
        f_user = request.data['Username']
        f_pass= request.data['Password']
        f_email=request.data['Email']
        f_licence=request.data['Licence']
        print(f_email,f_user,f_licence,f_pass)
        mydata = LegalAdvisor.objects.filter(Username=f_user,License=f_licence,email=f_email).update(Password=f_pass)
        print(mydata)
        return Response(status=status.HTTP_201_CREATED)
        # return HttpR
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])    
def addProperty(request):
    if request.method == 'GET':
        data = Addproperty.objects.all()
        serializer = AddPropertySerializer(data, context={'request': request}, many=True)        
        
        return Response(serializer.data)
        

    elif request.method == 'POST':
        
        a_name=request.data['name']
        a_email=request.data['email']
        a_postal=request.data['postal']
        a_address=request.data['address']
        a_phone=request.data['phone']
        a_price=request.data['price'] 
        a_size=request.data['size']
        a_des=request.data['des']      
        a_file=request.data['File']
        a_city=request.data['city']
        print(a_city)

        # decoded_file = base64.b64decode(a_file)
        # print(decoded_file)
        format, imgstr = a_file.split(';base64,') 
        # print(imgstr)
        ext = format.split('/')[-1] 
        # print(ext)
        data = ContentFile(base64.b64decode(imgstr), name=a_name+'.' + ext)
        # print(data)
        name = format.split(":")[-1]

        a=Addproperty.objects.all()
        
        serializer = AddPropertySerializer(a, context={'request': request}, many=True)
        data=serializer.data
        if(Addproperty.objects.count()==0):
            object=Addproperty.objects.create(Property={'city':a_city,'P':[{'email':a_email,'postal':a_postal,'address':a_address,'phone':a_phone,'price':a_price,'size':a_size,'des':a_des,'city':a_city,'image':a_file}]}) 
            object.save()
            
        try: 
            for i in data:
                od2 = json.loads(json.dumps(i))
                if((od2['Property']['city']))==a_city:
                    n=od2['id']
                    od2['Property']['P']
                    od2['Property']['P'].append({'email':a_email,'postal':a_postal,'address':a_address,'phone':a_phone,'price':a_price,'size':a_size,'des':a_des,'city':a_city,'image':a_file})
                    m=od2['Property']
                # print(m)
                    Addproperty.objects.filter(pk=n).update(Property=m)
                   
            return Response(status=status.HTTP_201_CREATED)


        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            y=Addproperty.objects.count()
            count=0
            for j in data:
                
                od1 = json.loads(json.dumps(j))
                if((od1['Property']['city']))!=a_city:
                    count+=1

            if y==count:
                object=Addproperty.objects.create(Property={'city':a_city,'P':[{'email':a_email,'postal':a_postal,'address':a_address,'phone':a_phone,'price':a_price,'size':a_size,'des':a_des,'city':a_city,'image':a_file}]}) 
                object.save()


            return Response(status=status.HTTP_201_CREATED)
                
            
       