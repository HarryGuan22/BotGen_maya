from SPBotGen.BodyParts.Robot import Robot
from SPBotGen.BodyParts.Pelvis import Pelvis
from SPBotGen.BodyParts.Torso import Torso
from SPBotGen.BodyParts.Arm import Arm
from SPBotGen.BodyParts.Leg import Leg
from SPBotGen.BodyParts.Head import Head
from SPBotGen.BotRenderer import BotRenderer
import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil

class BotGenerator(object):
    @classmethod
    def generate(cls):
        return Robot(Pelvis(Torso(Arm('1'),Head('1')), Leg('1')))
        

if __name__ == '__main__':
    if cmds.objExists('output'):
        cmds.delete('output', 'output1', 'output2')
        
    
    robots = []
    r1 = BotGenerator.generate()
    robots.append(r1)
    r2 = BotGenerator.generate()
    robots.append(r2)
    r3 = BotGenerator.generate()
    robots.append(r3)
    br = BotRenderer()
    # br.torso_locs
    br.render(robot=r1, pos='render_pos_1')
    br.render(robot=r2, pos='render_pos_2')
    br.render(robot=r3, pos='render_pos_3')

    # br.head_geo
    # br.head
    # br.pelvis
    # br.pelvis_geo
    # br.pelvis_locs
    # cmds.listRelatives(br.pelvis)
    # nmUtil.align_lras(snap_align=True, delete_history=True, sel=[br.torso, self.pelvis_locs[-1]])

    # b.pelvis_NT.index
    # br.pelvis_list[1]
    # br.pelvis_geo
    # br.pelvis
    # cmds.duplicate(br.pelvis_list[1])
    cmds.exactWorldBoundingBox