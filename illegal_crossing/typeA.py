#!/usr/bin/env python3
# Flow rates plan, per 100s:
# 120+60, 110+55, 100+50,...,20+10, 6+3

import threading

# first 10s of clean road, 10+5 (1/s and 1/2s), agents appearing both sides
class Simulation:
    def __init__(self):
        self.t = 0.0
        # via [random.randint(0,10) for i in range(10)]
        self.seqR = [5, 3, 1, 10, 3, 10, 6, 1, 10, 4]
        self.seqL = [5, 10, 1, 1, 6]
        self.agentsR = []
        self.agentsL = []
        self.illealR = []
        self.illealL = []

    def typeA(self):
        # run decision-making script every 0.5 seconds
        sim = threading.Timer(0.5, self.typeA)
        sim.start()

        print('t = ' + str(self.t))
        # agents arriving
        if self.t > 0 and int(self.t) == self.t:
            self.agentsR.append(self.seqR[int(self.t)-1])
        if self.t > 0 and int(self.t) == self.t and self.t % 2 == 0:
            self.agentsL.append(self.seqL[int(self.t/2)-1])
        print('rightBefore ' + str(self.agentsR))
        print('leftBefore ' + str(self.agentsL))
        
        # if illegals in view more than threshold, runs the light
        # right
        run = []
        for i in range(len(self.agentsR)):
            if len(self.illealR) >= self.getThre(int(self.t), 'R', self.agentsR[i]):
                self.illealR.append(self.agentsR[i])
                run.append(i)
        self.agentsR = [i for j, i in enumerate(self.agentsR) if j not in run]
        # left
        run = []
        for i in range(len(self.agentsL)):
            if len(self.illealL) >= self.getThre(int(self.t), 'L', self.agentsL[i]):
                self.illealL.append(self.agentsL[i])
                run.append(i)
        self.agentsL = [i for j, i in enumerate(self.agentsL) if j not in run]

        # output in-time results
        print('rightAfter ' + str(self.agentsR))
        print('illegal right  ' + str(self.illealR))
        print('leftAfter  ' + str(self.agentsL))
        print('illegal left  ' + str(self.illealL))
        
        self.t += 0.5

        # stop simulation
        if self.t >= 11:
            sim.cancel()

    def getThre(self, t: int, road: str, hurry: int) -> int:
        # Road width = 9
        if road == 'R':
            if t == 0:
                if hurry == 0: return 40
                elif hurry == 1: return 25
                elif hurry == 2: return 20
                elif hurry == 3: return 13
                elif hurry == 4: return 8
                elif hurry == 5: return 5
                elif hurry == 6: return 3
                elif hurry == 7: return 2
                elif hurry == 8: return 1
                elif hurry >= 9: return 0
            elif t == 1:
                if hurry == 0: return 30
                elif hurry == 1: return 18
                elif hurry == 2: return 13
                elif hurry == 3: return 7
                elif hurry == 4: return 5
                elif hurry == 5: return 3
                elif hurry == 6: return 1
                elif hurry >= 7: return 0
            elif t == 2:
                if hurry == 0: return 20
                elif hurry == 1: return 13
                elif hurry == 2: return 9
                elif hurry == 3: return 6
                elif hurry == 4: return 3
                elif hurry == 5: return 2
                elif hurry >= 6: return 0
            elif t == 3:
                if hurry == 0: return 18
                elif hurry == 1: return 11
                elif hurry == 2: return 7
                elif hurry == 3: return 4
                elif hurry == 4: return 1
                elif hurry >= 5: return 0
            elif t == 4:
                if hurry == 0: return 15
                elif hurry == 1: return 9
                elif hurry == 2: return 5
                elif hurry == 3: return 2
                elif hurry >= 4: return 0
            elif t == 5:
                if hurry == 0: return 13
                elif hurry == 1: return 7
                elif hurry == 2: return 4
                elif hurry == 3: return 1
                elif hurry >= 4: return 0
            elif t == 6:
                if hurry == 0: return 10
                elif hurry == 1: return 6
                elif hurry == 2: return 2
                elif hurry >= 3: return 0
            elif t == 7:
                if hurry == 0: return 9
                elif hurry == 1: return 4
                elif hurry == 2: return 1
                elif hurry >= 3: return 0
            # after 7s nobody runs the light
            else:
                return 1000
        # Road width = 12
        if road == 'L':
            if t == 0:
                if hurry == 0: return 50
                elif hurry == 1: return 35
                elif hurry == 2: return 25
                elif hurry == 3: return 16
                elif hurry == 4: return 10
                elif hurry == 5: return 7
                elif hurry == 6: return 4
                elif hurry == 7: return 2
                elif hurry == 8: return 1
                elif hurry == 9: return 1
                elif hurry == 10: return 0
            elif t == 1:
                if hurry == 0: return 35
                elif hurry == 1: return 22
                elif hurry == 2: return 16
                elif hurry == 3: return 9
                elif hurry == 4: return 6
                elif hurry == 5: return 4
                elif hurry == 6: return 2
                elif hurry == 7: return 1
                elif hurry == 8: return 1
                elif hurry >= 9: return 0
            elif t == 2:
                if hurry == 0: return 25
                elif hurry == 1: return 17
                elif hurry == 2: return 11
                elif hurry == 3: return 7
                elif hurry == 4: return 4
                elif hurry == 5: return 2
                elif hurry == 6: return 1
                elif hurry >= 7: return 0
            elif t == 3:
                if hurry == 0: return 22
                elif hurry == 1: return 14
                elif hurry == 2: return 9
                elif hurry == 3: return 6
                elif hurry == 4: return 2
                elif hurry == 5: return 1
                elif hurry >= 6: return 0
            elif t == 4:
                if hurry == 0: return 19
                elif hurry == 1: return 12
                elif hurry == 2: return 7
                elif hurry == 3: return 5
                elif hurry == 4: return 2
                elif hurry >= 5: return 0
            elif t == 5:
                if hurry == 0: return 15
                elif hurry == 1: return 9
                elif hurry == 2: return 5
                elif hurry == 3: return 4
                elif hurry == 4: return 1
                elif hurry >= 5: return 0
            elif t == 6:
                if hurry == 0: return 12
                elif hurry == 1: return 8
                elif hurry == 2: return 3
                elif hurry == 3: return 2
                elif hurry >= 4: return 0
            elif t == 7:
                if hurry == 0: return 10
                elif hurry == 1: return 7
                elif hurry == 2: return 2
                elif hurry == 3: return 1
                elif hurry >= 4: return 0
            # after 7s nobody runs the light
            else:
                return 1000


if __name__=="__main__":
    obj = Simulation()
    obj.typeA()