import streamlit as st
import pandas as pd
import random as rd

# Configuración de la página
st.set_page_config(
    page_title = "Distribución Bernoulli",
    layout = "wide"
)

# Título de la aplicación
st.title("Distribución Bernoulli")
st.divider()

# Configuración de columnas
col1, col2 = st.columns([1, 2], gap = "large")

with col1:
    st.subheader("Ingreso de datos")
    
    # Ingreso de datos
    prob_exito = st.number_input("Probabilidad de éxito (p)", min_value = 0.0, max_value = 1.0, step = 0.01)
    prob_fallo = 1 - prob_exito
    dias = st.number_input("Número de ensayos (n)", min_value = 1, step = 1)
    
    # Creación de tabla de probabilidades
    datos = [
        [prob_exito, prob_fallo],
        [prob_fallo, prob_exito],
    ]
    
    tabla1 = pd.DataFrame(datos, columns = ["0", "1"], index = ["p(x)", "P(x)"])
    st.dataframe(tabla1, use_container_width = True)
    
    # Condiciones de éxito y fallo
    st.info(f"""
            Si ri se encuentra dentro de 0 a {prob_exito}, xi = 0
            \nr
            Si ri se encuentra dentro de {prob_exito + 0.01} a 1, xi = 1
    """)

if prob_exito and dias:
    with col2:
        # Simulación de la distribución Bernoulli
        st.subheader("Simulación")
        
        # Creación de la tabla de simulación
        aleatorios = [rd.random() for _ in range(dias)]
        dias = [i for i in range(1, dias + 1)]
        
        xi = []
        
        for i in range(len(dias)):
            if aleatorios[i] <= prob_exito:
                xi.append(0)
            else:
                xi.append(1)
        
        evento = []
        
        for i in range(len(xi)):
            if xi[i] == 0:
                evento.append("Éxito")
            else:
                evento.append("Fallo")
                
        simulacion = pd.DataFrame({
            "Día": dias,
            "ri": aleatorios,
            "xi": xi,
            "Evento": evento
        })
        
        st.dataframe(simulacion, use_container_width = True, hide_index = True)
        
        # Cálculo de probabilidades
        total_fallos = sum(xi)
        total_exitos = len(xi) - total_fallos
        
        prob_fallos = total_fallos / len(xi)
        prob_exitos = total_exitos / len(xi)
        
        datos_finales = [
            [total_exitos, prob_exitos],
            [total_fallos, prob_fallos],
        ]
        
        tablafinal = pd.DataFrame(datos_finales, columns = ["Total", "Probabilidad"], index = ["Éxitos", "Fallos"])
        
        st.dataframe(tablafinal, use_container_width = True)
