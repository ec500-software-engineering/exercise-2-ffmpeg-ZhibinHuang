import os
import asyncio
import queue
import threading
import time

def convert_video(Q):
    while (not Q.empty()):
        f = Q.get()
        start_time = time.time()
        async def covert_720p():
            os.system("./ffmpeg -i ./in/{} -b:v 2000k -bufsize 2000k -r 30  -strict -2 -s 1280x720 \
            ./out/{}_720p.mp4".format(f,f))
            print(threading.currentThread())
            os.system('ps - ef | grep python')
            #print("thread 1")
            #await asyncio.sleep(1)
            return '720P covert successfully'
        async def covert_480p():
            os.system("./ffmpeg -i ./in/{} -b:v 1000k -bufsize 2000k -r 30  -strict -2 -s 720x480 \
            ./out/{}_480p.mp4".format(f,f))
            print(threading.currentThread())
            os.system('ps - ef | grep python')
            #print("thread 2")
            #await asyncio.sleep(1)
            return '480P covert successfully'

        coroutine1 = covert_720p()
        coroutine2 = covert_480p()

        tasks = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
        ]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))

        for task in tasks:
            print('Task: ', task.result(),"for file {}".format(f))
        print('Time: ',time.time() - start_time)


if __name__ == '__main__':
    Q = queue.Queue()
    path = './in'
    files = os.listdir(path)
    for file in files:
        Q.put(file)
    Q.get()
    #convert_video(Q)
    while (not Q.empty()):
        print(Q.get())

