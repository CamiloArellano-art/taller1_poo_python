from transporte_base import TransporteBase

class DeportivoAltaGama(TransporteBase):
    def __init__(self, referencia: str, tono: str, propulsor: str, carburante: str, tiene_capota_retratil: bool):
        super().__init__(
            referencia=referencia,
            tono=tono,
            propulsor=propulsor,
            accesos=2,
            cupo_personas=2,
            carburante=carburante
        )
        self.tiene_capota_retratil = tiene_capota_retratil

    # Polimorfismo
    def encender_sistema(self) -> str:
        inicio = super().encender_sistema()
        return f"[Deportivo] {inicio} ¡Válvulas de escape deportivas abiertas!"

    def abatir_techo(self) -> str:
        if self.tiene_capota_retratil:
            return f"El techo descapotable de {self.referencia} se ha replegado."
        return "Este modelo no cuenta con techo retráctil."