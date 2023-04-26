import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Arm(object):
    def __init__(self, arm_type):
        self.index = random.randint(0, (len(arm_list)-1))
        self.name = arm_list[self.index]
        self.arm_type = arm_type


arm_list = cmds.listRelatives('arm_GRP', c=True)