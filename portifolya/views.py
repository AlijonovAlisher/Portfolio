from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import *
from .form import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def about(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Replace 'success' with the URL or name of the success page
    else:
        form = SendMessageForm()
    about_info = About.objects.filter().last()
    skill_info = skill.objects.all()
    foll = follower.objects.filter().last()
    con = contact.objects.filter().last()
    ser = service.objects.filter().last()
    me = About_Me.objects.filter().last()
    res = Resume.objects.all()

    context = {
                'form': form,
                'about_info': about_info,
                'skill_info': skill_info,
                'follow_list': foll,
                'contact_list': con,
                'service_list': ser,
                'about_list': me,
                'resume_list': res,


    }
    return render(request, 'index.html', context)



def single (request):
    return render(request, 'single.html')



def works(request):
    return render(request, 'works.html')





