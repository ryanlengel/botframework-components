## Train Todo with interruption

for ($i = 0; $i -lt 5; $i++){
    foreach ($j in (1,2,5,10,20,50,100,200)){
        write-host $j
        $trainfile = "train" + $i + ".lu"
        $newtrainfile = "train" + $i + "-" + $j + ".lu"
        $testfile = "test" + $i + ".lu"
        $blu = "train" + $i + "-" + $j + ".blu"
        $report = "report" + $i + "-" + $j
        
        # write-host "xhr"
        python downsampling.py ..\Orch\$trainfile $newtrainfile $j
        bf orchestrator:create --model ..\..\..\..\models\ --in $newtrainfile --out model 
        bf orchestrator:test --in .\model\$blu --model ..\..\..\..\models\ --out $report --test ..\Orch\$testfile
    }
}