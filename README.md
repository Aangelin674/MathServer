# Ex.04 Design a Website for Server Side Processing
## Date:10.12.2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
``` 
math.html

<html>
  <head>
    <title>Calculator</title>
    <style>
      .box
      {
        width: 500px;
        height: 300px;
        border: dashed 3px black;
        padding:10 px;
        position:fixed;
        top:150px;
        left:500px;
        text-align:center;
        background-color:skyblue;


      }
    </style>
  </head>
  <body bgcolor="darkblue">
    <div class="box">
      <h1>Calculator</h1>
      <h3>ANGELIN GRACY.R (25007261</h3>
    <form method="POST">
    {% csrf_token %}
      <div class="formelt">
        <label>Distance(km)</label>
        <input type="text" name="Distance" required></input>
      </div>
      <br>
      <div class="formelt">
      <label>Fuel_used(l)</label>
        <input type="text" name="Fuel_used" required></input>  
      </div>
      <br>
      <div class="formelt">
         <input type="submit" value="Calculate"> 
      </div>
      <br>
      <div class="formelt">
        <label>Mileage:(km/l)</label>
        <input type="text" name="Mileage" value="{{Mileage}}"></input>
      </div>
      <br>
    </form>
    </div>
  </body>
</html>
      
views.py
from django.shortcuts import render
def mileage (request):
  D= float(request.POST.get('Distance',0))
  F= float(request.POST.get('Fuel_used',0))
  mileage = D/F if request.method == 'POST' else 0
  print("Distance = ",D)
  print("Fuel_used = ",F)
  print("Mileage = ",mileage)
  return render(request,'mathapp/math.html',{'Distance':D,'Fuel_used':F,'Mileage':mileage})

urls.py
from django.urls import path
from mathapp import views
urlpatterns = [
    path('',views.mileage,name='mileage'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (43).png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot (42).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
