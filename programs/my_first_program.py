from nada_dsl import *

def nada_main():
    prayasu = Party(name="Prayasu")  # party 0
    datta = Party(name="Datta")      # party 1

    prayasu_skill = SecretInteger(Input(name="prayasu_skill", party=prayasu))
    datta_skill = SecretInteger(Input(name="datta_skill", party=datta))

    selection_result = (
        (prayasu_skill > datta_skill).if_else(
            "Prayasu is selected!",
            "Datta is selected!"
        )
    )

    out = Output(selection_result, "selection_result", prayasu)

    return [out]
