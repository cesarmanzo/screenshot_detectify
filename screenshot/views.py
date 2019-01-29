from django.shortcuts import render
from django.contrib.auth.models import User, Group
from screenshot.models import *
from rest_framework import viewsets
from selenium import webdriver
import os
import time


def welcome(request):
    return render(request, 'main.html')


def read_source(request):
    count = 0
    r_type = request.POST.get('r_type')
    source = request.POST.get('source')

    if source == '1':
        multiple = request.POST.get('list')
        multiple = multiple.split(';')
        print(multiple)
    elif source == '2':
        with open('text.txt', 'r') as f:
            multiple = f.read().split(';')
            print(multiple)
    if r_type:
        r_type = 1
    else:
        r_type = 2
    saving = Requesting(source=int(source), r_type=r_type)
    saving.save()

    for url in multiple:
        count += 1
        print('THIS IS ', url)
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
        else:
            height = 768
        print(height)
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
    print('END')

    return True


def show_results(saving):
    results = Screenshots.objects.filter(requesting = saving)
    return results
