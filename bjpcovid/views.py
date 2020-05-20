from django.shortcuts import render
import requests
import json


def hello(request):
    data = requests.get('https://api.covid19india.org/dis tricts_daily.json')
    jsondata = json.loads(data.text)

    length = len(jsondata['districtsDaily']['Karnataka']['Vijayapura'])
    last_confirm = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length-2]['confirmed']
    confirm = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length - 1]['confirmed']
    active = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length - 1]['active']
    dead = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length - 1]['deceased']
    recovered = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length - 1]['recovered']
    date = jsondata['districtsDaily']['Karnataka']['Vijayapura'][length - 1]['date']

    return render(request, 'index.html', context={'date': date, 'confirm': confirm, 'active': active,
                                                  'recovered': recovered, 'dead': dead, 'today': confirm-last_confirm})
