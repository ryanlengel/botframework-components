## Train Todo using luis

# copy data from Orch
# python reduce-test.py test0.lu test-reduce.lu
# staging for rate1
# bf luis:test -i .\test-reduce.lu -o test-result-1.lu -a d63c9b48-f93a-4c8a-bf72-1e0f29a6f35f -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly --staging
# production for rate10
# bf luis:test -i .\test-reduce.lu -o test-result-10.lu -a d63c9b48-f93a-4c8a-bf72-1e0f29a6f35f -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly
# production for rate200
bf luis:test -i .\test-reduce.lu -o test-result-200.lu -a d63c9b48-f93a-4c8a-bf72-1e0f29a6f35f -s 6f2b3bd33efd43169b6e653574c5d493  --allowIntentsCount=2 --intentOnly