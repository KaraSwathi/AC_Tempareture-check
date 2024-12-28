pip install scikit-fuzzy 

import numpy as np
import skfuzzy as fuzz 
from skfuzzy import control as ctrl

tempareture=np.arange(15,40)#list of all inputs
print(tempareture)

temp=ctrl.Antecedent(tempareture,'temp')
print(temp)

ac_tempareture=np.arange(15,25)
print(ac_tempareture)

ac_temp = ctrl.Consequent(ac_tempareture,'ac_temp')
print(ac_temp)

temp.automf(3) #dividing the inputs in sets(3)
temp.view()

ac_temp.automf(3)
ac_temp.view()

rule1=ctrl.Rule(temp['poor'],ac_temp['good'])
rule2=ctrl.Rule(temp['average'],ac_temp['average'])
rule3=ctrl.Rule(temp['good'],ac_temp['poor'])

tempareture_ctrl=ctrl.ControlSystem([rule1,rule2,rule3])
detect_temp=ctrl.ControlSystemSimulation(tempareture_ctrl)

detect_temp.input['temp'] = 22
detect_temp.compute()
detect_temp.output['ac_temp']
ac_temp.view(sim = detect_temp)