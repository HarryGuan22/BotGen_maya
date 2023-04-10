import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Leg(object):
    def __init__(self, leg_type):
        # index1 is used for essential legs
        self.leg_count = random.randint(2,3)
        self.index1 = random.randint(0, (len(leg_list)-1))
        # index2 is used for supporting leg
        self.index2 = random.randint(0, (len(leg_list)-1))
        # self.geo1 = cmds.ls(leg_list[index1])[0]
        # self.geo2 = cmds.ls(leg_list[index2])[0]
        # self.geo1 = cmds.ls('leg_geo_1')[0]
        # self.geo2 = cmds.duplicate(self.geo1)[0]
        self.name = 'leg'
        self.leg_type = leg_type
        print('The legz type is ' +self.leg_type)
        
    def build(self):
        loc_left = cmds.ls('pg1_loc1')[0]
        loc_right = cmds.ls('pg1_loc2')[0]
        
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo1, loc_left])
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo2, loc_right])
        cmds.parentConstraint(loc_left, self.geo1)
        cmds.parentConstraint(loc_right, self.geo2)
leg_list = ['leg_geo_1', 'leg_geo_2']