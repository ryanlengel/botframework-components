## Train Todo with interruption

for ($i = 0; $i -lt 5; $i++){
    $trainfile = "train" + $i + ".lu"
    $testfile = "test" + $i + ".lu"
    $blu = "train" + $i + ".blu"
    $trainnointfile = "train-noint" + $i + ".lu"
    $report = "report" + $i
    $reportnoint = "report-noint" + $i
    $nointblu = "train-noint" + $i + ".blu"
    python ..\..\..\..\split-data.py ..\..\OriginalLuFile\calendarV2-UpdateEventDialog.lu $trainfile $testfile
    bf orchestrator:create --model ..\..\..\..\models\ --in $trainfile --out model 
    bf orchestrator:test --in .\model\$blu --model ..\..\..\..\models\ --out $report --test $testfile

    python removeInterruption.py $trainfile $trainnointfile
    bf orchestrator:create --model ..\..\..\..\models\ --in $trainnointfile --out model-noint
    bf orchestrator:test --in .\model-noint\$nointblu --model ..\..\..\..\models\ --out $reportnoint --test $testfile
}