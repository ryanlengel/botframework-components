## Train Todo using luis

# copy data from Orch
# python reduce-test.py test0.lu test-reduce.lu
# staging for rate1
#bf luis:test -i .\test-reduce.lu -o test-result-1.lu -a c1658f24-6b9e-4626-923f-d54bd40c0936 -s b6481341e45e4d0f98b8ec67570e6bcd  --allowIntentsCount=2 --intentOnly --staging
# production for rate10
bf luis:test -i .\test-reduce.lu -o test-result-10.lu -a 6db74cbc-0856-4e05-826c-a6bb0e6c3d62 -s b6481341e45e4d0f98b8ec67570e6bcd  --allowIntentsCount=2 --intentOnly --staging
# production for rate200
bf luis:test -i .\test-reduce.lu -o test-result-200.lu -a e14bd97d-f033-4ccc-8c74-b7fa6df4c844 -s b6481341e45e4d0f98b8ec67570e6bcd  --allowIntentsCount=2 --intentOnly --staging