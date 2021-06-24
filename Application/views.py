from django.shortcuts import render
from .models import *
from .form import *
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt

#		Our Homepage
def index(request):
	intro = Intro.objects.all()
	return render(request, 'Application/index.html', {'form': IntroForm(), 'intro': intro})
	
	
#		Save Page Using Ajax
#@csrf_exempt	
def saveData(request):
	if request.method == "POST":	
		form = IntroForm(request.POST)
		if form.is_valid():
			InfoId = request.POST.get('InfoId')
			name = request.POST['name']
			mobile = request.POST['mobile']
			email = request.POST['email']
			about = request.POST['about']
			if (InfoId == ''):
				usr = Intro(name = name, mobile = mobile, email = email, about = about)
				usr.save()
			else:
				usr = Intro(id = InfoId, name = name, mobile = mobile, email = email, about = about)
				usr.save()
			infoData = Intro.objects.values()
			listInfoData = list(infoData)
			return JsonResponse({'status': 'Save', 'listInfoData': listInfoData})
		else:
			return JsonResponse({'status': 'NotSave'})

#			Delete Data Functionality
def delete(request):
	if request.method == "POST":
		id = request.POST.get('sid')
		dele = Intro.objects.get(pk = id)
		dele.delete()
		return JsonResponse({'status': 'Deleted...'})
	else:
		return JsonResponse({'status': 'Somemthing Went Wrong...'})

#			 Edit Data Functionality

def edit(request):
	if request.method == "POST":
		id = request.POST.get('sid')
		editData = Intro.objects.get(pk = id)
		editIntroData = {'id': editData.id, 'name': editData.name, 'mobile': editData.mobile, 'email': editData.email, 'about': editData.about}
		return JsonResponse(editIntroData)
		

#Demo is used for testing purpose... 
def demo(request):
	if request.method == 'GET':
		return render(request, 'Application/demo.html', {'form': IntroForm
        ()})
	else:
		try:
			form =  IntroForm(request.POST)
			newIntroForm = form.save(commit = True)
			newIntroForm.save()
			return redirect('/')
		except ValueError:
			return render(request, 'Application/demo.html', {'error': 'Save Function kaam nhi kr raha h.', 'form': form})
