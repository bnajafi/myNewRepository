def materialSensitivity(materialList,serieSet,parallelSet,Rinside,Routside,T_inside,T_outside):
    from wallCalculation import *
    sensitivityResults = {}
    for material in materials:
        conductivity = material["k"]
        name=material["name"]
        R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":conductivity}
        parallelSet = [R3,R4,R5]
    
        heatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
        print results
        sensitivityResults[name] = heatTransfer
    return sensitivityResults
    
    




glassProp = {"name":"glass","k":0.98}
brickProp = {"name":"brick", "k":0.8}
cementProp = {"name":"cement", "k":0.75}

materials = [glassProp,brickProp,cementProp]


Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":materials[0]["k"]}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}
T_inside = 27
T_outside = 10
from wallCalculation import *
parallelSet = [R3,R4,R5]
serieSet= [R1,R2,R6]
sensitivityResults = {}
for material in materials:
    conductivity = material["k"]
    name=material["name"]
    R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":conductivity}
    parallelSet = [R3,R4,R5]
    heatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,T_inside,T_outside)
    print results
    sensitivityResults[name] = heatTransfer
    
results = materialSensitivity(materials,serieSet,parallelSet,Ri,Ro,T_inside,T_outside)

    