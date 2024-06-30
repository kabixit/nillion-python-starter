from nada_dsl import *

def nada_main():
    nillion = Party(name="nillion")
    x = SecretInteger(Input(name="x", party=nillion))
    y = SecretInteger(Input(name="y", party=nillion))
    condition = x > y
    maximum = condition.if_else(x, y)
    return [Output(maximum, "maximum", nillion)]
