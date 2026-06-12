# 🦎 Time is Time (TiT) — v6.6
(tit.NG66.Ei2C.py)

[![Python v3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/UI-PyQt5-green.svg)](https://pypi.org/project/PyQt5/)
[![Ecosistema](https://img.shields.io/badge/Environment-Xubuntu%20%2F%20XFCE-orange.svg)](https://xubuntu.org/)

> **"El calendario es una danza cósmica entre el tiempo y la eternidad, un reflejo de nuestro intento por ordenar lo infinito. Cada mes encierra sus misterios numéricos en la matriz elemental del universo de las causalidades..."**

---

## 🔬 Diagnóstico de Ingeniería Chamánica

* **Hipótesis Inicial:** Qt renderiza lento, Python es lento, el segundero consume CPU y la transparencia rompe el espacio-tiempo.
* **Diagnóstico Final:** Falta de Geckonismo™.
* **Solución Radical:** `(╯°□°）╯︵ ┻━┻` (Optimización y desacoplamiento mediante hilos secundarios).

**Time is Time (TiT)** es un centro de comando temporal flotante y ultra-ligero diseñado bajo los principios del minimalismo funcional y el orden cósmico del **Team Cangurera**. Desarrollado originalmente para integrarse de forma fluida sobre el escritorio de **Xubuntu (XFCE)**, este widget persistente elimina la contaminación visual y la carga cognitiva ofreciendo un control de tiempo absoluto en una sola interfaz tableteada y traslúcida.

---

## 🚀 Funcionalidades del Ecosistema Temporal

| Solapa / Módulo | Descripción Técnica | Control de Interfaz |
| :--- | :--- | :--- |
| **⏱️ Cronómetro** | Medición de precisión de alta velocidad. Registra el tiempo transcurrido en décimas de segundo nativas. | Iniciar / Pausar / Reiniciar. |
| **⏳ Una Hora Countdown**| Temporizador regresivo configurable de 1 a 60 minutos con bloqueo reactivo de controles durante el despegue. | Alarma sónica nativa vía `paplay` (`alarm-clock-elapsed.oga`). |
| **🚨 Alarma Horaria** | Centinela temporal que monitorea el reloj del sistema físico para disparar alertas en coordenadas exactas. | Conexión desvinculable (`disconnect()`) en caliente. |
| **⌚ Hora Actual** | Núcleo del presente real. Muestra hora, día de la semana abreviado y fecha sincronizada. | Actualización síncrona mediante Hilos de Tiempo independientes. |
| **📅 Mes Calendario** | **[NEW v6.6]** El "Transporte Temporal" del Delorean. Matriz cíclica inteligente acoplada al calendario gregoriano. | Navegación fractal de meses y años con control de desborde matemático. |
| **☕ Donar** | Solapa dedicada a la abundancia universal, el flujo financiero y la conexión cósmica. | Enlace de soporte. |

---

## 🛠️ Arquitectura y Blindaje del Código

* **Desacoplamiento Cuántico del Tiempo (`TimeThread`):** El reloj principal de la aplicación corre fuera del hilo gráfico de la UI utilizando un `QThread` dedicado. Evita los congelamientos de pantalla y empuja los datos a la interfaz con precisión milimétrica cada 1000 ms.
* **Estilo Futurista Transparente:** Aprovecha las propiedades físicas de `Qt.WA_TranslucentBackground` y banderas `Qt.WindowStaysOnTopHint` para mantenerse como un overlay flotante siempre al frente en el plano de trabajo.
* **Inmunidad al Lagueo de Red:** Se eliminaron de raíz los parches de frases motivacionales síncronas que asfixiaban el motor gráfico, reemplazándolos por un centinela estático de estabilidad `(╯°□°）╯︵ ┻━┻`.
* **Respeto absoluto al Presente Real:** La grilla del calendario (estructurada de manera ultra-eficiente combinando matrices de `pandas` y `calendar.monthcalendar`) resalta con un celeste de foco (`#259ae9`) **únicamente** la coordenada espacio-tiempo del presente real donde la máquina vive. Si viajas al pasado o al futuro, la grilla se mantiene limpia y simétrica.

---

## 📦 Dependencias Requeridas

Para desplegar este circo de monos en tu máquina del plano físico, asegurate de contar con las siguientes herramientas instaladas:

```bash
pip install PyQt5 pandas qdarkstyle requests
