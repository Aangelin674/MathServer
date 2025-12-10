from django.shortcuts import render
def mileage (request):
  D= float(request.POST.get('Distance',0))
  F= float(request.POST.get('Fuel_used',0))
  mileage = D/F if request.method == 'POST' else 0
  print("Distance = ",D)
  print("Fuel_used = ",F)
  print("Mileage = ",mileage)
  return render(request,'mathapp/math.html',{'Distance':D,'Fuel_used':F,'Mileage':mileage})

