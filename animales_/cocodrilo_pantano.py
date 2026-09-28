from especie_base import EspecieBase

class CocodriloPantano(EspecieBase):
    def __init__(self, alias: str, edad_anios: int, tonalidad: str, metros_longitud: float):
        super().__init__(
            alias=alias,
            edad_anios=edad_anios,
            entorno="Ríos / Pantanos",
            regimen_alimentario="Carnívoro",
            porte=f"{metros_longitud}m",
            tonalidad=tonalidad
        )
        self.metros_longitud = metros_longitud

    # Redefinición por Polimorfismo
    def emitir_sonido(self) -> str:
        return f"[Cocodrilo {self.alias}] Emite un rugido/soplido subacuático amenazante."

    def desplazarse(self) -> str:
        return f"[Cocodrilo {self.alias}] Se desliza sigilosamente por el agua del pantano."