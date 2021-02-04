#%%
import sys
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt 

def run_luis(testfile):
  thresholds = []
  macro_f1s = []

  y_true = []
  y_pred = []
  score = []
  for line in open(testfile):
    if line.startswith("# "):
      current_intent = line.strip().split(" ")[1]
    if line.startswith("> PASS") or line.startswith("> FAIL"):
      prediction = line.split(" ")[4].strip("(),")
      arr = prediction.split("(")
      # print(current_intent, arr[0], arr[1])
      y_true.append(current_intent)
      y_pred.append(arr[0])
      score.append(float(arr[1]))

  for j in range(101):
    all = 0
    right = 0
    threshold = float(j) / 100
    y_true_new = []
    y_pred_new = []
    for i in range(0, len(y_true)):
      y_true_new.append(y_true[i])
      y_pred_new.append(y_pred[i])
      if y_true_new[i] == 'UNKNOWN' or y_true_new[i] == 'None':
        y_true_new[i] = '_Interruption'
      if y_pred_new[i] == 'UNKNOWN' or y_true_new[i] == 'None' or score[i] < threshold:
        y_pred_new[i] = '_Interruption'
    result = classification_report(y_true_new, y_pred_new, output_dict=True)
    #if j == 20:
    #  print(classification_report(y_true_new, y_pred_new))
    thresholds.append(threshold)
    macro_f1s.append(result["macro avg"]["f1-score"])
  return thresholds, macro_f1s

#report = sys.argv[1]
#th, maf1 = run(report)


#%%
import os
print(os.getcwd())
th, maf1 = run_luis(luis_result)
th, maf1_noint = run_luis(luis_noint_result)
plt.title("threshold-macroF1") 
plt.xlabel("threshold") 
plt.ylabel("macroF1") 
plt.plot(th,maf1,label='int') 
plt.plot(th,maf1_noint, label="noint") 
plt.legend(loc='upper right')
plt.show()
# %%
