## Train Todo with interruption

for ($i = 0; $i -lt 5; $i++){
    $trainfile = "train" + $i + ".lu"
    $testfile = "test" + $i + ".lu"
    $blu = "train" + $i + ".blu"
    $report = "report" + $i

    python ..\..\..\..\split-data-norandom.py ..\..\OriginalLuFile\calendarSkillV1.lu $trainfile $testfile
    bf orchestrator:create --model ..\..\..\..\models\ --in $trainfile --out model 
    bf orchestrator:test --in .\model\$blu --model ..\..\..\..\models\ --out $report --test $testfile
}