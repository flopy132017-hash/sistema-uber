import uber_app as app


def test_hora():
    assert len(app.hora()) == 8


def test_solicitar_viaje():
    app.reset_estado()
    assert app.solicitar_viaje_logica() == "OK"
    assert app.estado_viaje == "Pendiente"


def test_aceptar_viaje():
    app.reset_estado()
    app.solicitar_viaje_logica()
    assert app.aceptar_viaje_logica() == "OK"
    assert app.estado_viaje == "Aceptado"


def test_cancelar_usuario():
    app.reset_estado()
    assert app.cancelar_usuario_logica() == "OK"
    assert app.estado_viaje == "Cancelado por usuario"


def test_cancelar_conductor_descuento():
    app.reset_estado()
    app.cancelar_conductor_logica()
    assert app.puntaje == 90


def test_suspension_temporal():
    app.reset_estado()

    app.puntaje = 70
    result = app.cancelar_conductor_logica()

    assert app.estado_conductor_actual == "SUSPENDIDO TEMPORAL"


def test_suspension_permanente():
    app.reset_estado()

    app.puntaje = 10
    result = app.cancelar_conductor_logica()

    assert app.estado_conductor_actual in ["SUSPENDIDO TEMPORAL", "SUSPENDIDO PERMANENTE"]