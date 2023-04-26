import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Leg(object):
    def __init__(self, leg_type):
        # index1 is used for essential legs
        self.leg_count = random.randint(2,3)
        self.index1 = random.randint(0, (len(kinetic_leg_list)-1))
        self.kinetic_name = kinetic_leg_list[self.index1]
        self.sup_name = 'None'
        if self.leg_count == 3:
            # self.index2 = random.randint(0, (len(sup_leg_list)-1))
            # self.sup_name = sup_leg_list[self.index2]
            self.sup_name = sup_leg_list[0]
        # index2 is used for supporting leg

        self.leg_type = leg_type

        
    def build(self):
        loc_left = cmds.ls('pg1_loc1')[0]
        loc_right = cmds.ls('pg1_loc2')[0]
        
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo1, loc_left])
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo2, loc_right])
        cmds.parentConstraint(loc_left, self.geo1)
        cmds.parentConstraint(loc_right, self.geo2)
kinetic_leg_list = ['leg_geo_1', 'leg_geo_2','leg_geo_3', 'leg_geo_4', 'leg_geo_5']
sup_leg_list = ['sup_geo_1']