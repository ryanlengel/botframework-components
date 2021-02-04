## Train Todo using luis

# copy data from Orch
# staging for int
bf luis:test -i .\test.lu -o test-result.lu -a 77a213da-925a-4b07-8567-60db0c85f0f9 -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly --staging
# production for noint
bf luis:test -i .\test.lu -o test-noint-result.lu -a 77a213da-925a-4b07-8567-60db0c85f0f9 -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly
