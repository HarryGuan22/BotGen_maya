import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Torso(object):
    def __init__(self, arm_NT, head_NT):
        self.index = random.randint(0, (len(torso_list)-1))
        # self.geo = cmds.ls(torso_list[index])[0]
        self.name = torso_list[self.index]
        self.arm_NT = arm_NT
        self.head_NT = head_NT
        
    def build(self):
        
        loc_up = cmds.ls('pg1_loc5')[0]
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo, loc_up])
        cmds.pointConstraint(loc_up, self.geo)

# torso_list = ['torso_geo_1', 'torso_geo_2','torso_geo_3']
torso_list = cmds.listRelatives('torso_GRP', c=True)