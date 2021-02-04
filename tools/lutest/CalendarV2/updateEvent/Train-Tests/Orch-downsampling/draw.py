#%%
orch_result = ".\\CalendarV2\\updateEvent\\Train-Tests\\Orch\\report0\\orchestrator_testing_set_scores.txt"
orch_noint_result = ".\\CalendarV2\\updateEvent\\Train-Tests\\Orch\\report-noint0\\orchestrator_testing_set_scores.txt"

#%%
for i in range(0,5):
    index_list = []
    score_list = []
    for j in [1,2,5,10,20,50]:
        plt.title("downsampling-macroF1") 
        plt.xlabel("downsampling rate") 
        plt.ylabel("macroF1") 
        if j == 50:
            index_list.append('original')
        else:
            index_list.append(str(j))
        orch_result = ".\\CalendarV2\\updateEvent\\Train-Tests\\Orch-downsampling\\report" + str(i) + "-" + str(j) + "\\orchestrator_testing_set_scores.txt"
        score_list.append(get_f1(orch_result))
        # print(score_list)
    plt.bar(index_list, score_list) #, color=['tab:blue','tab:orange','tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive'])
    plt.show()
# %%
