killall mplayer
nohup mplayer -nolirc  $1 -ss 00:00:$3 > dev/null 2>&1 &
