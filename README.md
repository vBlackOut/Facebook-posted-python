# Facebook-posting-python  
post your comment automatical  

requirement  
Python3.5 and Selenium  
Pyvirtualdisplay

just install it  
```
python3 -m pip install selenium  
python3 -m pip install pyvirtualdisplay
```

and edit your login and password, just add your comment 

```
for login
crawler_facebook.login("my_email","mypassword")

for add your post
crawler_facebook.create_post("your_post")
```


```
for disable display

crawler_facebook = Facebook(show=1)

set show = 0
# example
crawler_facebook = Facebook(show=0)
```

for start  
python3 main.py
