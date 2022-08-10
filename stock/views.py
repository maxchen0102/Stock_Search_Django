from django.shortcuts import render

from django.template.loader import get_template #讓你去使用模板（外觀）
from django.http import HttpResponse
from django import template
import twstock 
from twstock import Stock 
from twstock import realtime
import base64


import twstock 
from twstock import Stock 
from twstock import realtime
import matplotlib.pyplot as plt
import pandas as pd


#引入model 
from stock.models import StockTable1108,StockTable1201,StockTable1234,StockTable1604
from stock.models import StockTable2886,StockTable2887,StockTable2890,StockTable2892
from stock.models import StockTable3045,StockTable5876

from io import BytesIO

from stock.models import stock_list # 引入10支股票選項 在資料庫中 model 



def Yang_get_COVID19(request):
        t=get_template('gg.html')
        return HttpResponse(t.render(locals()))


def show_stock(request):
    if 'id' in request.GET and request.GET['id'] == '1':
        content=StockTable1108.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    elif 'id' in request.GET and request.GET['id'] == '2':
        content=StockTable1201.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    elif 'id' in request.GET and request.GET['id'] == '3':
        content=StockTable1234.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    elif 'id' in request.GET and request.GET['id'] == '4':
        content=StockTable1604.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    
    
    elif 'id' in request.GET and request.GET['id'] == '5':
        content=StockTable2886.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    elif 'id' in request.GET and request.GET['id'] == '6':
        content=StockTable2887.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    elif 'id' in request.GET and request.GET['id'] == '7':
        content=StockTable2890.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    elif 'id' in request.GET and request.GET['id'] == '8':
        content=StockTable2892.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    elif 'id' in request.GET and request.GET['id'] == '9':
        content=StockTable3045.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    
    elif 'id' in request.GET and request.GET['id'] == '10':
        content=StockTable5876.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    else:
        t=get_template('stock_list.html')
        return HttpResponse(t.render(locals()))







def show_picture(resuest):
    stock_1108=StockTable1108.objects.all()    
    stock_1108_pd = pd.DataFrame(stock_1108)
    stock_1108_pd = stock_1108_pd.set_index('stock_id')
    
    fig = plt.figure(figsize=(10, 6))
    plt.plot(stock_1108_pd.close, '-' , label="收盤價")
    plt.plot(stock_1108_pd.open, '-' , label="開盤價")
    plt.title('1108股份2018 開盤/收盤價曲線',loc='right')
    # loc->title的位置
    plt.xlabel('日期')
    plt.ylabel('收盤價')
    plt.grid(True, axis='y')
    plt.legend()
    fig.savefig('stock/static/image/stock_graph.png')
    
    t=get_template('graph.html')
    return HttpResponse(t.render(locals()))




'''
def first(request):
    if 'stock_name' in request.GET and request.GET['stock_name'] != '':
        #stock_name 是從get 得到的 定義了 你如果得到的話 會發生什麼事 定義在html 跳轉之類的
        return HttpResponse('Welcome!~' + request.GET['stock_name'])
    else:
        t=get_template('first_page.html') #沒有輸入東西的時候 停留在首頁 
        #然後 輸入之後 會在html設定跳轉之後的頁面是什麼 然後會攜帶所輸入的資訊
        return HttpResponse(t.render(locals()))
'''
'''
def welcome2(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        t=get_template('welcome.html')
        return HttpResponse(t.render(locals()))
''' 

def show_list(request):
    r1=stock_list.objects.all() # 把10個股票的資訊 存入choice 給html使用
    t=get_template('stock_list.html')
    return HttpResponse(t.render(locals()))
    


def real_stock(request):  
#=================
#即時查詢系統 
#================
#輸入你要查詢的股票代號 
#stock_number=input("enter your stock number ") 
    stock_number=request.GET['stock_name']
#得到所有當日即時資訊 包含一個為info的字典 在原字典中
    stock_info=twstock.realtime.get(stock_number) 
#把字典裡面的字典取出來d
    info=stock_info['info']
    info_real=stock_info['realtime']
    stock={
        'a':info['time'],
        'b':info['code'],
        'c':info['name'],
        'd':info['fullname'],
        'e':info_real['best_bid_price'],
        'f':info_real['best_bid_volume'],
        'g':info_real['best_ask_price'],
        'h':info_real['best_ask_volume'],
        "i":info_real['open'],
        "j":info_real['high'],
        "k":info_real['low'],
    }
    t=get_template('real.html')
    return HttpResponse(t.render(locals()))