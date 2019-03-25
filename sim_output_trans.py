#!/usr/bin/env python3

def intoGeo(borderA, borderB, borderC, borderD):
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

    # trans structure is by now okay, below removes the "()" and turn into float
    for agt in trans:
        for i in range(len(agt)):
            agt[i].append(float(agt[i][1]))
            temp = agt[i][0][1:-1].split(',')
            agt[i][0] = float(temp[0])
            agt[i][1] = float(temp[1])

    # turn into geo-coordinates
    # parameters here should change on demand
    xRate = [(borderB[0] - borderA[0])/400, (borderB[1] - borderA[1])/400]
    yRate = [(borderB[0] - borderC[0])/400, (borderB[1] - borderC[1])/400]
    geoCenter = [(borderA[0] + borderC[0])/2, (borderA[1] + borderC[1])/2]
    for agt in trans:
        for i in range(len(agt)):
            xGeo = agt[i][0] * xRate[0] + agt[i][1] * yRate[0]
            yGeo = agt[i][0] * xRate[1] + agt[i][1] * yRate[1]
            agt[i][0] = xGeo + geoCenter[0]
            agt[i][1] = yGeo + geoCenter[1]

    # turn trans into final deckgl format [{'trajectory':[[x,y,t]]}]
    res = []
    for agt in trans:
        res.append({'trajectory': agt})
    res = str(res).replace("'", "\"")
    
    print(res)

if __name__=="__main__":
    # example below is a rough square on zebras
    intoGeo([18.063574122393632, 59.33534103086854],
                  [18.063659496528416, 59.3352529905227],
                  [18.06380822690251, 59.33529050684259],
                  [18.063722852767725, 59.335378547188434])