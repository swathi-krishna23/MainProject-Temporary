from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Camera_info, Crashed_frames
from django.http import HttpResponse
from .functions.functions import handle_uploaded_file  
from .forms import InputForm
from django.contrib.auth.decorators import login_required

def input(request):  
    if request.method == 'POST':  
        input = InputForm(request.POST, request.FILES)  
        if input.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            # return HttpResponse("File uploaded successfuly")  
            # form.save()
            return redirect("/client/") 

    else:  
        form = InputForm()  
        return render(request,"client/upload.html",{'form':form})  



def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        print(type(form))
        if form.is_valid():
        # result=form.is_valid()
            form.save()
        else:
            form = UserCreationForm()
            return redirect("/client/register/")
        
        return redirect("/client/")
    else:
        form = UserCreationForm()

    return render(request, 'client/register.html', {'form': form})



def index(request):
    return render(request, 'client/notification.html')



def view(request):
    # try:
        # if request.method == 'GET':
            camera_info_results = Camera_info.objects.all()
            print(camera_info_results)
            
            crashed_frames_results = Crashed_frames.objects.all()
            print(crashed_frames_results)
            camera_info_fields = Camera_info._meta.get_fields()
            crashed_frames_fields = Crashed_frames._meta.get_fields()
            return render(request, 'client/view_db.html', {'camera_info': camera_info_results, 'camera_info_fields':camera_info_fields,
                                    'crashed_frames':crashed_frames_results, 'crashed_frames_fields':crashed_frames_fields})

    # except:
        # pass


@login_required(login_url='/login/')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        print(query)
        if query:
            result_city = Camera_info.objects.filter(city__icontains=query) 
            print(result_city, 'result_City')
            # result_city = result_city[0]
            # print(result_city)
            result_location = Camera_info.objects.filter(location__icontains=query)
            print(result_location, 'location')
            result = []
            city = [[]]
            if(result_city):
                for i in range(len(result_city)):
                    camera_id_curr = result_city[i].camera_id
                    # result.append(Camera_info.objects.filter(camera_id=camera_id_curr)) 
                    city[0].append(Crashed_frames.objects.filter(camera_id=camera_id_curr)) 
                    # print(camera_id_curr,'cam_id')
                    # print(city, 'city')
            # print(result_location)
            if result_city:
                for i in range(len(city)):
                    # print(len(city[0]))
                    curr_city = len(city[i])
                    print(curr_city)
                    for j in range(curr_city):
                        print(city[i][j])
                        print(type(city[i][j]))
                        result[0].append(city[i][j])
            if(result_location):
                for i in range(len(result_location)):
                    camera_id_curr = result_location[i].camera_id
                    result.append(Crashed_frames.objects.filter(camera_id=camera_id_curr)) 
                    # print(camera_id_curr)
                    # print(result,'city')
                    
            # for item in result:
            #     print(item)
            #     break
            
            # for item in result:
            #     print(item[0].camera_id)
            #     break
            # print(result[1])
            # print(result)
            
            # print(len(result[0][0]))
            return render(request, 'client/searchBar.html', {'result':result[0]})
        else:
            print("No information to show")
            return render(request, 'client/searchBar.html', {})
        
# def searchBar(request):
#     return render(request, 'client/searchBar.html')