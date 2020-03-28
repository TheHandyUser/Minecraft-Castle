#Imports
from mcpi.minecraft import Minecraft

#Setup
mc = Minecraft.create()

#Code
mc.postToChat("Creating Castle..")
mc.setBlocks(-45,0,-45,45,45,45,0)
mc.setBlocks(-25,-3,-25,25,12,25,49)
mc.setBlocks(-24,-3,-24,24,12,24,10)
mc.setBlocks(-23,-3,-23,23,12,23,49)
mc.setBlocks(-22,-3,-22,22,12,22,10)
mc.setBlocks(-21,-3,-21,21,12,21,49)
mc.setBlocks(-20,-3,-41,41,12,41,0)
mc.setBlocks(-25,-4,-25,25,-4,25,49)
mc.setBlocks(-24,-3,-24,24,-3,24,10)
mc.setBlocks(-20,-2,-20,20,-2,20,89)
mc.setBlocks(-20,-1,-20,20,-1,20,20)
mc.setBlocks(-20,0,-20,20,0,20,0)
mc.setBlocks(0,0,-26,5,3,-20,49)