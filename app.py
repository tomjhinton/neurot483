from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from datetime import datetime
import random
from dotenv import load_dotenv
import tweepy
import os
import io
import sys
import numpy as np
from PIL import Image, ImageFont, ImageOps, ImageChops
import requests
from random import randint, seed
import json
import math
import PIL

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def func2(p):
    return 255 - p

def Random_Alpha():
    l = ['A','B','C','D', 'E', 'F']
    return l[random.randint(0,5)]

def create( ):


    quote_font = ImageFont.truetype('test2.ttf', randint(350, 650))
    quote_font1 = ImageFont.truetype('test2.ttf', randint(350, 650))
    quote_font2 = ImageFont.truetype('test2.ttf', randint(350, 650))


    arr = [quote_font, quote_font1, quote_font2]

    arrG = ['testyn4.gif', 'testyn8.gif', 'testyn6.gif', 'testy7.gif', 'testy8.gif', 'testy9.gif', 'testyn3.gif', 'testyn2.gif']


    imgsize=(3000,3000)
    im2 = Image.new('RGBA', imgsize)




    im3 = PIL.Image.open(arrG[randint(0, 7)])
    im3.seek(randint(0, im3.n_frames-1))
    im3 = im3.convert('RGBA')
    im3 = im3.resize((3000, 3000))
    im6 = PIL.Image.open(arrG[randint(0, 7)])
    im6.seek(randint(0, im6.n_frames-1))
    im6 = im6.convert('RGBA')
    im6 = im6.resize((3000, 3000))
    im4 = ImageChops.difference(im6, im3)

    im3 = PIL.Image.open(arrG[randint(0, 7)])
    im3.seek(randint(0, im3.n_frames-1))
    im3 = im3.convert('RGBA')
    im3 = im3.resize((3000, 3000))
    im6 = PIL.Image.open(arrG[randint(0, 7)])
    im6.seek(randint(0, im6.n_frames-1))
    im6 = im6.convert('RGBA')
    im6 = im6.resize((3000, 3000))
    im7 = ImageChops.difference(im6, im3, )
    im7 = im7.rotate(10)
    im4 = ImageChops.difference(im4, im7)

    im3 = PIL.Image.open(arrG[randint(0, 7)])
    im3.seek(randint(0, im3.n_frames-1))
    im3 = im3.convert('RGBA')
    im3 = im3.resize((3000, 3000))
    im6 = PIL.Image.open(arrG[randint(0, 7)])
    im6.seek(randint(0, im6.n_frames-1))
    im6 = im6.convert('RGBA')
    im6 = im6.resize((3000, 3000))
    im8 = ImageChops.difference(im6, im3, )
    im8 = im8.rotate(10)
    im8 = ImageChops.composite(im6, im3, im8.convert("L"))
    im8 = ImageChops.difference(im4, im8)


    # im2 = ImageChops.difference(im2, im7)
    c_k = os.getenv("API_key")
    c_s = os.getenv("API_secret_key")
    a_k = os.getenv("Access_token")
    a_s = os.getenv("access_token_secret")
    auth = tweepy.OAuthHandler(c_k, c_s)
    auth.set_access_token(a_k, a_s)
    api = tweepy.API(auth)




    draw = ImageDraw.Draw(im2)
    for i in range(randint(400, 550)):
        draw = ImageDraw.Draw(im2)
        draw.multiline_text((randint(-10, 500),randint(-10, 500)), Random_Alpha(), tuple(np.random.randint(256, size=3)), font=arr[randint(0, 2)])
        quote_font = ImageFont.truetype('test2.ttf', randint(350, 1000))
        quote_font1 = ImageFont.truetype('test2.ttf', randint(350, 1000))
        quote_font2 = ImageFont.truetype('test2.ttf', randint(350, 1000))
        draw = ImageDraw.Draw(im2)
        arr = [quote_font,  quote_font1, quote_font2]
        im2 = im2.rotate(10)


    im2 = im2.filter(ImageFilter.CONTOUR)

    im2 = ImageChops.composite(im8, im7, im2.convert("L"))

    im2 = im2.convert('RGB')

    # im2.show()


    c_k = os.getenv("API_key")
    c_s = os.getenv("API_secret_key")
    a_k = os.getenv("Access_token")
    a_s = os.getenv("access_token_secret")
    auth = tweepy.OAuthHandler(c_k, c_s)
    auth.set_access_token(a_k, a_s)
    api = tweepy.API(auth)

    mapikc= os.getenv('musixmatch')

    albums = ['31785986', '21481176', '19901802']

    trackIds = requests.get(
  'https://api.musixmatch.com/ws/1.1/album.tracks.get?apikey='
  +  mapikc +
  '&album_id=' + albums[randint(0,2)]
)


    ids = trackIds.json()


    lyrics = requests.get(
      'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey='
      + mapikc +
      '&track_id=' + str(ids['message']['body']['track_list'][randint(0,len(ids['message']['body']['track_list'])-1 )]["track"]["track_id"])
    )

    lyrics = lyrics.json()


    print(lyrics)

    if(lyrics['message']['body']['lyrics']):
        i = lyrics['message']['body']['lyrics']['lyrics_body'].upper().split('\n')
        i = list(filter(lambda x : len(x) > 4 , i))
    elif(bool(lyrics['message']['body']['lyrics']) == False):
            lyrics = requests.get(
              'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey='
              + mapikc +
              '&track_id=' + str(ids['message']['body']['track_list'][randint(0,len(ids['message']['body']['track_list'])-1 )]["track"]["track_id"])
            )

            lyrics = lyrics.json()
            i = lyrics['message']['body']['lyrics']['lyrics_body'].upper().split('\n')
            i = list(filter(lambda x : len(x) > 4 , i))




    buf = io.BytesIO()
    im2.save(buf, format='PNG')
    buf.seek(0)
    thing = buf.getvalue()
    test = api.media_upload('art.png',file= buf)
    api.update_status(status=i[randint(0,len(i)-3)], media_ids=[test.media_id])

create()
