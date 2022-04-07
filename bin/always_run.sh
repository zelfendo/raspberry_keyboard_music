#!/usr/bin/bash
# 计算启动进城数量
NUM=`ps -eaf|grep -v grep |grep "python3 /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py"|wc -l`
if [ $NUM -eq 0 ]; then
  # 0-驻守进城-启动 
  nohup python3 /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py > /home/pi/Work/raspberry_keyboard_music/logs/deamon.log 2>&1 &
fi
if [ $NUM -gt 1 ]; then
  # > 1 - 杀死全部重新启动
  for i in `ps -eaf|grep -v grep |grep "python3 /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py"|sed -r "s/[ ]+/ /g"|cut -f 2 -d" "`;
  do
    kill -9 $i
  done
  nohup python3 /home/pi/Work/raspberry_keyboard_music/bin/mengmeng.py > /home/pi/Work/raspberry_keyboard_music/logs/deamon.log 2>&1 &
fi
