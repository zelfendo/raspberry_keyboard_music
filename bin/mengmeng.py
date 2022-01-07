#!/usr/bin/env python
#coding: utf-8

from evdev import InputDevice
from select import select
import os

MUSIC_PATH = '/home/pi/music'
DEVICE_NAME = '/dev/input/event1'

def log(s):
  print s
def get_target_music():

    list = os.listdir(MUSIC_PATH)
    ret_list = []
    for i in range(0,len(list)):
      path = os.path.join(MUSIC_PATH,list[i])
      if os.path.isfile(path):
         ret_list.append(path)
    return ret_list
def play_music(music_list, number):
    index = number % len(music_list)
    fname = music_list[index]
    log(fname)
    os.system("bash -x tool/player.sh %s >> tool/start.log 2>&1" % fname)
def stop_music():
        os.system("bash -x tool/stop.sh >> tool/start.log 2>&1")


def loop_run(music_list):
  dev = InputDevice(DEVICE_NAME)
  while True:
    select([dev], [], [])
    for event in dev.read():
      if event.type != 1 : continue
      if event.value != 1 : continue
      if event.code == 1 or "%s" % event.code == "01":
        stop_music()
      else:
        log(type(event.code))
        play_music(music_list, event.code)
      # print "Key: %s Status: %s" % (event.code, "pressed" if event.value else "release")




if __name__ == '__main__':
   music_list = get_target_music()
   loop_run(music_list)
