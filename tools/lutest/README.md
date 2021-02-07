# The LU test module is to test lu models including Orchestrator and Luis


## Prerequisites
* To use orchestrator, you should
    * Install bf cli about orchestrator
    * Get the base model under lutest folder
    * Please refer to https://github.com/microsoft/botframework-sdk/blob/main/Orchestrator/docs/BFOrchestratorUsage.md for details
* To test luis/luisV2
    * Manually import lu file into luis portal. (If test LuisV2, refer to https://github.com/Azure/luis-private-preview/blob/main/how-to-train.md)
    * Use bf cli - bf luis:test to test the luis result. (No difference between luisV1 and luisV2)
* To draw the evaluation result in python
    * I just run the python code in VSCodel
    * Refer to https://code.visualstudio.com/docs/python/jupyter-support-py for interactive python environment.

## The folder structure
* Skill Name (e.g., Todo)
    * Dialog Name (e.g. AddItem)
        * OriginalLuFile - the original lu files of the dialog
        * Train-Tests
            * Each test scenario
                * run.sh  (Main script to get the testing result)
                * trainxxx.lu (lu file to train the model)
                * testxxx.lu (lu file to test the model)
                * reportxxx/ (orchestrator result report)
                * model/ (store orchestrator .blu file)
                * draw.py, setfilename.py (to get report with testing result and draw picture)
                * other .py files, used to process data
* model/, please get base Orchestrator model in this folder, refer to https://github.com/microsoft/botframework-sdk/blob/main/Orchestrator/docs/BFOrchestratorUsage.md
* evaluate.py, run() function in this file is to convert Orchstrator xx_scores.txt to Classifacation report, and we can use the new report to draw picture. **To draw pictures from orchestrator result, please first run this file in interactive python tevironment.**
* evaluate-luis.py, run_luis() function in this file is to convert Luis result.lu to Classifacation report, and we can use the new report to draw picture. **To draw pictures from luis result, please first run this file in interactive python tevironment.**
* other .py files, used to precess data