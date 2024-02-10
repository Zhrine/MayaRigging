import pymel.core as pm

def build_right_half_skeleton():
    # Create joints for the right half of the body
    root_joint = pm.createNode('joint', name='root_R')
    spine_joint = pm.createNode('joint', name='spine_R')
    chest_joint = pm.createNode('joint', name='chest_R')
    neck_joint = pm.createNode('joint', name='neck_R')
    head_joint = pm.createNode('joint', name='head_R')
    shoulder_joint = pm.createNode('joint', name='shoulder_R')
    arm_joint = pm.createNode('joint', name='arm_R')
    forearm_joint = pm.createNode('joint', name='forearm_R')
    hand_joint = pm.createNode('joint', name='hand_R')
    hip_joint = pm.createNode('joint', name='hip_R')
    thigh_joint = pm.createNode('joint', name='thigh_R')
    shin_joint = pm.createNode('joint', name='shin_R')
    foot_joint = pm.createNode('joint', name='foot_R')
    toe_joint = pm.createNode('joint', name='toe_R')

    # Parent the joints to create the hierarchy
    pm.parent(spine_joint, root_joint)
    pm.parent(chest_joint, spine_joint)
    pm.parent(neck_joint, chest_joint)
    pm.parent(head_joint, neck_joint)
    pm.parent(shoulder_joint, chest_joint)
    pm.parent(arm_joint, shoulder_joint)
    pm.parent(forearm_joint, arm_joint)
    pm.parent(hand_joint, forearm_joint)
    pm.parent(hip_joint, spine_joint)
    pm.parent(thigh_joint, hip_joint)
    pm.parent(shin_joint, thigh_joint)
    pm.parent(foot_joint, shin_joint)
    pm.parent(toe_joint, foot_joint)

    # Set the joint positions for the default A-pose
    root_joint.setTranslation([0, 0, 0])
    spine_joint.setTranslation([0, 5, 0])
    chest_joint.setTranslation([0, 10, 0])
    neck_joint.setTranslation([0, 15, 0])
    head_joint.setTranslation([0, 18, 0])
    shoulder_joint.setTranslation([2, 10, 0])
    arm_joint.setTranslation([5, 10, 0])
    forearm_joint.setTranslation([9, 10, 0])
    hand_joint.setTranslation([12, 10, 0])
    hip_joint.setTranslation([0, 5, 0])
    thigh_joint.setTranslation([0, 0, 0])
    shin_joint.setTranslation([0, -5, 0])
    foot_joint.setTranslation([0, -10, 0])
    toe_joint.setTranslation([0, -12, 2])

    # Rename the joints with _R at the end
    for joint in pm.ls(type='joint'):
        joint.rename(joint.name() + '_R')

    # Mirror the joints and rename them with _L
    pm.mirrorJoint(root_joint, mirrorYZ=True, mirrorBehavior=True, search='_R', replace='_L')

build_right_half_skeleton()
