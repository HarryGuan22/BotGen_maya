import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
class BotRenderer(object):
    def __init__(self):
       # self.pelvis_list =  ['pelvis_geo_1', 'pelvis_geo_2','pelvis_geo_3']
       # self.torso_list = ['torso_geo_1', 'torso_geo_2', 'torso_geo_3']
       # self.leg_list = ['leg_geo_1', 'leg_geo_2']
       # self.head_list = ['head_geo_1','head_geo_2','head_geo_3']
       # self.arm_list = ['arm_geo_1','arm_geo_2']
       self.upPelvis_list = cmds.listRelatives('upright_pelvis_GRP', c=True)
       self.quadPelvis_list = cmds.listRelatives('quad_pelvis_GRP', c=True)
       self.insectPelvis_list = cmds.listRelatives('insect_pelvis_GRP', c=True)
       self.leg_list = cmds.listRelatives('leg_GRP', c=True)
    def render(self, info, pos='render_pos'):
        self.pos = cmds.ls(pos)[0]
        self.output_grp = cmds.group(em=True, n='output')
        nmUtil.a_to_b(sel=[self.output_grp, self.pos])
        self.pelvis = []
        self.renderPelvis(info)
        self.renderLeg(info)
        self.renderTorso(info)
        self.renderArm(info)
    
    def renderPelvis(self, info):
        self.pelvis_type = info['Pelvis']
        self.pelvis_geo = cmds.duplicate(self.pelvis_type, name='pelvis_output', renameChildren=True)
        self.pelvis.append(self.pelvis_geo)
        # pelvis_children = cmds.listRelatives(self.pelvis_geo, c=True)
        self.pelvis_locs = [c for c in self.pelvis_geo if cmds.listRelatives(c,shapes=True, type="locator")]
        self.leg_locs = [c for c in self.pelvis_locs if 'leg' in c]
        self.sup_locs = [c for c in self.pelvis_locs if 'sup' in c]
        self.torso_locs = [c for c in self.pelvis_locs if 'torso' in c]
        
        # for i, c in enumerate(self.pelvis_locs):
        #     new_name = 'leg_loc_' + str(i)
        #     cmds.rename(c, new_name)
        
        # self.pelvis_locs = cmds.listRelatives(self.pelvis_geo, c=True, typ='locator')
        nmUtil.a_to_b(sel=[self.pelvis_geo[0], self.pos])
        # cmds.makeIdentity(self.pelvis, apply=True)
        cmds.parent(self.pelvis_geo[0], self.output_grp)
        # self.renderTorso(pelvis.torso_NT)
        # self.renderLeg(pelvis.leg_NT)
    def renderLeg(self, info):
        sup_leg = info['Supporting_leg']
        bot_type = info['Bot_type']
        if bot_type == 'insectile':
            leg_type = 'leg_geo_5'
            for i, c in enumerate(self.leg_locs):
                new_name = 'output_leg_' + str(i)
                self.leg_geo = cmds.duplicate(leg_type, name=new_name, renameChildren=True)[0]
                nmUtil.a_to_b(sel=[self.leg_geo, c])
                cmds.parent(self.leg_geo, self.output_grp)

        else:
            leg_type = info['Kinetic_leg']
            for i, c in enumerate(self.leg_locs):
                new_name = 'output_leg_' + str(i)
                    
                if i % 2 == 0:
                    self.leg_geo = cmds.duplicate(leg_type, name=new_name, renameChildren=True)[0]
                    # nmUtil.align_lras(snap_align=True,  sel=[self.pelvis_geo[0], c])
                    nmUtil.a_to_b(sel=[self.leg_geo, c])
                    cmds.parent(self.leg_geo, self.output_grp)
                else:
                    self.leg_geo = cmds.duplicate(leg_type, name=new_name, renameChildren=True)[0]
                    cmds.setAttr(self.leg_geo + ".scaleX", -1)
                    # nmUtil.align_lras(snap_align=True,  delete_history=False, sel=[self.pelvis_geo[0], c])
                    nmUtil.a_to_b(sel=[self.leg_geo, c])
                    cmds.parent(self.leg_geo, self.output_grp)
                    cmds.makeIdentity(self.leg_geo, apply=True, t=True, r=True, s=True, n=False, pn=True)
            if len(self.sup_locs) != 0 and sup_leg != 'None':
                self.sup_geo = cmds.duplicate(sup_leg, name='sup', renameChildren=True)[0]
                # nmUtil.align_lras(snap_align=True,  sel=[self.pelvis_geo[0], c])
                nmUtil.a_to_b(sel=[self.sup_geo, self.sup_locs[0]])
                cmds.parent(self.sup_geo, self.output_grp)
                
        
        
    def renderTorso(self, info):
        torso_type = info['Torso']
        
        
        self.torso_geo = cmds.duplicate(torso_type, name='torso_output', renameChildren=True)
        nmUtil.a_to_b(sel=[self.torso_geo[0], self.torso_locs[0]])
        cmds.parent(self.torso_geo[0], self.output_grp)
        
        
        self.torso_slot_locs = [c for c in self.torso_geo if cmds.listRelatives(c,shapes=True, type="locator")]
        self.arm_locs = [c for c in self.torso_slot_locs if 'arm' in c]
        
        
        # self.torso_children = cmds.listRelatives(self.torso, children=True)
        # for i, c in enumerate(self.torso_children):
        #     if cmds.objectType(c) != 'shape':
        #         new_name = self.torso + '_loc_' + str(i)
        #         cmds.rename(c, new_name)
        # self.torso_locs = cmds.listRelatives(self.torso, children=True)
        # nmUtil.a_to_b(sel=[self.torso, self.pelvis_locs[-1]])
        # nmUtil.align_lras(snap_align=True, delete_history=True, sel=[self.torso, self.pelvis_locs[-1]])
    def renderArm(self, info):
        arm_type = info['Arm']
            
        for i, c in enumerate(self.arm_locs):
                new_name = 'output_arm_' + str(i)
                    
                if i % 2 == 0:
                    self.arm_geo = cmds.duplicate(arm_type, name=new_name, renameChildren=True)[0]
                    # nmUtil.align_lras(snap_align=True,  sel=[self.pelvis_geo[0], c])
                    nmUtil.a_to_b(sel=[self.arm_geo, c])
                    cmds.parent(self.arm_geo, self.output_grp)
                else:
                    self.arm_geo = cmds.duplicate(arm_type, name=new_name, renameChildren=True)[0]
                    cmds.setAttr(self.arm_geo + ".scaleX", -1)
                    # nmUtil.align_lras(snap_align=True,  delete_history=False, sel=[self.pelvis_geo[0], c])
                    nmUtil.a_to_b(sel=[self.arm_geo, c])
                    cmds.parent(self.arm_geo, self.output_grp)
                    
        
    def renderHead(self, head):
        index = head.index
        self.head_geo = self.head_list[index]
        self.head = cmds.duplicate(self.head_geo, name='head_output', renameChildren=True)[0]
        
        nmUtil.align_lras(snap_align=True, delete_history=True, sel=[self.head, self.torso_locs[-1]])
        cmds.parent(self.head, self.output_grp)
    
    
        
        
        
        
        