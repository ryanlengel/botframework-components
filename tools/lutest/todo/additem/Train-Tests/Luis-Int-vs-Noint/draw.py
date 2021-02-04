#%%
luis_result = ".\\todo\\additem\\Train-Tests\\Luis-Int-vs-Noint\\test-result.lu"
luis_noint_result = ".\\todo\\additem\\Train-Tests\\Luis-Int-vs-Noint\\test-noint-result.lu"

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
# %%
