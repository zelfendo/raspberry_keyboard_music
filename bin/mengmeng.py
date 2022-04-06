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

# 蓝牙键盘不标准，不是按照0-xx排列的顺序，导致不确定那个按键是哪首歌,重新映射
keyboard_map = {}
def load_keyboard_map():
  try:
    f = open(HOME_PATH + "/bin/keyboard_map")
    for i in f:
      if i.strip() != "":
        index = len(keyboard_map) + 1
        keyboard_map[int(i)] = index
  except Exception as e:
    logging.info("加载keyboard_map失败:%s" % e)

def get_music_list():
  ''' 获得目标路径的音乐'''
  file_list = os.listdir(MUSIC_PATH)
  ret_list = []
  for file_name in file_list:
    path = os.path.join(MUSIC_PATH, file_name)
    if os.path.isfile(path):
       ret_list.append(path)
  ret_list.sort()
  return ret_list

def play_music(music_list, number):
  index = number % len(music_list)
  fname = "'%s'" % music_list[index]
  logging.info("播放序号[%02d]%s" % (index, fname))
  if "mp3" in fname:
    os.system("bash -x %s/bin/player.sh %s %s/logs/player.log 10 >> %s/logs/start.log 2>&1" % (HOME_PATH, fname, HOME_PATH, HOME_PATH))
  else:
    os.system("bash -x %s/bin/player.sh %s %s/logs/player.log 00 >> %s/logs/start.log 2>&1" % (HOME_PATH, fname, HOME_PATH, HOME_PATH))
def stop_music():
  os.system("bash -x %s/bin/stop.sh >> %s/logs/stop.log 2>&1" % (HOME_PATH, HOME_PATH))

def loop_play_music():
  from evdev import InputDevice
  from select import select
  dev = InputDevice(DEVICE_NAME)
  while True:
    music_list = get_music_list()
    select([dev], [], [])
    for event in dev.read():
      if event.type != 1 : continue # ONLY KEYBOARD
      if event.value != 1 : continue # ONLY PRESS
      code = keyboard_map.get(event.code, event.code)
      logging.info("键盘事件Type:[%02d]value[%s]code[%s]new_code[%s]" % (event.type, event.value, event.code, code))
      #if event.code <= OFFSET or ("%d" % event.code) <= ("%d" % OFFSET):
      if code <= OFFSET:
        stop_music()
      else:
        play_music(music_list, code-OFFSET)


if __name__ == '__main__':
   load_keyboard_map()
   loop_play_music()
