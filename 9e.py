import threading
x=0
count=10
lock=threding.lock()
define incr()
for i in range(count)
x+=1
display x
define decr()
for i in range(count)
x-=1
display x
t1=threading.thread(target=incr)
t2=threading.thread(target=decr)