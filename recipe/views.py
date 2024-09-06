from django.shortcuts import render, redirect,get_object_or_404
from .models import recipe_module  
from django.core.exceptions import ValidationError


def recipe(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipeName')
        recipe_description = request.POST.get('recipeDescription')
        recipe_image = request.FILES.get('recipeImage')
        recipe_imageUrl=request.POST.get('recipeImageUrl')
        try:
            recipe = recipe_module(
                
                recipeName=recipe_name,
                recipeDescription=recipe_description,
                recipeImage=recipe_image,
                recipeImageUrl=recipe_imageUrl
            )
            if recipe_image or recipe_imageUrl:
                 recipe.save()

                
            return redirect('disply_recipe')
        except ValidationError as e:
            print(f"Validation error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'index.html')


def disply_recipe(request):
    recipe = recipe_module.objects.all()
    search=request.GET.get("search_recipe")
    if search:
        recipe = recipe_module.objects.filter(recipeName__icontains=search)
    # filter=recipe_module.objects.filter(disply_recipe)
    
    return render(request,"recipe_display.html",{'recipe':recipe})

def recipe_delete(request,id):
    query = get_object_or_404(recipe_module, id=id)
    query.delete()
    
    return redirect('disply_recipe')

def update_recipe(request, id):
    recipe = get_object_or_404(recipe_module, id=id)
    
    if request.method == "POST":
        recipe_name = request.POST.get('recipeName')
        recipe_description = request.POST.get('recipeDescription')
        recipe_image = request.FILES.get('recipeImage')
        recipe_image_url = request.POST.get('recipeImageUrl')

        recipe.recipeName = recipe_name
        recipe.recipeDescription = recipe_description
        
       
        if recipe_image:
            recipe.recipeImage = recipe_image
      
        if recipe_image_url:
            recipe.recipeImageUrl = recipe_image_url
        
        try:
            recipe.save()
            return redirect('disply_recipe')
        except ValidationError as e:
            print(f"Validation error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}") 
   
    return render(request, 'update_rechipe.html', {'recipe': recipe})
# def update_recipe(request,id):
#     # query = get_object_or_404(recipe_module, id=id)
#     # query.delete()
    
#     return redirect('update_recipe_html')


from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
         
        if user is not None:
            # Log the user in and redirect to a success page
            login(request, user)
            return redirect('recipes')  # Redirect to the home page or another page
        else:
            # Display an error message if authentication fails
            messages.error(request, "Invalid username or password")
            return redirect('/',user)
        
    context = {'is_signup': False}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_view')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        print(username)
        # confermpassword = request.POST['password2']
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already exists")
            return redirect('signup_view')
        user = User.objects.create_user(username=username, password=password)
       
        user.save()
    
        return redirect('login_view')
        
           
    context = {'is_signup': True}
    return render(request, 'login.html', context)
