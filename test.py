#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from chain import *


epd = epd2in7b.EPD()
epd.init()
font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
font14 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 14)
blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
drawBl = ImageDraw.Draw(blimage)
drawRe = ImageDraw.Draw(reimage)


def start():
        epd.Clear(0XFF)
        blimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        reimage = Image.new('1',(epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH),255)
        drawBl = ImageDraw.Draw(blimage)
        drawRe = ImageDraw.Draw(reimage)
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
        drawBl.text((10,0),'weiwei go die',font = font24, fill = 0)
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()
def setting():
        epd.init()
        epd.Clear(0XFF)
        drawBl.rectangle((0,60,263,63),fill = 0)
        drawBl.rectangle((60,0,63,63),fill =0)
        drawBl.text((70,25),'Setting',font = font18,fill =0)
        okimage = Image.open('ok.bmp')
        setimage = Image.open('setting.bmp')
        replyimage = Image.open('reply.bmp')
	#
        qrcode = Image.open('addrs.bmp')
        blimage.paste(replyimage,(5,121))
        blimage.paste(setimage,(5,5))
        blimage.paste(okimage,(208,121))
	#
        qrcode = qrcode.resize((50,50),Image.ANTIALIAS)
        blimage.paste(qrcode,(128,116))
        epd.display(epd.getbuffer(blimage),(epd.getbuffer(reimage)))
        time.sleep(2)
        epd.sleep()
if __name__ == '__main__':
        #start()
        setting()
