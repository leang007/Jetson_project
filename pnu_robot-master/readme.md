#



connect to pNu_wifi pass pnurobot
check ip 

$ hostname -I

$ ssh root@172.24.1.1


set ros master to 172.24.1.1
set ros ip to this ip

clone git

change permission in folder script

```
sudo chmod +x *.py
```

1. 
'''
$ roslaunch pnu_robot pnu_mapping.launch
'''

'''
$ roslaunch pnu_robot visualize_run.launch
'''

move robot around
when finish
Ctrl + C All terminal

2.

'''
$ roslaunch pnu_robot make_mapping_pbstream.launch
$ roslaunch pnu_robot make_mapping_nav.launch
'''
