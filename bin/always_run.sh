#!/usr/bin/bash
NUM=`ps -eaf|grep -v grep |grep "python /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py"|wc -l`
if [ $NUM -eq 0 ]; then
  nohup python /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py > /home/pi/Work/raspberry_keyboard_music/logs/null 2>&1 & 
fi
if [ $NUM -gt 1 ]; then
  for i in `ps -eaf|grep -v grep |grep "python /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py"|sed -r "s/[ ]+/ /g"|cut -f 2 -d" "`;
  do
    kill -9 $i
  done
  nohup python /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py > /home/pi/Work/raspberry_keyboard_music/logs/null 2>&1 & 
fi
