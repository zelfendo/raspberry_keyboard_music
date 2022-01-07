#!/usr/bin/env python
#coding:utf-8

from select import select
import os
HOME_PATH = '/home/pi/Work/raspberry_keyboard_music'
MUSIC_PATH = '/home/pi/music'
DEVICE_NAME = '/dev/input/event1'
def log(s):
  print s

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
  log(fname)
  os.system("bash -x %s/bin/player.sh %s >> tool/start.log 2>&1" % (HOME_PATH, fname))
def stop_music():
  os.system("bash -x %s/bin/stop.sh >> tool/start.log 2>&1" % HOME_PATH)

def loop_play_music(music_list):
  from evdev import InputDevice
  dev = InputDevice(DEVICE_NAME)
  while True:
    select([dev], [], [])
    for event in dev.read():
      if event.type != 1 : continue # ONLY KEYBOARD
      if event.value != 1 : continue # ONLY PRESS
      if event.code == 1 or "%s" % event.code == "01":
        stop_music()
      else:
        log(type(event.code))
        play_music(music_list, event.code-1)


if __name__ == '__main__':
   music_list = get_music_list()
   loop_play_music(music_list)
