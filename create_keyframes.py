import bpy
import math

# set frame end for rendering to frame 450
bpy.data.scenes['Scene'].frame_end = 450

# define variables for later use
camera = bpy.data.objects['Camera']
target = bpy.data.objects['Empty']
predator = bpy.data.objects['Predator']

# change the current frame
bpy.ops.anim.change_frame(frame=24)
# set location of the camera
camera.location.xyz = (280,0,20)
# set rotation of the camera
camera.rotation_euler.x = 270*math.pi/180
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 270*math.pi/180
# insert keyframe for both location as rotation
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

# repeat the process with different values
bpy.ops.anim.change_frame(frame=48)
camera.location.xyz = (250,20,20)
camera.rotation_euler.x = 270*math.pi/180
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 2*math.pi
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=72)
camera.location.xyz = (230,0,20)
camera.rotation_euler.x = 270*math.pi/180
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

target.location.xyz = (250,0,20)
target.keyframe_insert('location')

bpy.ops.anim.change_frame(frame=96)
predator.location.xyz = (400,0,70)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -math.pi/2
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=144)
camera.location.xyz = (230,0,20)
camera.rotation_euler.x = 270*math.pi/180
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

predator.location.xyz = (240,0,18)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -math.pi/2
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=148)
camera.location.xyz = (230,0,28)
camera.rotation_euler.x = math.pi
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=152)
camera.location.xyz = (230,0,19)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

predator.location.xyz = (220,0,17)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -math.pi/2
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=154)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 20*math.pi/180
predator.rotation_euler.z = -60*math.pi/180
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=190)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 20*math.pi/180
predator.rotation_euler.z = -60*math.pi/180
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=200)
predator.location.xyz = (124,-50,15)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -math.pi/2
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (140,-58,18)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = 20*math.pi/180
camera.rotation_euler.z = 430*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=202)
predator.rotation_euler.x = 0
predator.rotation_euler.y = -20*math.pi/180
predator.rotation_euler.z = -120*math.pi/180
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (135,-58,18)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = 20*math.pi/180
camera.rotation_euler.z = 420*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=232)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 20*math.pi/180
predator.rotation_euler.z = -120*math.pi/180
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (50.5,-12,8)
camera.rotation_euler.x = 80*math.pi/180
camera.rotation_euler.y = -20*math.pi/180
camera.rotation_euler.z = 430*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=236)
predator.location.xyz = (28,0,5)
predator.rotation_euler.x = 0
predator.rotation_euler.y = -20*math.pi/180
predator.rotation_euler.z = -120*math.pi/180
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (44,-8,8)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = 20*math.pi/180
camera.rotation_euler.z = 420*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=270)
predator.rotation_euler.x = 0
predator.rotation_euler.y = -20*math.pi/180
predator.rotation_euler.z = -120*math.pi/180
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (-50,46,8)
camera.rotation_euler.x = 85*math.pi/180
camera.rotation_euler.y = 20*math.pi/180
camera.rotation_euler.z = 430*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=272)
predator.location.xyz = (-68,50,5)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -90*math.pi/180
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=274)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 20*math.pi/180
predator.rotation_euler.z = -60*math.pi/180
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=276)
camera.location.xyz = (-62,55,8)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = -20*math.pi/180
camera.rotation_euler.z = 480*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=306)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 20*math.pi/180
predator.rotation_euler.z = -60*math.pi/180
predator.keyframe_insert('rotation_euler')

camera.location.xyz = (-142,8,8)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = -20*math.pi/180
camera.rotation_euler.z = 480*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=308)
predator.location.xyz = (-160,0,5)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -90*math.pi/180
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=312)
camera.location.xyz = (-155,0,8)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = 0
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=332)
target.location.xyz = (-300,0,10)
target.keyframe_insert('location')

camera.location.xyz = (-210,0,8)
camera.rotation_euler.x = math.pi/2
camera.rotation_euler.y = 0
camera.rotation_euler.z = 450*math.pi/180
camera.keyframe_insert('location')
camera.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=344)
predator.location.xyz = (-250,0,5)
predator.rotation_euler.x = 0
predator.rotation_euler.y = 0
predator.rotation_euler.z = -90*math.pi/180
predator.keyframe_insert('location')
predator.keyframe_insert('rotation_euler')

bpy.ops.anim.change_frame(frame=450)
predator.location.xyz = (-480,0,15)
predator.keyframe_insert('location')

target.location.xyz = (500,0,10)
target.keyframe_insert('location')
