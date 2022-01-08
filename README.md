# raspberry_keyboard_music
  树莓派给小孩的玩具 
# 一些可能碰到的问题
## 1. 安装树莓派samba的时候，iphone不能写入
报错：

不能完成此操作 未能完成操作 OSStatus 错误 100093
  
解决策略：
1. vim /etc/samba/smb.conf
2. 搜索到[global]， 在下面加上
3. vfs objects = acl_xattr catia fruit streams_xattr

