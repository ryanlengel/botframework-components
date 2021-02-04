#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 


#%%
index_list = []
score_list = []
for i in [1, 10, 200]:
    plt.title("downsampling-macroF1") 
    plt.xlabel("sample rate") 
    plt.ylabel("macroF1") 
    index_list.append(str(i))
    orch_result = ".\\CalendarV1\\dispatch\\Train-Tests\\Orch-norandom-reduce\\report" + str(i) + "\\orchestrator_testing_set_scores.txt"
    score_list.append(get_f1(orch_result))
print(score_list)
plt.bar(index_list, score_list)
plt.show()
# %%
