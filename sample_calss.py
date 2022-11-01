class Sample:
    val = 'クラス変数'

sample = Sample()
sample2 = Sample()

sample.__class__.val = '上書きしました．'

#sample.val = 'クラス変数2'
print(Sample.val)
print(sample.val)
print(sample2.val)