#Imports
from mcpi.minecraft import Minecraft

#Setup
mc = Minecraft.create()

#Code
mc.postToChat("Creating Castle..")
mc.setBlocks(-50,0,-50,50,50,50,0)
mc.setBlocks(-50,0,-50,50,12,50,49)
mc.setBlocks(-48,0,-48,48,12,48,10)
mc.setBlocks(-46,0,-46,46,12,46,49)
mc.setBlocks(-44,0,-44,44,12,44,10)
mc.setBlocks(-42,0,-42,42,12,42,49)
mc.setBlocks(-41,0,-41,41,12,41,0)