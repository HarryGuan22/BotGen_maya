import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
class Robot(object):
    def __init__(self, pelvis_NT):
        
       
        self.pelvis_NT = pelvis_NT
        self.type = 'None'
        if 'up' in pelvis_NT.name:
            self.type = 'upright'
        elif 'quad' in pelvis_NT.name:
            self.type = 'quadruped'
        elif 'insect' in pelvis_NT.name:
            self.type = 'insectile'
        
       

botType_list = ['upright', 'quadruped', 'insectile']