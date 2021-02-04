#%%
for i in range(0,5):
    orch_result = ".\\CalendarV2\\updateEvent\\Train-Tests\\Orch-qna\\report" + str(i) + "\\orchestrator_testing_set_scores.txt"
    orch_noint_result = ".\\CalendarV2\\updateEvent\\Train-Tests\\Orch-qna\\report-noint" + str(i) + "\\orchestrator_testing_set_scores.txt"
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
