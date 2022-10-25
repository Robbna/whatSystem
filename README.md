# What is _whatSystem_:grey_question:

_whatSystem_ is a python script that allows us to **know what operating system is running on the IP address** we provide.
Based on the [TTL](http://subinsb.com/default-device-ttl-values/#comment-3068871033) you will receive the OS being used.
#### :page_facing_up: Default TTL values:
| Device / OS | TTL |
| ----------- | --- |
| Linux/Unix  | 64  |
| Windows     | 128 |


### :closed_lock_with_key: REQUERIMENTS

- Python 3.10.4 or higher

```
sudo apt install python3-pip
```

### :computer: EXECUTION

You must to especify what ip address you want to analice.
```
python3 whatSystem.py [IP]
```
### :mag_right: EXAMPLE

```
s1k0@s1k0:~$ python3 whatSystem.py localhost

[*] System: LINUX (64 TTL)
```
```
s1k0@s1k0:~$ python3 whatSystem.py 127.0.0.1

[*] System: LINUX (64 TTL)
```
```
s1k0@s1k0:~$ python3 whatSystem.py 192.168.1.135

[*] System: WINDOWS (128 TTL)
```

