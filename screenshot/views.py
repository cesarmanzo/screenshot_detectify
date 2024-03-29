from django.shortcuts import render
from screenshot.models import *
from rest_framework import viewsets
from selenium import webdriver
import os
import time
import requests


def welcome(request):
    return render(request, 'main.html')


def read_source(request):
    count = 0
    r_type = request.POST.get('r_type')
    source = request.POST.get('source')
    

    # file = request.POST.get('file')
    
    # file = request.POST.get(('_files')[0]'file'))

    #re = requests.get(request)
    # print(file)

    if source == '1':
        multiple = request.POST.get('list')
        multiple = multiple.split(';')
    elif source == '2':
        multiple = request.FILES['file'].read().decode('utf-8')
        print(multiple)
        multiple = multiple.split(';')
    if r_type:
        r_type = 1
    else:
        r_type = 2
    saving = Requesting(source=int(source), r_type=r_type)
    saving.save()

    for url in multiple:
        count += 1
        print(url)
        take_screenshot(url, r_type, saving, count)

    res = show_results(saving)

    return render(request, 'results.html', {'res': res})

def take_screenshot(url, r_type, saving, count):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('hide-scrollbars')
    op.add_argument('kiosk')
    driver = webdriver.Chrome(chrome_options=op)
    try:
        driver.get(url)
        if r_type == 1:
            height = driver.execute_script(
                """return Math.max(document.body.scrollHeight,
                    document.body.offsetHeight,
                    document.documentElement.clientHeight,
                    document.documentElement.scrollHeight,
                    document.documentElement.offsetHeight)""")
            if height < 768:
                height = 768
        else:
            height = 768
        driver.set_window_size(1366, height)
        title = driver.title
        time.sleep(1)
        name = 'media/'+ str(saving.id) + '-' + str(count) + '.png'
        driver.get_screenshot_as_file(name)
        tosave = Screenshots(image=name, title=title, url=url, requesting=saving)
        tosave.save()
    except Exception as e:
        print('error: ', e)
    driver.quit()

    return True


def show_results(saving):
    results = Screenshots.objects.filter(requesting = saving)
    return results

def past_requesting(request):
    past = Requesting.objects.all()
    return render(request, 'past.html', {'past': past})

def showing_results(request):
    res = Screenshots.objects.filter(requesting = request.GET.get('saving'))
    print(res)
    return render(request, 'results.html', {'res': res})
