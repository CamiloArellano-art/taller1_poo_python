from transporte_base import TransporteBase

class CamionPesado(TransporteBase):
    def __init__(self, referencia: str, tono: str, propulsor: str, limite_toneladas: float):
        super().__init__(
            referencia=referencia,
            tono=tono,
            propulsor=propulsor,
            accesos=2,
            cupo_personas=3,
            carburante="Diésel"
        )
        self.limite_toneladas = limite_toneladas

    # Polimorfismo
    def encender_sistema(self) -> str:
        inicio = super().encender_sistema()
        return f"[Camión Pesado] {inicio} Presión del circuito de frenos neumático verificada."

    def activar_seguridad(self) -> str:
        return f"Freno de ahogo y sensores de estabilidad habilitados para {self.limite_toneladas} Toneladas."