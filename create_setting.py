# enable add-on "curve sapling (tree)" manually and save user settings
# bpy.ops.wm.addon_enable(module="add_curve_sapling") fails sometimes

import bpy
import math
import random

# remove previous cube or plane
for object in bpy.data.objects:
    if object.name.startswith('Cube') or object.name.startswith('Plane'):
        try:
            bpy.data.scenes['Scene'].objects.unlink(object)
        except:
            pass

# create material
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.2
    mat.alpha = alpha
    mat.ambient = 1
    return mat

# create see-through material
def makeInvisibleMaterial(name):
    mat = bpy.data.materials.new(name)
    mat.use_shadeless = True
    mat.use_transparency = True
    mat.alpha = 0
    mat.use_raytrace = False
    return mat

# link material to object
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
    
# camera
camera = bpy.data.objects['Camera']
camera.location.xyz = (300,0,25)
camera.rotation_euler.x = 3 * math.pi / 2
camera.rotation_euler.y = math.pi
camera.rotation_euler.z = 3 * math.pi / 2
# set clip end to see distant objects too
camera.data.clip_end = 1000

# lamp
lamp = bpy.data.objects['Lamp']
lamp.location.xyz = (0,0,100)
lamp.rotation_euler.x = 0
lamp.rotation_euler.y = 0
lamp.rotation_euler.z = 0
lamp.data.type = 'SUN'
lamp.data.sky.use_sky = True
lamp.data.sky.use_atmosphere = True

# make materials for tree, leaves and birds
brown = makeMaterial('Brown', (0.2,0.05,0), (1,1,1), 1)
green = makeMaterial('Green', (0,1,0), (1,1,1), 1)
yellow = makeMaterial('Yellow', (0.8,0.8,0), (1,1,1), 1)

# add target (empty)
bpy.ops.object.add()
bpy.context.object.location.xyz = (250,0,20)

# add cone (bird)
# I want this in second layer and this results in 20 booleans to specify the second layer as True!
bpy.ops.mesh.primitive_cone_add(rotation=(math.pi/2, 0, math.pi/2), layers=(False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
setMaterial(bpy.data.objects['Cone'], yellow)

# add a plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, -1 / 2.0), rotation=(0, 0, 0))
bpy.ops.transform.resize(value=(500, 500, 10))

# add emitter plane, make invisible
bpy.ops.mesh.primitive_plane_add(location=(250, 0, 20), rotation=(0, 0, 0))
invisibleMat = makeInvisibleMaterial('Invisible')
setMaterial(bpy.data.objects['Plane.001'], invisibleMat)

# particle systems
plane = bpy.data.objects['Plane.001']
bpy.ops.object.particle_system_add()
plane.particle_systems['ParticleSystem'].name = "Birds"
plane.particle_systems['Birds'].settings.count = 100
plane.particle_systems['Birds'].settings.frame_start = 1
plane.particle_systems['Birds'].settings.frame_end = 1
plane.particle_systems['Birds'].settings.lifetime = 99999
plane.particle_systems['Birds'].settings.physics_type = 'BOIDS'
plane.particle_systems['Birds'].settings.particle_size = 0.2
# update scene or it won't work!
bpy.data.scenes['Scene'].update()
# make birds very fast
plane.particle_systems[0].settings.boids.air_speed_max = 100
# create fake context or it won't work
fake_context = bpy.context.copy()
fake_context["particle_system"] = bpy.context.object.particle_systems[0]
# add goal rule
bpy.ops.boid.rule_add(fake_context)
bpy.ops.boid.rule_move_up(fake_context)
plane.particle_systems[0].settings.boids.active_boid_state.active_boid_rule.object = bpy.data.objects['Empty']
# add avoid collision rule to prevent collision with other objects and boids
bpy.ops.boid.rule_add(fake_context, type='AVOID_COLLISION')
bpy.ops.boid.rule_move_up(fake_context)
plane.particle_systems[0].settings.boids.active_boid_state.active_boid_rule.use_avoid = True
plane.particle_systems[0].settings.boids.active_boid_state.active_boid_rule.use_avoid_collision = True

plane.particle_systems[0].settings.render_type = 'OBJECT'
plane.particle_systems[0].settings.dupli_object = bpy.data.objects['Cone']
plane.particle_systems[0].settings.use_rotation_dupli = True

# add a tree
bpy.ops.curve.tree_add(bevel=True, showLeaves=True, handleType='0', shape='4', baseSize=0.25,  leafShape='rect')
bpy.context.scene.objects.active = bpy.data.objects['tree']
bpy.data.objects['tree'].select = True
# set material of tree
setMaterial(bpy.data.objects['tree'], brown)
setMaterial(bpy.data.objects['leaves'], green)

bpy.data.objects['tree'].location.xyz = (0,0,0)

# duplicate tree
for i in range(200):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['tree'].select = True
    bpy.data.objects['leaves'].select = True
    x = random.randint(-250,250)
    y = random.randint(-100,100)
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(x, y, 0)})

# fix position leaves
for object in bpy.data.objects:
    if object.name.startswith('leaves'):
        object.location.xyz = (0,0,0)
