import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Head(object):
    def __init__(self, head_type):
        self.index = random.randint(0, (len(head_list)-1))
        # self.geo = cmds.ls('head_geo_1')[0]
        self.name = 'head'
        self.head_type = head_type
        print('The head type is ' + self.head_type)
        
    def build(self):
        loc_neck = cmds.ls('tg1_loc1')[0]
        # nmUtil.align_lras(snap_align=True, delete_history=False, sel=[self.geo, loc_neck])
        cmds.pointConstraint(loc_neck,self.geo)

head_list = ['head_geo_1','head_geo_2','head_geo_3']
