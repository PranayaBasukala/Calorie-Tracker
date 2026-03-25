from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def main(request):
    import json
    import requests

    if request.method == 'POST':
        query=request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_key = os.getenv('NUTRITION_API_KEY', '')
        if not api_key:
            api = "Error: API key not configured"
            return render(request, 'main.html', {'api': api, 'error': True})
        
        api_request=requests.get(api_url + query, headers={'X-Api-Key': api_key})
        
        try:
            if api_request.status_code == 200:
                api = json.loads(api_request.content)
            else:
                api = f"Error: {api_request.status_code} - {api_request.text}"
        except Exception as e:
            api = f"Error: {str(e)}"
            print(e)

        return render(request, 'main.html',{'api':api})
    else:
        return render(request, 'main.html',{'query':"Enter a valid query"})    




def SignUpPage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'signup.html')
        
        try:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'signup.html')
        
    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('main')
        else:
            messages.error(request, "Username or password is incorrect")
            return render(request, 'login.html')
  
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')



# 
# def handleSignUp(request):
#     if request.method == 'POST':
#         # Get the post parameters
#         username = request.POST ['user']
#         fname = request.POST ['fname']
#         lname = request.POST ['lname']
#         email = request.POST ['email']
#         pass1 = request.POST ['pass1']
#         pass2 = request.POST ['pass2']
        

#         # validation of the inputs
        
#         # Create the user
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()
#         messages.sucess(request, "Your foodie account has been sucessfully created")
#         return redirect('home')
#     else:
#         return HttpResponse('404 - Not Found')
    
# def handleLogin(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password = request.POST['pass']
#         return redirect('main.html')
    
#     else:
#         return HttpResponse('404-not Found')



# '''
# from django.http import JsonResponse
# def get_food_item(request, name):
#     try:
#         food_item = FoodItem.objects.get(name=name)
#         data = {
#             'name': food_item.name,
#             'calories': food_item.calories,
#             'serving_size_g': food_item.serving_size_g,
#             'fat_total_g': food_item.fat_total_g,
#             'fat_saturated_g': food_item.fat_saturated_g,
#             'protein_g': food_item.protein_g,
#             'sodium_mg': food_item.sodium_mg,
#             'potassium_mg': food_item.potassium_mg,
#             'cholesterol_mg': food_item.cholesterol_mg,
#             'carbohydrates_total_g': food_item.carbohydrates_total_g,
#             'fiber_g': food_item.fiber_g,
#             'sugar_g': food_item.sugar_g,
#         }
#         return JsonResponse(data)
#     except FoodItem.DoesNotExist:
#         return JsonResponse({'error': 'Food item not found'}, status=404)
# '''

# # from django.shortcuts import render
# # from django.http import HttpResponse

# # def get_food_item(request, name):
# #     # Your view logic here
# #     print('try')
# #     return HttpResponse(f"You requested information for food item: {name}")