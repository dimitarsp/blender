import bpy
from mathutils import Vector
import math

filename = "c:/users/dimitar.pouchnikov/desktop/1.csv"
file = open(filename, "r")
lines = file.readlines()
file.close()

scene = bpy.context.scene

factor = 1.3    # factor for width vs length
type = 1        # 0 = flat plane, 1 = box with height

spacing = 0     # init spacing. used for iter, so do not change
spaceFac = 4    # factor for spacing
spaceFacSame = 1  # factor for spacing same elements

for index, line in enumerate(lines):
    #remove the \n
    line = line.strip()
    #split the line by the comma
    item = line.split(',')
    name = item[0]
    if not item[1] =="":
        print(float(item[1]))
    """
    noUnits = int(item[2])
    unitArea = float(item[3])
    totalArea = float(item[4])
    ht = float(item[5])
    comments = item[5]

    #create a long side by using a factor multiplied by the square root
    width = round(math.sqrt(unitArea)*factor, 2)
    length = unitArea/width

    #initiate mesh
    mesh_data = bpy.data.meshes.new("plane_mesh_data")

    #if stands in name then create different settings
    if "stands" in name:
        print(name)

    #choose a plane or a box
    if type==0:
        ptA = (0,0,0)
        ptB = (width,0,0)
        ptC = (width,length,0)
        ptD = (0,length,0)
        verts = [ptA, ptB, ptC, ptD]
        mesh_data.from_pydata(verts, [], [(0,1,2,3)])
    else:
        ptA = (0,0,0)
        ptB = (width,0,0)
        ptC = (width,length,0)
        ptD = (0,length,0)
        ptE = (0,0,ht)
        ptF = (width,0,ht)
        ptG = (width,length,ht)
        ptH = (0,length,ht)
        verts = [ptA, ptB, ptC, ptD, ptE, ptF, ptG, ptH]
        faces = [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,6,7,3),(3,7,4,0)]
        mesh_data.from_pydata(verts, [], faces)

    mesh_data.update()

    obj = bpy.data.objects.new(str(index)+" "+str(name), mesh_data)
    scene.objects.link(obj)

    #move objects
    loc = obj.location
    vec = (spacing,0,0)
    obj.location = loc+Vector(vec)

    #create duplicates if noUnits>1
    if noUnits>1:
        for i in range(1,noUnits):
            newObj = obj.copy()
            newObj.data = obj.data
            scene.objects.link(newObj)

            locVert = newObj.location
            vecVert = (0,(length+spaceFacSame)*i,0)
            newObj.location = locVert+Vector(vecVert)

    #declare spacing after to be used for the next loop
    spacing+=width+spaceFac
    """
