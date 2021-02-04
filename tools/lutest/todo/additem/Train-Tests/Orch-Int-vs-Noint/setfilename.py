#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

#%%
orch_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report0\\orchestrator_testing_set_scores.txt"
orch_noint_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report-noint0\\orchestrator_testing_set_scores.txt"

#%%
for i in range(0,5):
    orch_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report" + str(i) + "\\orchestrator_testing_set_scores.txt"
    orch_noint_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report-noint" + str(i) + "\\orchestrator_testing_set_scores.txt"
    th, maf1 = run(orch_result)
    th, maf1_noint = run(orch_noint_result)
    plt.title("threshold-macroF1") 
    plt.xlabel("threshold") 
    plt.ylabel("macroF1") 
    plt.plot(th,maf1,label='int') 
    plt.plot(th,maf1_noint, label="noint") 
    plt.legend(loc='upper right')
    plt.show()
# %%
