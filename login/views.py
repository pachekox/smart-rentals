from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import  Tuser

# Create your views here.
def index(request):
	context={
	'stm':'Hello There'
	}
	return render(request,'login/index.html',context)

def log(request):
	if request.method == 'POST':
		name = request.POST['username']
		username = request.POST['password']
		query = Tuser.objects.filter(username = name,password = username).exists()
		# password = Tuser.Objects.get(password = password)

		if query:
			# return HttpResponse("Details in Database")
			context={
			'stm':'Details exists in the Database'
			}
			return render(request,'login/login.html',context)

		else:
			return HttpResponse("Details Mismatch")
	else:
		return render(request,'login/login.html')

def register(request):
	if request.method == "POST":
		email = request.POST['mail']
		username = request.POST['username']
		password = request.POST['password']

		if password == request.POST['cpassword']:
			user1 = Tuser(username = username , password= password , mail = email)
			user1.save()
			return redirect("log")
		else:
			return HttpResponse("password does not match")
	else:
		return render(request,'login/register.html')
	