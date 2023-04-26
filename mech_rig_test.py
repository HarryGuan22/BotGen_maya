#rigging Test
import maya.cmds as cmds
import nmrig.shelfUtils as nmUtil
import maya.api.OpenMaya as OpenMaya

output_list = ['output','output1', 'output2']
dict_list = [bot1_info,bot2_info,bot3_info]


class MechAutoRigger(object):
    def __init__(self):
        self.rig_list = []
    
    @classmethod
    def generate_joints(cls, output=['output','output1', 'output2'], dict_list=[bot1_info,bot2_info,bot3_info]):
        for output_grp in output:
            children = cmds.listRelatives(output_grp, children=True)
            
            leg_list = [leg for leg in children if 'leg' in leg]
            sup_list = [sup for sup in children if 'sup' in sup]
            descendants = cmds.listRelatives(leg_list, allDescendents=True, type="transform")
            leg_locs = [c for c in descendants if cmds.listRelatives(c,shapes=True, type="locator")]
            
            
            pelvis_ls = [mesh for mesh in children if 'pelvis' in mesh]
            pelvis = pelvis_ls[0]
            pelvis_jnt = cmds.joint(n='{}_pelvis'.format(output_grp))
            pelvis_ctrl = cmds.circle(nr=[0, 1, 0], c=[0, 0, 0], r=3.5)[0]
            nmUtil.a_to_b(sel=[pelvis_jnt,pelvis])
            nmUtil.align_lras(snap_align=True, sel=[pelvis_ctrl,pelvis_jnt])
            
            master_ctrl = cmds.circle(n='master_ctrl',normal=(0,1,0),r=7)[0]
            nmUtil.align_lras(snap_align=True, sel=[master_ctrl,pelvis_jnt])
            set_curve_override_color(master_ctrl,17)
            cmds.move(0,-3.5, 0, master_ctrl,r=True)
            
            if not sup_list:
                print('it does not have a sup leg')
            else:
                print('it has a sup leg')
                sup_des = cmds.listRelatives(sup_list, allDescendents=True, type="transform")
                sup_locs = [c for c in sup_des if cmds.listRelatives(c,shapes=True, type="locator")]
                sup_chain = create_chain(joint_loc_list = sup_locs)
                setup_sup(sup_chain, master_ctrl)
                cmds.parent(sup_chain[0], pelvis_jnt)
                sup_children = cmds.listRelatives(sup_list[0], children=True, type='transform')
                sup_meshes = [m for m in sup_children if cmds.listRelatives(m,shapes=True, type="mesh")]
                sup_chain.pop(-1)
                for joint, mesh in zip(sup_chain, sup_meshes):
                    cmds.parent(mesh, joint)
                
            
            
        
            parent_constraint = cmds.parentConstraint(pelvis_ctrl, pelvis_jnt)
            set_curve_override_color(pelvis_ctrl,17)
            parent_object = cmds.listRelatives(pelvis_jnt, parent=True)

            # Check if the pelvis jnt has a parent
            if parent_object is not None:
                cmds.parent(pelvis_jnt,w=True)
            else:
                print("ok")
            
            n = len(leg_list)
            sublistLength = int(len(leg_locs) / n)
            
            sublists = [leg_locs[i:i+sublistLength] for i in range(0, len(leg_locs), sublistLength)]
            for i, loc_list in enumerate(sublists):
                
                joint_chain = []
                joint_chain = create_chain(joint_loc_list = loc_list)
                # cmds.joint(joint_chain[0], edit=True, zso=True, oj="xyz", sao="xup", ch=True)
                cmds.jointDisplayScale(0.5)
                t_ctrl = setup_leg(leg_chain = joint_chain, master = master_ctrl)
                cmds.parent(joint_chain[0], pelvis_jnt)
                if 'leg5' in joint_chain[0]:
                    leg_children = cmds.listRelatives(leg_list[i], children=True, type='transform')
                    leg_meshes = [m for m in leg_children if cmds.listRelatives(m,shapes=True, type="mesh")]
                    joint_chain.pop(-1)
                    for joint, mesh in zip(joint_chain, leg_meshes):
                        cmds.parent(mesh, joint)
                elif 'leg4' or 'leg3' or 'leg1' or 'leg2' in leg_chain[0]:
                    leg_children = cmds.listRelatives(leg_list[i], children=True, type='transform')
                    leg_meshes = [m for m in leg_children if cmds.listRelatives(m,shapes=True, type="mesh")]
                    
                    if 'leg4' or 'leg3' in leg_chain[0]:
                        joint_chain.pop(-1)
                        print('trim off toe')
                        
                    for joint, mesh in zip(joint_chain, leg_meshes):
                        cmds.parent(mesh, joint)
            
            cmds.parent(output_grp, pelvis_ctrl)
            cmds.parent(pelvis_ctrl,master_ctrl)
            cmds.parent(pelvis_jnt,master_ctrl)
            
        
            
            
    def create_chain(joint_loc_list):
        chain = []
        for j in joint_loc_list:
            if j == joint_loc_list[0]:
                par = None
            else:
                par = jnt
            jnt = cmds.joint(par, n='{}_JNT'.format(j))
            nmUtil.a_to_b(sel=[jnt,j], freeze=True)
            chain.append(jnt)
        # cmds.hide(joint_list)
        return chain
    def set_curve_override_color(curve_name, color_index):
        """
        Sets the override color of the specified curve to the specified color index.
        """
        curve_shape = cmds.listRelatives(curve_name, shapes=True)[0]
        cmds.setAttr(curve_shape + ".overrideEnabled", True)
        cmds.setAttr(curve_shape + ".overrideColor", color_index)    

    def setup_sup(sup_chain, master):
        if 'sup1' in sup_chain[0]:
            cmds.parent(sup_chain[1], w=True)
            sup_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(sup_chain[1]), startJoint=sup_chain[1], endEffector=sup_chain[3], solver="ikRPsolver")[0]
            sup_ctrl = cmds.circle(n='{}_ctrl'.format(sup_chain[-1]),normal=(0,1,0))[0]
            nmUtil.align_lras(snap_align=True, sel=[sup_ctrl,sup_chain[-1]])
            aim_constraint = cmds.aimConstraint(sup_ctrl, sup_chain[0], mo=True,aim=[0, 0, 1], u=[0, 1, 0], wut="scene", sk=["x","z"])
            cmds.parent(sup_ik_handle,sup_ctrl)
            cmds.parent(sup_chain[1],sup_chain[0])
            cmds.parent(sup_ctrl,master)
    def setup_leg(leg_chain, master):
        if 'leg5' in leg_chain[0]:
            print('leg5 is here')
            
            shoulder = leg_chain[0]
            
            upper = leg_chain[1]
            knee = leg_chain[2]
            shin = leg_chain[3]
           
            
            PV_loc= pole_vec_shin(upper=upper,shin=shin)
            PV = cmds.spaceLocator()[0]
            cmds.move(PV_loc.x, PV_loc.y, PV_loc.z, PV, worldSpace=True)
            # get the world-space translation of joint A
            
            cmds.parent(leg_chain[1], w=True)
            upper_arm_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(shoulder), startJoint=leg_chain[1], endEffector=leg_chain[3], solver="ikRPsolver")[0]
            lower_arm_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(leg_chain[3]), startJoint=leg_chain[3], endEffector=leg_chain[4], solver="ikRPsolver")[0]
            ctrl = cmds.circle(n='{}_ctrl'.format(leg_chain[4]),normal=(0,1,0))[0]
            # nmUtil.align_lras(snap_align=True, sel=[ctrl,leg_chain[4]])
            nmUtil.a_to_b(is_trans=True, is_rot=False, sel=[ctrl,leg_chain[4]])
            aim_constraint = cmds.aimConstraint(ctrl, shoulder, mo=True,aim=[1, 0, 0], u=[0, 0, 1], wut="scene", sk=["x","z"])
            pole_vector_constraint = cmds.poleVectorConstraint(PV, lower_arm_ik_handle)

            cmds.parent(upper_arm_ik_handle,lower_arm_ik_handle,ctrl)
            cmds.parent(PV,knee)
            cmds.parent(upper,shoulder)
            cmds.parent(ctrl,master)
        elif 'leg1' in leg_chain[0]:
                print('a humanoid leg is here')
                
                
                thigh = leg_chain[0]
                knee = leg_chain[1]
                ankle = leg_chain[2]
                toe = leg_chain[3]
                upper_leg_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(leg_chain[1]), startJoint=leg_chain[1], endEffector=leg_chain[3], solver="ikRPsolver")[0]
                # lower_leg_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(leg_chain[3]), startJoint=leg_chain[3], endEffector=leg_chain[4], solver="ikRPsolver")[0]
                ctrl = cmds.circle(n='{}_ctrl'.format(leg_chain[3]),normal=(0,1,0))[0]
                nmUtil.align_lras(snap_align=True, sel=[ctrl,leg_chain[-1]])
                cmds.parent(upper_leg_ik_handle,ctrl)
                cmds.parent(ctrl,master)
                
        elif 'leg2' in leg_chain[0]:
                print('a reverse leg is here')
                
            
                reverse_leg_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(leg_chain[1]), startJoint=leg_chain[0], endEffector=leg_chain[-1], solver="ikRPsolver")[0]
                
                ctrl = cmds.circle(n='{}_ctrl'.format(leg_chain[-1]),normal=(0,1,0))[0]
                nmUtil.align_lras(snap_align=True, sel=[ctrl,leg_chain[-1]])
                cmds.parent(reverse_leg_ik_handle,ctrl)
                
                cmds.parent(ctrl,master)
                
        elif 'leg4' or 'leg3' in leg_chain[0]:
                print('a boston dynamic type leg is here')
                shoulder = leg_chain[0]
            
                upper = leg_chain[1]
                knee = leg_chain[2]
                lower = leg_chain[3]
                leg_ik_handle = cmds.ikHandle(name="{}_ik_handle".format(shoulder), startJoint=leg_chain[1], endEffector=leg_chain[3], solver="ikRPsolver")[0]
                ctrl = cmds.circle(n='{}_ctrl'.format(leg_chain[3]),normal=(0,1,0))[0]
                nmUtil.align_lras(snap_align=True, sel=[ctrl,leg_chain[3]])
                cmds.parent(leg_ik_handle,ctrl)
                cmds.parent(ctrl,master)
        

    def pole_vec_shin(upper,shin):
        # get the world-space translation of joint A
        joint_a_translation = cmds.xform(upper, query=True, translation=True, worldSpace=True)

        # get the world-space translation of joint B
        joint_b_translation = cmds.xform(shin, query=True, translation=True, worldSpace=True)
            
        joint_a_vector = OpenMaya.MVector(joint_a_translation[0], joint_a_translation[1], joint_a_translation[2])
        joint_b_vector = OpenMaya.MVector(joint_b_translation[0], joint_b_translation[1], joint_b_translation[2])
            
        difference_vector = joint_b_vector - joint_a_vector
        pole_vec_loc = difference_vector/2 + joint_b_vector
        return pole_vec_loc
# objectName = "output_leg_7"

# # Get all the descendants of the object using the "listRelatives" command
# descendants = cmds.listRelatives(objectName, allDescendents=True, type="transform")
# locs = [c for c in descendants if cmds.listRelatives(c,shapes=True, type="locator")]
if __name__ == '__main__':
    # joints = cmds.ls(type='joint')
    # cmds.delete(joints)
    MechAutoRigger.generate_joints()
    # children = cmds.listRelatives('output', children=True)
    # leg_list = [leg for leg in children if 'leg' in leg]
    # leg_children = cmds.listRelatives(leg_list[0], children=True, type='transform')
    # leg_meshes = [m for m in leg_children if cmds.listRelatives(m,shapes=True, type="mesh")]
    # Create a motionPath node and attach the controller to the curve
    