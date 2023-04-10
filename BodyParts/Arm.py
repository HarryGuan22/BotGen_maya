import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Arm(object):
    def __init__(self, arm_type):
        self.index1 = random.randint(0, (len(arm_list)-1))
        self.index2 = random.randint(0, (len(arm_list)-1))
        self.name = 'arm'
        self.arm_type = arm_type
        print('The arm type is ' + self.arm_type)

arm_list = ['arm_geo_1','arm_geo_2']