#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

#%%
th, maf1 = run_luis(luis_result)
th, maf1_noint = run_luis(luis_noint_result)
plt.title("threshold-macroF1") 
plt.xlabel("threshold") 
plt.ylabel("macroF1") 
plt.plot(th,maf1,label='int') 
plt.plot(th,maf1_noint, label="noint") 
plt.legend(loc='upper right')
plt.show()

#%%
index_list = []
score_list = []
for i in [1, 10, 200]:
    plt.title("downsampling-macroF1") 
    plt.xlabel("sample rate") 
    plt.ylabel("macroF1") 
    index_list.append(str(i))
    luis_result = ".\\CalendarV1\\dispatch\\Train-Tests\\Luis-norandom-reduce\\test-result-" + str(i) + ".lu"
    th, maf1 = run_luis(luis_result)
    print(maf1[0])
    score_list.append(maf1[0])
print(score_list)
plt.bar(index_list, score_list)
plt.show()
# %%
