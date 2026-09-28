from especie_base import EspecieBase

class CaballoEjemplar(EspecieBase):
    def __init__(self, alias: str, edad_anios: int, tonalidad: str, porte: str, max_velocidad: int):
        super().__init__(
            alias=alias,
            edad_anios=edad_anios,
            entorno="Pradera / Campo",
            regimen_alimentario="Herbívoro",
            porte=porte,
            tonalidad=tonalidad
        )
        self.max_velocidad = max_velocidad

    # Redefinición por Polimorfismo
    def emitir_sonido(self) -> str:
        return f"[Caballo {self.alias}] ¡Relincha fuertemente! (¡Iiii-hh-hh-hh!)"

    def desplazarse(self) -> str:
        base = super().desplazarse()
        return f"[Caballo] {base} Está galopando a {self.max_velocidad} km/h."