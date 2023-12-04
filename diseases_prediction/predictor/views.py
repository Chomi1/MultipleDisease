from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import HeartDiseasePredictionData, DiabetesPredictionData
from django.utils import timezone
import pickle
# Create your views here.

def render_with_base(request, template_name, context=None):
    return render(request, template_name, context)

def render_with_result(request, template_name, context=None):
    return render(request, template_name, context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render_with_base (request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index_page')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render_with_base(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your home page


def admin_page(request):
    return render_with_base(request, 'admin.html')

def profile_page(request):
    return render_with_base(request, 'profile.html')

def index_page(request):
    return render_with_base(request, 'index.html')

def heart_disease_prediction(request):
    if request.method == 'POST':
        age = float(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = float(request.POST.get('trestbps'))
        chol = float(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = float(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

        with open('predictor/heart_disease_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

       
        prediction = model.predict(features)

        timestamp = timezone.now()

        prediction_instance = HeartDiseasePredictionData.objects.create(
            user=request.user,
            age=age,
            sex=sex,
            cp=cp,
            trestbps=trestbps,
            chol=chol,
            fbs=fbs,
            restecg=restecg,
            thalach=thalach,
            exang=exang,
            oldpeak=oldpeak,
            slope=slope,
            ca=ca,
            thal=thal,
            prediction=prediction
        
        )
        prediction_instance.save()

        return render_with_base(request, 'heart_disease_result.html', {'prediction': prediction[0]})

    return render_with_base(request, 'heart_disease_prediction.html')

@login_required

def heart_disease_profile(request):
    # Assuming you are trying to retrieve data for the currently logged-in user
    user = request.user

    # Use filter instead of get to handle the case where multiple objects are returned
    prediction_data = HeartDiseasePredictionData.objects.filter(user=user)

    return render(request, 'heart_disease_profile.html', {'prediction_data': prediction_data})

@login_required
def diabetes_prediction(request):
    if request.method == 'POST':
        pregnancies = float(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        diabetes_pedigree_function = float(request.POST.get('diabetes_pedigree_function'))
        age = float(request.POST.get('age'))

        # Create a feature list
        features2 = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]

        with open('predictor/diabetes_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        
        prediction = model.predict(features2)

        timestamp = timezone.now()

        prediction_instance = DiabetesPredictionData.objects.create(
            user=request.user,
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            diabetes_pedigree_function=diabetes_pedigree_function,
            age=age,
            prediction=prediction
        )

        prediction_instance.save()

        return render(request, 'diabetes_result.html', {'prediction': prediction[0]})

    return render(request, 'diabetes_prediction.html')


@login_required
def diabetes_profile(request):
    # Assuming you are trying to retrieve data for the currently logged-in user
    user = request.user

    # Use filter instead of get to handle the case where multiple objects are returned
    prediction_data = DiabetesPredictionData.objects.filter(user=user)

    return render(request, 'diabetes_profile.html', {'prediction_data': prediction_data})

