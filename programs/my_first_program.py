from nada_dsl import *

def nada_main():
    prayasu = Party(name="Prayasu")  # party 0
    datta = Party(name="Datta")      # party 1

    prayasu_skill = SecretInteger(Input(name="prayasu_skill", party=prayasu))
    datta_skill = SecretInteger(Input(name="datta_skill", party=datta))

    selection_result = (
        (prayasu_skill > datta_skill).if_else(
            Integer(0),
            (datta_skill > prayasu_skill).if_else(
                Integer(1),
                Integer(2)
            )
        )
    )

    out = Output(selection_result, "selection_result", prayasu)

    return [out]
