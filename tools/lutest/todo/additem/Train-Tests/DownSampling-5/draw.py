#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

#%%
for i in range(0,5):
    plt.title("threshold-macroF1") 
    plt.xlabel("threshold") 
    plt.ylabel("macroF1")     
    for j in [0.1, 0.3, 0.5, 0.7, 0.9, 1]:
        orch_result = ".\\todo\\additem\\Train-Tests\\DownSampling-5\\report" + str(i) + "-" + str(j) + "\\orchestrator_testing_set_scores.txt"
        th, maf1 = run(orch_result)
        plt.plot(th,maf1,label='ds'+str(j)) 
    plt.legend(loc='upper right')
    plt.show()
# %%

