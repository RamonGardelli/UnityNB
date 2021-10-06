## explicarUniones
  * explicarTema{"tema":"uniones quimicas"}
    -utter_explicarUniones
  
## explicarEstructuraAtomica
  * explicarTema{"tema":"estructura atomica"}
    - utter_explicarEstructura
  
## explicarTablaPeriodica
  * explicarTema{"tema":"tabla periodica"}
    - utter_explicarTabla

## explicarUniones + ejemplo
  * explicarTema{"tema":"uniones quimicas"}
    - utter_explicarUniones
  * darEjemplo
    - utter_darEjemploUniones
    
## explicarEstructuraAtomica
  * explicarTema{"tema":"estructura atomica"}
    - utter_explicarEstructura
  * darEjemplo
    - utter_darEjemploEstructura
    
## explicarTablaPeriodica
  * explicarTema{"tema":"tabla periodica"}
    - utter_explicarTabla
  * darEjemplo
    - utter_darEjemploTabla

## explicar + temaEstructura
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"estructura atomica"}
    - utter_explicarEstructura
    
## explicar + temaUniones
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"uniones quimicas"}
    - utter_explicarUniones
 
## explicar + temaTabla
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"tabla periodica"}
    - utter_explicarTabla
    
## explicar + temaEstructura + ejemplo
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"estructura atomica"}
    - utter_explicarEstructura
  * darEjemplo
    - utter_darEjemploEstructura
    
## explicar + temaUniones + ejemplo
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"uniones quimicas"}
    - utter_explicarUniones
  * darEjemplo
    - utter_darEjemploUniones

## explicar + temaTabla
  * explicarTema
    - utter_preguntarPorTema
  * temas{"tema":"tabla periodica"}
    - utter_explicarTabla
  * darEjemplo
    - utter_darEjemploTabla
    
## darEjemploUniones
  * darEjemplo{"tema":"uniones quimicas"}
    - utter_darEjemploUniones
    
## darEjemploEstructura
  * darEjemplo{"tema":"estructura atomica"}
    - utter_darEjemploEstructura
    
## darEjemploTabla
  * darEjemplo{"tema":"tabla periodica"}
    - utter_darEjemploTabla
    
## darEjemplo + temaUniones
  * darEjemplo
    - utter_preguntarPorEjemplo
  * temas{"tema":"uniones quimicas"}
    - utter_darEjemploUniones
    
## darEjemplo + temaEstructura
  * darEjemplo
    - utter_preguntarPorEjemplo
  * temas{"tema":"estructura atomica"}
    - utter_darEjemploEstructura
    
## darEjemplo + temaTabla
  * darEjemplo
    - utter_preguntarPorEjemplo
  * temas{"tema":"tabla periodica"}
    - utter_darEjemploTabla

## preguntar fechas
  * preguntarFechas
    - utter_darFechasExamenes
    
## preguntar fechas parcial
  * preguntarFechas{"examen":"parcial"}
    - utter_darFechasParcial
    

## preguntar fechas recuperatorio
  * preguntarFechas{"examen":"recuperatorio"}
    - utter_darFechasRecuperatorio
    
## preguntar fechas prefinal
  * preguntarFechas{"examen":"prefinal"}
    - utter_darFechasPrefinal
    
## agradecer
  * agradecer
    - utter_agradecer
    
## saludar
  * saludar
    - utter_saludar
