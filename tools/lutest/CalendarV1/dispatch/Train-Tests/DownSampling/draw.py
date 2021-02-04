#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 


#%%
for i in range(0,5):
    index_list = []
    score_list = []
    for j in [1,2,5,10,20,50,100,200]:
        plt.title("downsampling-macroF1") 
        plt.xlabel("downsampling rate") 
        plt.ylabel("macroF1") 
        if j == 200:
            index_list.append('origin')
        else:
            index_list.append(str(j))
        orch_result = ".\\CalendarV1\\dispatch\\Train-Tests\\Downsampling\\report" + str(i) + "-" + str(j) + "\\orchestrator_testing_set_scores.txt"
        score_list.append(get_f1(orch_result))
        # print(score_list)
    plt.bar(index_list, score_list) #, color=['tab:blue','tab:orange','tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive'])
    plt.show()
# %%
print(index_list)
print("\t".join([str(x) for x in score_list]))
# %%
