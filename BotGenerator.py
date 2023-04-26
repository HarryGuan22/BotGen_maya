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
    
    @classmethod
    def get_info_dict(cls, robot):
        info_dict = {}
        info_dict['Bot_type'] = robot.type
        info_dict['Pelvis'] = robot.pelvis_NT.name
        info_dict['Torso'] = robot.pelvis_NT.torso_NT.name
        info_dict['Kinetic_leg'] = robot.pelvis_NT.leg_NT.kinetic_name
        info_dict['Supporting_leg'] = robot.pelvis_NT.leg_NT.sup_name
        info_dict['Arm'] = robot.pelvis_NT.torso_NT.arm_NT.name
        info_dict['Head'] = robot.pelvis_NT.torso_NT.head_NT.name
        return info_dict
            
        

if __name__ == '__main__':
    if cmds.objExists('output'):
        cmds.delete('output', 'output1', 'output2')
        joints = cmds.ls(type='joint')
        cmds.delete(joints)

        
    
    
    r1 = BotGenerator.generate()
    bot1_info = BotGenerator.get_info_dict(robot=r1)
    
    r2 = BotGenerator.generate()
    bot2_info = BotGenerator.get_info_dict(robot=r2)
    
    r3 = BotGenerator.generate()
    bot3_info = BotGenerator.get_info_dict(robot=r3)
    
    br = BotRenderer()
    
    # obj = br.leg_list[0]
    # test = cmds.listRelatives(obj, c=True, typ='transform')
    # br.torso_locs
    
    br.render(info=bot1_info, pos='render_pos_1')
    br.render(info=bot2_info, pos='render_pos_2')
    br.render(info=bot3_info, pos='render_pos_3')
    
    cmds.select(clear=True)
    # b.pelvis_NT.index
    # br.pelvis_list[1]
    # br.pelvis_geo
    # br.pelvis
    # cmds.duplicate(br.pelvis_list[1])
    
