from logica import hora

def test_hora():
    resultado = hora()

    assert isinstance(resultado, str)
    assert len(resultado) == 8