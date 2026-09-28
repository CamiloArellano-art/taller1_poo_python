from especie_base import EspecieBase

class EscarabajoSilvestre(EspecieBase):
    def __init__(self, alias: str, edad_meses: int, tonalidad: str, posee_cuerno: bool):
        super().__init__(
            alias=alias,
            edad_anios=edad_meses,
            entorno="Bosque / Tierra",
            regimen_alimentario="Herbívoro/Descomponedor",
            porte="Muy Pequeño",
            tonalidad=tonalidad
        )
        self.posee_cuerno = posee_cuerno

    # Redefinición por Polimorfismo
    def emitir_sonido(self) -> str:
        return f"[Escarabajo {self.alias}] Frota sus patas/alas para generar estridulación (sonido casi imperceptible)."

    def desplazarse(self) -> str:
        detalle = "con su cuerno frontal" if self.posee_cuerno else ""
        return f"[Escarabajo {self.alias}] Trepa sobre la corteza de los árboles {detalle}."