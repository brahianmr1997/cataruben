from django.shortcuts import render, redirect

def prueba(request):
    context = {'ciudad' : 'Santiago de cali',
                'intro': 'Capital del valle',
                'img': 'http://www.institutocanzion.com.co/wp-content/uploads/2019/02/CALI.jpg',
            }
    return render(request, 'mapjs\\home.html', context)

# Create your views here.
