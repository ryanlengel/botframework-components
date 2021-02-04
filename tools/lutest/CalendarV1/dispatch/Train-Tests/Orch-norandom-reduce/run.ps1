## Train Todo with interruption

foreach($i in (1,10,200)){
    # write-host $i
    $trainfile = "train0-" + $i + ".lu"
    $testfile = "test0.lu"
    $blu = "train0-" + $i + ".blu"
    $report = "report" + $i

    bf orchestrator:create --model ..\..\..\..\models\ --in $trainfile --out model 
    bf orchestrator:test --in .\model\$blu --model ..\..\..\..\models\ --out $report --test $testfile
}