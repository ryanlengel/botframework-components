## Train Todo with interruption

for ($i = 0; $i -lt 5; $i++){
    #for ($j = 0.1; $j -lt 1; $j+=0.2)
    $j = 1
    #{
        $trainfile = "train" + $i + ".lu"
        $newtrainfile = "train" + $i + "-" + $j + ".lu"
        $testfile = "test" + $i + ".lu"
        $blu = "train" + $i + "-" + $j + ".blu"
        $trainnointfile = "train-noint" + $i + "-" + $j + ".lu"
        $report = "report" + $i + "-" + $j
        $reportnoint = "report-noint" + $i + "-" + $j
        $nointblu = "train-noint" + $i + "-" + $j + ".blu"
        python ..\..\..\..\downsampling-5.py ..\Orch-Int-vs-Noint\$trainfile $newtrainfile $j
        bf orchestrator:create --model ..\..\..\..\models\ --in $newtrainfile --out model 
        bf orchestrator:test --in .\model\$blu --model ..\..\..\..\models\ --out $report --test ..\Orch-Int-vs-Noint\$testfile    
    #}
}