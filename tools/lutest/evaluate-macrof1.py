#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

def get_f1(filename):
  thresholds = []
  macro_f1s = []

  y_true = []
  y_pred = []
  score = []
  for line in open(filename):
    arr = line.split("\t")
    y_true.append(arr[1])
    y_pred.append(arr[2])
    score.append(float(arr[3]))

  result = classification_report(y_true, y_pred, output_dict=True)
  return result["macro avg"]["f1-score"]

#report = sys.argv[1]
#th, maf1 = run(report)


#%%
f1 = get_f1(orch_result)
plt.bar([1], [f1])
# plt.title("threshold-macroF1") 
# plt.xlabel("threshold") 
# plt.ylabel("macroF1") 
# plt.plot(th,maf1,label='int') 
# plt.plot(th,maf1_noint, label="noint") 
# plt.legend(loc='upper right')
plt.show()
# %%
