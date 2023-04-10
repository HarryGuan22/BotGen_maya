import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
class Pelvis(object):
    def __init__(self, torso_NT, leg_NT):
        self.index = random.randint(0, (len(pelvis_list)-1))
        self.name = 'pelvis'
        self.torso_NT = torso_NT
        self.leg_NT = leg_NT
        print("The pelvis consists of {} and {}\n".format(self.torso_NT.name, self.leg_NT.name))

pelvis_list = ['pelvis_geo_1', 'pelvis_geo_2','pelvis_geo_3']

   
         