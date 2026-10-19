#-- Estaciones de Metro --

import random

def Estaciones(): 
    linea1 = {
        "Propatria": {"estaciones_siguientes": ["Perez Bonalde"], "tiempo": random.randint(5,8)},
        "Perez Bonalde": {"estaciones_siguientes": ["Propatria", "Plaza Sucre"], "tiempo": random.randint(5,8)},
        "Plaza Sucre": {"estaciones_siguientes": ["Perez Bonalde", "Agua Salud"], "tiempo": random.randint(5,8)},
        "Agua Salud": {"estaciones_siguientes": ["Plaza Sucre", "Caño Amarillo"], "tiempo": random.randint(5,8)},
        "Caño Amarillo": {"estaciones_siguientes": ["Agua Salud", "Capitolio"], "tiempo": random.randint(5,7)},
        "Capitolio": {"estaciones_siguientes": ["Caño Amarillo", "La Hoyada", "El Silencio"], "tiempo": random.randint(5,7)},
        "La Hoyada": {"estaciones_siguientes": ["Capitolio", "Parque Carabobo"], "tiempo": random.randint(5,7)},
        "Parque Carabobo": {"estaciones_siguientes": ["La Hoyada", "Bellas Artes"], "tiempo": random.randint(5,7)},
        "Bellas Artes": {"estaciones_siguientes": ["Parque Carabobo", "Colegio de Ingenieros"], "tiempo": random.randint(5,7)},
        "Colegio de Ingenieros": {"estaciones_siguientes": ["Bellas Artes", "Plaza Venezuela"], "tiempo": random.randint(5,7)},
        "Plaza Venezuela": {"estaciones_siguientes": ["Colegio de Ingenieros", "Sabana Grande", "Ciudad Universitaria", "Zona Rental"], "tiempo": random.randint(5,7)},
        "Sabana Grande": {"estaciones_siguientes": ["Plaza Venezuela", "Chacaito"], "tiempo": random.randint(5,7)},
        "Chacaito": {"estaciones_siguientes": ["Sabana Grande", "Chacao"], "tiempo": random.randint(5,7)},
        "Chacao": {"estaciones_siguientes": ["Chacaito", "Altamira"], "tiempo": random.randint(5,7)},
        "Altamira": {"estaciones_siguientes": ["Chacao", "Miranda"], "tiempo": random.randint(5,7)},
        "Miranda": {"estaciones_siguientes": ["Altamira", "Los Dos Caminos"], "tiempo": random.randint(5,7)},
        "Los Dos Caminos": {"estaciones_siguientes": ["Miranda", "Los Cortijos"], "tiempo": random.randint(3,5)},
        "Los Cortijos": {"estaciones_siguientes": ["Los Dos Caminos", "La California"], "tiempo": random.randint(3,5)},
        "La California": {"estaciones_siguientes": ["Los Cortijos", "Petare"], "tiempo": random.randint(5,7)},
        "Petare": {"estaciones_siguientes": ["La California", "Palo Verde"], "tiempo": random.randint(5,7)},
        "Palo Verde": {"estaciones_siguientes": ["Petare"], "tiempo": random.randint(5,7)}
    }

    linea2 = {
        "El Silencio": {"estaciones_siguientes": ["Capitolio", "Capuchinos"], "tiempo": random.randint(5, 8)},
        "Capuchinos": {"estaciones_siguientes": ["El Silencio", "Maternidad", "Teatros"], "tiempo": random.randint(5, 7)},
        "Maternidad": {"estaciones_siguientes": ["Capuchinos", "Artigas"], "tiempo": random.randint(5, 7)},
        "Artigas": {"estaciones_siguientes": ["Maternidad", "La Paz"], "tiempo": random.randint(5, 7)},
        "La Paz": {"estaciones_siguientes": ["Artigas", "La Yaguara"], "tiempo": random.randint(5, 7)},
        "La Yaguara": {"estaciones_siguientes": ["La Paz", "Carapita"], "tiempo": random.randint(5, 7)},
        "Carapita": {"estaciones_siguientes": ["La Yaguara", "Antímano"], "tiempo": random.randint(5, 7)},
        "Antímano": {"estaciones_siguientes": ["Carapita", "Mamera"], "tiempo": random.randint(5, 7)},
        "Mamera": {"estaciones_siguientes": ["Antímano", "Caricuao", "Ruiz Pineda"], "tiempo": random.randint(5, 7)},
        "Caricuao": {"estaciones_siguientes": ["Mamera", "Zoologico"], "tiempo": random.randint(5, 7)},
        "Zoologico": {"estaciones_siguientes": ["Caricuao"], "tiempo": random.randint(5, 7)},
        "Ruiz Pineda": {"estaciones_siguientes": ["Mamera", "Las Adjuntas"], "tiempo": random.randint(5, 7)},
        "Las Adjuntas": {"estaciones_siguientes": ["Ruiz Pineda"], "tiempo": random.randint(5, 8)}
    }

    linea3 = {
        "Plaza Venezuela": {"estaciones_siguientes": ["Colegio de Ingenieros", "Sabana Grande", "Ciudad Universitaria"], "tiempo": random.randint(5, 7)},
        "Ciudad Universitaria": {"estaciones_siguientes": ["Plaza Venezuela", "Los Símbolos"], "tiempo": random.randint(5, 7)},
        "Los Símbolos": {"estaciones_siguientes": ["Ciudad Universitaria", "La Bandera"], "tiempo": random.randint(5, 7)},
        "La Bandera": {"estaciones_siguientes": ["Los Símbolos", "El Valle"], "tiempo": random.randint(5, 7)},
        "El Valle": {"estaciones_siguientes": ["La Bandera", "Coche"], "tiempo": random.randint(5, 7)},
        "Coche": {"estaciones_siguientes": ["El Valle", "Mercado"], "tiempo": random.randint(5, 7)},
        "Mercado": {"estaciones_siguientes": ["Coche", "Rinconada"], "tiempo": random.randint(5, 7)},
        "Rinconada": {"estaciones_siguientes": ["Mercado"], "tiempo": random.randint(5, 8)}
    }

    linea4 = {
        "Zona Rental": {"estaciones_siguientes": ["Plaza Venezuela", "Parque Central"], "tiempo": random.randint(5, 8)},
        "Parque Central": {"estaciones_siguientes": ["Zona Rental", "Nuevo Circo"], "tiempo": random.randint(5, 7)},
        "Nuevo Circo": {"estaciones_siguientes": ["Parque Central", "Teatros"], "tiempo": random.randint(5, 7)},
        "Teatros": {"estaciones_siguientes": ["Nuevo Circo", "Capuchinos"], "tiempo": random.randint(5, 7)},
        "Capuchinos": {"estaciones_siguientes": ["Teatros", "El Silencio", "Maternidad"], "tiempo": random.randint(5, 7)}
    }
    
    return {
        "Linea 1": linea1,
        "Linea 2": linea2,
        "Linea 3": linea3,
        "Linea 4": linea4
    }