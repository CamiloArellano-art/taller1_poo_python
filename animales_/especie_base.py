class EspecieBase:
    def __init__(self, alias: str, edad_anios: int, entorno: str, regimen_alimentario: str, porte: str, tonalidad: str):

        self.alias = alias
        self.edad_anios = edad_anios
        self.entorno = entorno
        self.regimen_alimentario = regimen_alimentario
        self.porte = porte
        self.tonalidad = tonalidad
        
        self._nivel_vital = 100
        self._en_reposo = False

    # Métodos de acceso (Getters)
    def consultar_energia(self) -> int:
        return self._nivel_vital

    def verificar_reposo(self) -> bool:
        return self._en_reposo

    def desplazarse(self) -> str:
        if self._en_reposo:
            return f"{self.alias} se encuentra dormido y no puede avanzar."
        self._nivel_vital = max(0, self._nivel_vital - 10)
        return f"{self.alias} se está moviendo en su hábitat ({self.entorno})."

    def emitir_sonido(self) -> str:
        return f"{self.alias} emite un sonido o señal para comunicarse."

    def ingerir_alimento(self) -> str:
        self._nivel_vital = min(100, self._nivel_vital + 20)
        return f"{self.alias} se alimenta de su comida habitual (Dieta: {self.regimen_alimentario})."

    def reposar(self) -> str:
        self._en_reposo = True
        self._nivel_vital = 100
        return f"{self.alias} entra en periodo de descanso/sueño."