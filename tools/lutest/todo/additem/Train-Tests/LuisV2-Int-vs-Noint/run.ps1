## Train Todo using luis

# copy data from Orch
# staging for int
# bf luis:test -i .\test0.lu -o test-result.lu -a e14bd97d-f033-4ccc-8c74-b7fa6df4c844 -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly --staging
# production for noint
bf luis:test -i .\test.lu -o test-noint-result.lu -a 35810e2f-a9c7-4632-b2e6-98ed21352713 -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly
