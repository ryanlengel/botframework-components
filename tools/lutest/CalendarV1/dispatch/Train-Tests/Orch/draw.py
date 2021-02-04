#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 


#%%
index_list = []
score_list = []
for i in range(0,5):
    plt.title("threshold-macroF1") 
    plt.xlabel("threshold") 
    plt.ylabel("macroF1") 
    index_list.append(i)
    orch_result = ".\\CalendarV1\\dispatch\\Train-Tests\\Orch\\report" + str(i) + "\\orchestrator_testing_set_scores.txt"
    score_list.append(get_f1(orch_result))
    print(score_list)
plt.bar(index_list, score_list)
plt.show()
# %%
