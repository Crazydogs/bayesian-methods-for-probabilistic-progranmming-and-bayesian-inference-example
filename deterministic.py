import pymc as pm

# 随机变量
random_value = pm.Poisson('random_value', 3)
print 'random_value: ', random_value.value

# 确定型变量
@pm.deterministic
def deterministic_value(par_1=random_value):
    return par_1 + 100
print 'deterministic_value: ', deterministic_value.value

print 'call random_value.random()'
random_value.random()
print 'random_value: ', random_value.value
print 'deterministic_value: ', deterministic_value.value

print 'call random_value.random()'
random_value.random()
print 'random_value: ', random_value.value
print 'deterministic_value: ', deterministic_value.value
