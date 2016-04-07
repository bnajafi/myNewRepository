
# create dictionary with different values of k for the brick object
#input dictionary  
glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cement ={"name":"cement", "k": 1.5}
material_list = [glassProp,brickProp,cement]
Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
resultsParallel=compositeWallParallel(parallelSet) 
serieSet= [R1,R2,R6]
sensitivty_results = {}
for material in material_list:
        name= material["name"]
        k = material["k"]
        R4 = {"name":"R4","type":"cond","length":0.16,"area":0.22,"k":k}
        parallelSet = [R3,R4,R5]
        HeatTrasfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,Ti,To)
        sensitivty_results[name] = HeatTrasfer 
        

def materialSensitivity(material_List,serieSet,parallelSet,Ri,Ro)
    # do not forget to write help guidelines here!!
    #for material in material_List
    # you need to import wallHeatTransfer from wallCalculation Script
    for material in material_List:
        print material["name"]
    heatTrasnfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
    #do not forget to write comments in your code   
results   
#out put should be like this: result_sensitivity=  {"glass":253,"brick": 350,... } 
# the ouput can also be a list of dictionaries [{"name":"glass","HeatTransfer" : 253},{"name":"brick","HeatTransfer" : 352}]   