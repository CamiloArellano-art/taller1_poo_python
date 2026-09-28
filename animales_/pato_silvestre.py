
from especie_base import EspecieBase

class PatoSilvestre(EspecieBase):
    def __init__(self, alias: str, edad_anios: int, tonalidad: str, puede_volar: bool):
        super().__init__(
            alias=alias,
            edad_anios=edad_anios,
            entorno="Lago / Humedal",
            regimen_alimentario="Omnívoro",
            porte="Pequeño",
            tonalidad=tonalidad
        )
        self.puede_volar = puede_volar

    # Redefinición por Polimorfismo
    def emitir_sonido(self) -> str:
        return f"[Pato {self.alias}] ¡Hace Cuak Cuak!"

    def desplazarse(self) -> str:
        modo = "volando por el cielo" if self.puede_volar else "nadando en el agua"
        return f"[Pato {self.alias}] Se desplaza {modo}."