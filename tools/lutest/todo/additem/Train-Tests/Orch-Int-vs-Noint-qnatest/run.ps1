## Train Todo with interruption

for ($i = 0; $i -lt 5; $i++){
    $trainfile = "train" + $i + ".lu"
    $testfile = "test" + $i + ".lu"
    $blu = "train" + $i + ".blu"
    $trainnointfile = "train-noint" + $i + ".lu"
    $report = "report" + $i
    $reportnoint = "report-noint" + $i
    $nointblu = "train-noint" + $i + ".blu"
   
    bf orchestrator:test --in ..\Orch-Int-vs-Noint\model\$blu --model ..\..\..\..\models\ --out $report --test $testfile

    bf orchestrator:test --in ..\Orch-Int-vs-Noint\model-noint\$nointblu --model ..\..\..\..\models\ --out $reportnoint --test $testfile
}