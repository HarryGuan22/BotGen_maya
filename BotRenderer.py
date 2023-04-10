import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
class BotRenderer(object):
    def __init__(self):
       self.pelvis_list =  ['pelvis_geo_1', 'pelvis_geo_2','pelvis_geo_3']
       self.torso_list = ['torso_geo_1', 'torso_geo_2', 'torso_geo_3']
       self.leg_list = ['leg_geo_1', 'leg_geo_2']
       self.head_list = ['head_geo_1','head_geo_2','head_geo_3']
       self.arm_list = ['arm_geo_1','arm_geo_2']
    def render(self, robot, pos='render_pos'):
        self.pos = cmds.ls(pos)[0]
        self.output_grp = cmds.group(em=True, n='output')
        nmUtil.a_to_b(sel=[self.output_grp, self.pos])
        self.renderPelvis(robot.pelvis_NT)
        
    
    def renderPelvis(self, pelvis):
        index = pelvis.index
        self.pelvis_geo = self.pelvis_list[index]
        self.pelvis = cmds.duplicate(self.pelvis_geo, name='pelvis_output', renameChildren=True)[0]
        self.children = cmds.listRelatives(self.pelvis, children=True)
        for i, c in enumerate(self.children):
            if cmds.objectType(c) != 'shape':
                new_name = self.pelvis + '_loc_' + str(i)
                cmds.rename(c, new_name)
        self.pelvis_locs = cmds.listRelatives(self.pelvis, children=True)
        nmUtil.a_to_b(sel=[self.pelvis, self.pos])
        # cmds.makeIdentity(self.pelvis, apply=True)
        cmds.parent(self.pelvis, self.output_grp)
        self.renderTorso(pelvis.torso_NT)
        self.renderLeg(pelvis.leg_NT)
    def renderTorso(self, torso):
        index = torso.index
        self.torso_geo = self.torso_list[index]
        self.torso = cmds.duplicate(self.torso_geo, name='torso_output', renameChildren=True)[0]
        self.torso_children = cmds.listRelatives(self.torso, children=True)
        for i, c in enumerate(self.torso_children):
            if cmds.objectType(c) != 'shape':
                new_name = self.torso + '_loc_' + str(i)
                cmds.rename(c, new_name)
        self.torso_locs = cmds.listRelatives(self.torso, children=True)
        nmUtil.a_to_b(sel=[self.torso, self.pelvis_locs[-1]])
        # nmUtil.align_lras(snap_align=True, delete_history=True, sel=[self.torso, self.pelvis_locs[-1]])
        cmds.parent(self.torso, self.output_grp)
        self.renderArm(torso.arm_NT)
        self.renderHead(torso.head_NT)
    def renderHead(self, head):
        index = head.index
        self.head_geo = self.head_list[index]
        self.head = cmds.duplicate(self.head_geo, name='head_output', renameChildren=True)[0]
        
        nmUtil.align_lras(snap_align=True, delete_history=True, sel=[self.head, self.torso_locs[-1]])
        cmds.parent(self.head, self.output_grp)
    def renderLeg(self, leg):
        index1 = leg.index1
        self.ess_leg_geo = self.leg_list[index1]
        
        self.essLeg_1 = cmds.duplicate(self.ess_leg_geo, name='essLeg1_output', renameChildren=True)[0]
        self.essLeg_2 = cmds.duplicate(self.ess_leg_geo, name='essLeg2_output', renameChildren=True)[0]
        nmUtil.align_lras(snap_align=True,  sel=[self.essLeg_1, self.pelvis_locs[1]])
        nmUtil.align_lras(snap_align=True,  sel=[self.essLeg_2, self.pelvis_locs[2]])
        
        if leg.leg_count == 3:
            index2 = leg.index2
            self.sup_leg_geo = self.leg_list[index2]
            self.supLeg_1 = cmds.duplicate(self.sup_leg_geo, name='supLeg1_output', renameChildren=True)[0]
            nmUtil.align_lras(snap_align=True,  sel=[self.supLeg_1, self.pelvis_locs[3]])
            cmds.parent(self.supLeg_1, self.output_grp)
            
        cmds.parent(self.essLeg_1,self.essLeg_2, self.output_grp)
    def renderArm(self, arm):
        index1 = arm.index1
        index2 = arm.index2
        self.arm1_geo = self.arm_list[index1]
        self.arm2_geo = self.arm_list[index2]
        
        self.arm1 = cmds.duplicate(self.arm1_geo, name='arm1_output', renameChildren=True)[0]
        
        self.arm2 = cmds.duplicate(self.arm2_geo, name='arm2_output', renameChildren=True)[0]
        cmds.setAttr(self.arm2+'.scaleX', -1)
        cmds.makeIdentity(self.arm2, apply=True, t=1,r=1, s=1, n=0, pn=1)
        nmUtil.align_lras(snap_align=True,  sel=[self.arm1, self.torso_locs[1]])
        nmUtil.align_lras(snap_align=True,  sel=[self.arm2, self.torso_locs[2]])
            
        cmds.parent(self.arm1,self.arm2, self.output_grp)
        
        
        
        
        