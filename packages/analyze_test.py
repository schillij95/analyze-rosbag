import rosbag
import numpy as np
bag = rosbag.Bag('/home/amod20-rh3-ex-record-Julian-Schilliger.bag')
topics = []
for topic, msg, t in bag.read_messages():
    topics.append(topic)
topics = set(topics)
#print(topics)
for name in topics:
    num_msgs = 0
    list = []
    time = []
    for topic, msg, t in bag.read_messages(topics=[name]):
        num_msgs += 1
        if(len(list) > 0):
            time.append(t.to_sec()-list[-1])
        list.append(t.to_sec())
    nplist = np.asarray(time)
    mean = np.mean(nplist)
    median = np.median(nplist)
    min = np.min(nplist)
    max = np.max(nplist)
    print(name)
    if(num_msgs > 1):
        print("num_msgs, mean, median, min, max")
        print(num_msgs, mean, median, min, max)
    else:
        print("only 1 message received")
bag.close()
