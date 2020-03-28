#Imports
from mcpi.minecraft import Minecraft

#Setup
mc = Minecraft.create()

#Code
mc.postToChat("Creating Castle..")
mc.setBlocks(-80,0,-80,80,80,80,0)
mc.setBlocks(-50,-3,-50,50,12,50,49)
mc.setBlocks(-48,-3,-48,48,12,48,10)
mc.setBlocks(-46,-3,-46,46,12,46,49)
mc.setBlocks(-44,-3,-44,44,12,44,10)
mc.setBlocks(-42,-3,-42,42,12,42,49)
mc.setBlocks(-41,-3,-41,41,12,41,0)
mc.setBlocks(-50,-4,-50,50,-4,50,49)
mc.setBlocks(-49,-3,-49,49,-3,49,10)
mc.setBlocks(-41,-2,-41,41,-2,41,89)
mc.setBlocks(-41,-1,-41,41,-1,41,20)
mc.setBlocks(-41,0,-41,41,0,41,0)
mc.setBlocks(0,0,-51,10,3,-41,49)