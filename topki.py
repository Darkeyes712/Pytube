import os

for i in os.listdir('C:\\Users\\nikol\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\moviepy\\video\\fx'):
    hui = i.split('.')[0]
    print(f'from moviepy.video.fx.{hui} import {hui}')