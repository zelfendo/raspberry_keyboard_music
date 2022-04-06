# raspberry_keyboard_music
  树莓派给小孩的玩具 
# 操作方法
## 1. 开机启动
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
## 2. 定时防止挂掉
```
crontab -e 
# 添加
XDG_RUNTIME_DIR=/run/user/user_id
*/2 * * * * /home/pi/Work/raspberry_keyboard_music/bin/always_run.sh
```
注意第一行的user_id需要改成自己的id，可以通过命令 id来查询,否则会碰到蓝牙播放无声音的问题
# 一些可能碰到的问题
## 1. 安装树莓派samba的时候，iphone不能写入
报错：

```不能完成此操作 未能完成操作 OSStatus 错误 100093```
  
解决策略：
```
1. vim /etc/samba/smb.conf
2. 搜索到[global]， 在下面加上
3. vfs objects = acl_xattr catia fruit streams_xattr
```

## 2. mplayer报错
 vim ~/.mplayer/config
ao=alsa
