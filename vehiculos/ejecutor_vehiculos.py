# Archivo: ejecutor_vehiculos.py

from deportivo_alta_gama import DeportivoAltaGama
from furgoneta_comercial import FurgonetaComercial
from camion_pesado import CamionPesado

def iniciar_demo():
    print("=== DEMOSTRACIÓN DE POO EN VEHÍCULOS ===")

    auto_sport = DeportivoAltaGama(referencia="BMW Z4", tono="Negro", propulsor="3.0L Turbo", carburante="Extra", tiene_capota_retratil=True)
    van_reparto = FurgonetaComercial(referencia="Carry Van", tono="Blanco", propulsor="1.3L", volumen_carga_m3=4.5)
    camion_volquete = CamionPesado(referencia="Chevrolet FTR", tono="Blanco", propulsor="5.2L Turbo Diésel", limite_toneladas=12.0)

    arranque_sport = auto_sport.encender_sistema()
    techo_sport = auto_sport.abatir_techo()

    arranque_van = van_reparto.encender_sistema()
    marcha_van = van_reparto.regular_velocidad()

    arranque_camion = camion_volquete.encender_sistema()
    frenado_camion = camion_volquete.activar_seguridad()

    print("\n--- RESULTADOS: DEPORTIVO ---")
    print(arranque_sport)
    print(techo_sport)

    print("\n--- RESULTADOS: FURGONETA ---")
    print(arranque_van)
    print(marcha_van)

    print("\n--- RESULTADOS: CAMIÓN ---")
    print(arranque_camion)
    print(frenado_camion)

if __name__ == "__main__":
    iniciar_demo()