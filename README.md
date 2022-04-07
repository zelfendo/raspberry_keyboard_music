# raspberry_keyboard_music
  用树莓派做的小孩玩具，适合1岁多的孩子，用来安抚孩子。
  主要功能：
  	按键盘，随机播放/home/music下的mp3文件
	按键盘第一个键，停止播放
# 操作方法
## 1. 设置开机启动
设置启动：
```
sudo cp bin/always_run.sh /etc/init.d/
cd /etc/init.d/
sudo update-rc.d always_run.sh defaults 100
```
关闭启动：
```
cd /etc/init.d
sudo update-rc.d -f always_run.sh remove
rm always_run.sh
```
## 2. 设置定时防止挂掉
```
crontab -e
# 添加
XDG_RUNTIME_DIR=/run/user/user_id
*/2 * * * * /home/pi/Work/raspberry_keyboard_music/bin/always_run.sh
```
注意第一行的user_id需要改成自己的id，可以通过命令 id来查询,否则会碰到蓝牙播放无声音的问题

## 3. 其他设置
### 3.1 配置
其他配置都在bin/mengmeng.py文件里面
*  HOME_PATH: 文件的地址，用来设置环境变量
* MUSIC_PATH: mp3文件的地址，注意如果使用ftp或者scp更新文件注意文件权限
* DEVICE_NAME: 键盘的设备id
* OFFSET: 默认=1，我的键盘第一个键坏了，所以这个用第二个键盘来做停止键
* USE_KEY_MAP: 是否使用keymap，默认使用，不标准的蓝牙键盘（例如我的）的键不是按照顺序来的，这里做的是影射，可以编辑成自己的，如果对播放顺序不抱有期望，可以设置成false
### 3.2 文件说明
```
├── bin 
│   ├── always_run.sh # 驻守进城启动程序，定时启动驻守进程
│   ├── keyboard_map  # 键盘映射关系，USE_KEY_MAP=false时候不用
│   ├── mengmeng.py   # 驻守监听程序
│   ├── player.sh     # 启动播放器, 可以根据自己安装的播放器修改
│   └── stop.sh       # 杀死播放器
├── logs
│   ├── main.log      # 主日志
│   ├── start.log     # 启动播放器日志
│   ├── stop.log      # 停止播放器日志
│   └── deamon.log    # 驻守进城的日志
└── README.md
```
