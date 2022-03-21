from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import student
# Create your views here.

def loginview( request ):
    print ( request.method, request.FILES)
    if request . method == 'POST':
        if len(request.FILES) == 0:
            return (
                render(request, 'askexcelfile.html')
                if request.POST['uid'] == 'litindia'
                and request.POST['password'] == 'litindia'
                else render(request, 'index.html', {'error': 'Invalid Login'})
            )

        with open ('data.csv', 'wb') as fileobj:
            fileobj . write ( request.FILES ['studfile'] . read() )
        df = pd . read_csv ('data.csv')
        i = 0
        img_list = []
        msg = []
        while i < len (df):
            name = df . loc [ i ] . Name
            cource = df . loc [ i ] . Cource
            reg = df . loc [ i ] . RegNo
            mid = df . loc [ i ] . Mailid
            if len ( student . objects .  filter ( name = name , cource = cource , regno = reg, mid = mid )) == 0:
                obj = student ( name = name , cource = cource , regno = reg, mid = mid )
                obj . save ()
                from PIL import Image
                from PIL import ImageFont
                from PIL import ImageDraw

                img = Image.open("login/static/lit.jpg")
                draw = ImageDraw.Draw(img)
                # font = ImageFont.truetype(<font-file>, <font-size>)
                font = ImageFont.truetype("./arial.ttf",25);
                # draw.text((x, y),"Sample Text",(r,g,b))
                draw.text((1035, 1720),name,(0,0,0),font=font)
                draw.text((1144, 2100),cource,(0,0,0),font=font)

                img_name=name + cource+'.jpg'
                img.save(f'login\\static\\certificate\\{img_name}')
                img_list . append ( img_name )
            else:
                msg.append( name + ' Allready taken Certificate on ' + cource + ' having REGNo ' + str(reg))
            i += 1
        # if not msg :
        #     msg = str ( img_list )

        return render (request, 'display.html', {'img_list':img_list, 'msg':msg})
    return render ( request, 'index.html')
