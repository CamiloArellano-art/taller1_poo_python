from transporte_base import TransporteBase

class FurgonetaComercial(TransporteBase):
    def __init__(self, referencia: str, tono: str, propulsor: str, volumen_carga_m3: float):
        super().__init__(
            referencia=referencia,
            tono=tono,
            propulsor=propulsor,
            accesos=5,
            cupo_personas=2,
            carburante="Gasolina"
        )
        self.volumen_carga_m3 = volumen_carga_m3

    # Polimorfismo
    def regular_velocidad(self) -> str:
        return f"[Furgoneta Urbano] Gestión de marcha optimizada para reparto urbano (Capacidad: {self.volumen_carga_m3} m³)."

    def controlar_climatizacion(self, temperatura: int) -> str:
        return f"Sistema de climatización ajustado a {temperatura}°C en cabina de carga."