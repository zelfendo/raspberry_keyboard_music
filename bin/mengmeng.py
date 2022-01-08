#!/usr/bin/env python
#coding:utf-8

import logging
import os

HOME_PATH = '/home/pi/Work/raspberry_keyboard_music'
MUSIC_PATH = '/home/music'
DEVICE_NAME = '/dev/input/event0'
#OFFSET = 1
OFFSET = 2 # for my keyboard 's first key is broken

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='%s/logs/main.log' % HOME_PATH , level=logging.DEBUG, format=LOG_FORMAT)


def get_music_list():
  ''' 获得目标路径的音乐'''
  file_list = os.listdir(MUSIC_PATH)
  ret_list = []
  for file_name in file_list:
    path = os.path.join(MUSIC_PATH, file_name)
    if os.path.isfile(path):
       ret_list.append(path)
  return ret_list

def play_music(music_list, number):
  index = number % len(music_list)
  fname = music_list[index]
  logging.info("播放序号[%02d]%s" % (index, fname))
  if fname.endswith("mp3"):
    os.system("bash -x %s/bin/player.sh %s %s/logs/player.log 15 >> %s/logs/start.log 2>&1" % (HOME_PATH, fname, HOME_PATH, HOME_PATH))
  else:
    os.system("bash -x %s/bin/player.sh %s %s/logs/player.log 00 >> %s/logs/start.log 2>&1" % (HOME_PATH, fname, HOME_PATH, HOME_PATH))
def stop_music():
  os.system("bash -x %s/bin/stop.sh >> %s/logs/stop.log 2>&1" % (HOME_PATH, HOME_PATH))

def loop_play_music(music_list):
  from evdev import InputDevice
  from select import select
  dev = InputDevice(DEVICE_NAME)
  while True:
    select([dev], [], [])
    for event in dev.read():
      if event.type != 1 : continue # ONLY KEYBOARD
      if event.value != 1 : continue # ONLY PRESS
      if event.code == 1 or "%s" % event.code == "01":
        stop_music()
      else:
        play_music(music_list, event.code-OFFSET)


if __name__ == '__main__':
   music_list = get_music_list()
   loop_play_music(music_list)
