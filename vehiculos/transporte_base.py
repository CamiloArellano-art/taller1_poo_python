class TransporteBase:
    def __init__(self, referencia: str, tono: str, propulsor: str, accesos: int, cupo_personas: int, carburante: str):

        self.referencia = referencia
        self.tono = tono
        self.propulsor = propulsor
        self.accesos = accesos
        self.cupo_personas = cupo_personas
        self.carburante = carburante
        
        self._operativo = False
        self._ritmo_kmh = 0

    def marcha_activa(self) -> bool:
        return self._operativo

    def leer_velocidad(self) -> int:
        return self._ritmo_kmh

    def encender_sistema(self) -> str:
        if not self._operativo:
            self._operativo = True
            return f"El transporte {self.referencia} ha iniciado su motor ({self.propulsor})."
        return "El sistema ya está activo."

    def apagar_sistema(self) -> str:
        if self._operativo:
            self._operativo = False
            self._ritmo_kmh = 0
            return f"El transporte {self.referencia} fue desactivado."
        return "El sistema ya está fuera de línea."

    def regular_velocidad(self) -> str:
        if not self._operativo:
            return "Imposible alterar la marcha con el motor apagado."
        return f"Aceleración y frenado controlados. Velocidad actual: {self._ritmo_kmh} km/h."