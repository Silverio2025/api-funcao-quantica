import pennylane as qml
from pennylane import numpy as np

def qubit_pennylane(texto):
    valor = sum(ord(c) for c in texto) % 2

    dev = qml.device("default.qubit", wires=1)

    @qml.qnode(dev)
    def circuito():
        if valor == 0:
            qml.Hadamard(wires=0)
        else:
            qml.PauliX(wires=0)
        return qml.sample(wires=0)

    resultado = circuito()
    return {"quantum": int(resultado[0])}
