#!/usr/bin/env python3
# def intoGeo(borderA, borderB, borderC, borderD):
def intoGeo():
    with open('out.txt', 'r') as f:
        line = f.readline()
        li_all = []
        while line:
            li = line.split()
            li_all.append(li)
            line = f.readline()
    
    # prev each el in li_all represents all agent regarding the same time 
    # below each el in trans represents all time of one agent
    trans = []
    for i in range(1, len(li_all[0])):
        agent = []
        for el in li_all:
            thistime = []
            thistime.append(el[i])
            thistime.append(el[0])
            agent.append(thistime)
        trans.append(agent)

    # the structure is already okay, just remove the "()" and turn into float
    # for el_1 in trans:
    #     for el_2 in el_1:
    #         # inner = []
    #         # pos = el_2[0][1:-1].split(",")
    #         # inner.append(float(pos[0]))
    #         # inner.append(float(pos[1]))
    #         # inner.append(float(el_2[1]))
    #         temp = el_2[0][1:-1].split(",")
    #         print(trans[1])
    #         el_1.append(el_1[1])
    #         el_1[0] = temp[0]
    #         el_1[1] = temp[1]
    #         # print(el_1)
    print(trans)

if __name__=="__main__":
    # print(intoGeo([18.063574122393632, 59.33534103086854],
    #               [18.063659496528416, 59.3352529905227],
    #               [18.06380822690251, 59.33529050684259],
    #               [18.063722852767725, 59.335378547188434]))
    intoGeo()