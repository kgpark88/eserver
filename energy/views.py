import os
import sys
from datetime import datetime, timedelta
import numpy as np
from shutil import move
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import tensorflow as tf
from tensorflow.keras import layers

from energy.models import EnergyUsage

# model_path = "saved_models"
# model = tf.keras.models.load_model(model_path)

wdays =['월','화','수','목','금','토','일']

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'b_name': openapi.Schema(type=openapi.TYPE_STRING, description='빌딩 이름'),
        'from_dt': openapi.Schema(type=openapi.TYPE_STRING, description='조회 시작일'),
        'to_dt': openapi.Schema(type=openapi.TYPE_STRING, description='조회 종료일'),
    }
))
@api_view(['POST'])
def energy_usage(request):
    '''
    에너지 사용량 조회 REST API
    ---
    에너지 사용량 조회 REST API
    '''

    b_name = request.data.get('b_name', '')
    from_dt = request.data.get('from_dt', '')
    to_dt = request.data.get('to_dt', '')

    from_dt = datetime.strptime(from_dt, '%Y-%m-%d')    
    to_dt = datetime.strptime(to_dt, '%Y-%m-%d')   

    qs = EnergyUsage.objects.filter(
        b_name=b_name, daq_time__date__gte=from_dt, 
        daq_time__date__lte=to_dt).order_by('daq_time')

    res = {}
    x_axis = []
    p_usage = []
    prediction = []
    temp = []
    rh = []
    for q in qs:
        dt_str = q.daq_time.strftime("%m-%d %H:%M")
        x_axis.append(dt_str)
        p_usage.append(q.p_usage)
        prediction.append(q.p_usage + 10)
        temp.append(q.temp)
        rh.append(q.rh)
    res = {
        'x_axis':x_axis, 
        'p_usage':p_usage, 
        'prediction':prediction, 
        'temp':temp, 
        'rh':rh
    }
    # print(res)
    return JsonResponse(res)


@api_view(['POST'])
def predict_energy(request):
    info = 'info'

    res = {
        'info': info, 
    }
    return JsonResponse(res)
