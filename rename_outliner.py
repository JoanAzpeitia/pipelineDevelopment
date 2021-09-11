#rename script
import maya.cmds as cmds

def renamePanel():
    cmds.window(width=100, height=50)
    cmds.paneLayout(configuration='quad')
    cmds.button(label='renameGeo', command=renameGEO)
    cmds.button(label='renameGroup', command=renameGRP)
    cmds.showWindow()

def renameGEO(arg=None):
    geometryObjects = cmds.ls(geometry=True)
    for item in geometryObjects:
        #b = item.encode('utf-8')
        cmds.rename(item, item + '_geo')

def renameGRP(arg=None):
    selectedObjects = cmds.ls(sl=True)
    for item in selectedObjects:
        cmds.rename(item, item + '_grp')
