#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

def run(filename):
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

  for j in range(21):
    all = 0
    right = 0
    threshold = float(j) / 20
    y_true_new = []
    y_pred_new = []
    for i in range(0, len(y_true)):
      y_true_new.append(y_true[i])
      y_pred_new.append(y_pred[i])
      if y_true_new[i] == 'UNKNOWN':
        y_true_new[i] = '_Interruption'
      if y_pred_new[i] == 'UNKNOWN' or score[i] < threshold:
        y_pred_new[i] = '_Interruption'
    result = classification_report(y_true_new, y_pred_new, output_dict=True)
    #if j == 10:
    #  print(classification_report(y_true_new, y_pred_new))
    thresholds.append(threshold)
    macro_f1s.append(result["macro avg"]["f1-score"])
  return thresholds, macro_f1s

#report = sys.argv[1]
#th, maf1 = run(report)


#%%
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
