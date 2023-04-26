import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import random
import itertools
class Pelvis(object):
    def __init__(self, torso_NT, leg_NT):
        self.index = random.randint(0, (len(pelvis_list)-1))
        self.name = pelvis_list[self.index]
        self.torso_NT = torso_NT
        self.leg_NT = leg_NT
        
upPelvis_list = cmds.listRelatives('upright_pelvis_GRP', c=True)
quadPelvis_list = cmds.listRelatives('quad_pelvis_GRP', c=True)
insectPelvis_list = cmds.listRelatives('insect_pelvis_GRP', c=True)
# packed_list = itertools.zip_longest(upPelvis_list, quadPelvis_list, fillvalue=None)
packed_list = itertools.zip_longest(upPelvis_list, quadPelvis_list, insectPelvis_list, fillvalue=None)
pelvis_list = [item for sublist in packed_list for item in sublist if item is not None]

