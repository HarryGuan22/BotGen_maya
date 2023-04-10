import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
class Robot(object):
    def __init__(self, pelvis_NT):
        self.name='Robot'
        self.pelvis_NT = pelvis_NT
        print("The robot consists of: ( Pelvis:{} )\n".format(self.pelvis_NT.name))
         