#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

#%%
orch_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report0\\orchestrator_testing_set_scores.txt"
orch_noint_result = ".\\todo\\additem\\Train-Tests\\Orch-Int-vs-Noint\\report-noint0\\orchestrator_testing_set_scores.txt"

#%%
for i in range(0,5):
    plt.title("threshold-macroF1") 
    plt.xlabel("threshold") 
    plt.ylabel("macroF1")     
    for k in range(1,10,2):
        j = k / 10
        orch_result = ".\\todo\\additem\\Train-Tests\\DownSampling\\report" + str(i) + "-" + str(j) + "\\orchestrator_testing_set_scores.txt"
        th, maf1 = run(orch_result)
        plt.plot(th,maf1,label='ds'+str(j)) 
    plt.legend(loc='upper right')
    plt.show()
# %%
