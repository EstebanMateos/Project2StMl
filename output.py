import json
from math import inf
import matplotlib.gridspec as gridspec

with open(f"output/results_MC_method_Constant.json", "r") as f:
    MC_method_Constant = json.load(f) 

with open(f"output/results_MC_method_Linear.json", "r") as f:
    MC_method_Linear = json.load(f) 

with open(f"output/results_MC_method_Exponentially.json", "r") as f:
    MC_method_Exponentially = json.load(f) 

with open(f"output/results_QL_sum_method_Constant.json", "r") as f:
    QL_Sum_method_Constant = json.load(f) 

with open(f"output/results_QL_sum_method_Linear.json", "r") as f:
    QL_Sum_method_Linear = json.load(f) 

with open(f"output/results_QL_sum_method_Exponentially.json", "r") as f:
    QL_Sum_method_Exponentially = json.load(f) 

with open(f"output/results_QL_ext_method_Constant.json", "r") as f:
    QL_Ext_method_Constant = json.load(f) 

with open(f"output/results_QL_ext_method_Linear.json", "r") as f:
    QL_Ext_method_Linear = json.load(f) 

with open(f"output/results_QL_ext_method_Exponentially.json", "r") as f:
    QL_Ext_method_Exponentially = json.load(f) 

import matplotlib.pyplot as plt

fig = plt.figure() 
plt.title("Evolution of the rewards over episodes depending on the exploration rate method")
# create figure window

gs = gridspec.GridSpec(3, 3, hspace=0.7)
# Creates grid 'gs' of a rows and b columns 
ax = plt.subplot(gs[0, 0])
plt.plot(range(len(MC_method_Constant[str(8)])),MC_method_Constant[str(8)])
plt.title("MC Constant")
ax = plt.subplot(gs[0, 1])
plt.plot(range(len(MC_method_Linear[str(8)])),MC_method_Linear[str(8)])
plt.title("MC Linear")
ax = plt.subplot(gs[0, 2])
plt.plot(range(len(MC_method_Exponentially[str(8)])),MC_method_Exponentially[str(8)])
plt.title("MC Exponential")

ax = plt.subplot(gs[1, 0])
plt.plot(range(len(QL_Sum_method_Constant[str(8)])),QL_Sum_method_Constant[str(8)])
plt.title("QL_Sum Constant")
ax = plt.subplot(gs[1, 1])
plt.plot(range(len(QL_Sum_method_Linear[str(8)])),QL_Sum_method_Linear[str(8)])
plt.title("QL_Sum Linear")
ax = plt.subplot(gs[1, 2])
plt.plot(range(len(QL_Sum_method_Exponentially[str(8)])),QL_Sum_method_Exponentially[str(8)])
plt.title("QL_Sum Exponential")

ax = plt.subplot(gs[2, 0])
plt.plot(range(len(QL_Ext_method_Constant[str(8)])),QL_Ext_method_Constant[str(8)])
plt.title("QL_Ext Constant")
ax = plt.subplot(gs[2, 1])
plt.plot(range(len(QL_Ext_method_Linear[str(8)])),QL_Ext_method_Linear[str(8)])
plt.title("QL_Ext Linear")
ax = plt.subplot(gs[2, 2])
plt.plot(range(len(QL_Ext_method_Exponentially[str(8)])),QL_Ext_method_Exponentially[str(8)])
plt.title("QL_Ext Exponential")


fig.add_subplot(ax) #add 'ax' to figure
plt.show()

fig = plt.figure() 
plt.title("Evolution of the rewards over episodes depending on the exploration rate method")
# create figure window

gs = gridspec.GridSpec(1,5, wspace=0.8)
# Creates grid 'gs' of a rows and b columns 
ax = plt.subplot(gs[0, 0])
plt.plot(range(len(MC_method_Linear[str(1)])),MC_method_Linear[str(1)])
plt.title("Deck 1 : MC Linear")

ax = plt.subplot(gs[0, 1])
plt.plot(range(len(MC_method_Linear[str(2)])),MC_method_Linear[str(2)])
plt.title("Deck 2 : MC Linear")

ax = plt.subplot(gs[0, 2])
plt.plot(range(len(MC_method_Linear[str(6)])),MC_method_Linear[str(6)])
plt.title("Deck 6 : MC Linear")

ax = plt.subplot(gs[0, 3])
plt.plot(range(len(MC_method_Linear[str(8)])),MC_method_Linear[str(8)])
plt.title("Deck 8 : MC Linear")

ax = plt.subplot(gs[0, 4])
plt.plot(range(len(MC_method_Linear[str(inf)])),MC_method_Linear[str(inf)])
plt.title("Deck inf : MC Linear")

fig.add_subplot(ax) #add 'ax' to figure
plt.show()
