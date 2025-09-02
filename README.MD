# Django REST API - Gestión de Tareas

API REST desarrollada con *Django REST Framework* para la gestión de tareas con filtros por fecha y personas.

---

## 🚀 Características

- *CRUD de personas*: Crear, leer, actualizar y eliminar personas.  
- *Filtro de persona por documento*: Buscar persona por número de documento.  
- *CRUD de tareas*: Crear, leer, actualizar y eliminar tareas.  
- *Filtro por fecha específica*: Obtener tareas de una fecha determinada.  
- *Filtro por rango de fechas*: Buscar tareas entre dos fechas.  
- *Filtro por persona*: Obtener tareas asignadas a una persona específica.  
- Respuestas en formato JSON.  
- Estructura de datos consistente.  

---

## 📋 Endpoints Disponibles

### 1. CRUD de Personas

- **GET** `/api/personas/`  
  Lista todas las personas registradas.  

- **POST** `/api/personas/`  
  Crea una nueva persona.  
  **Ejemplo request (JSON):**
  ```json
  {
    "nombre": "Carlos Pérez",
    "tipo_documento": "CC",
    "numero_documento": "123456789",
    "email": "carlos@example.com"
  }
  ```

- **GET** `/api/personas/{id}/`  
  Obtiene una persona por su ID.  

- **PUT** `/api/personas/{id}/`  
  Actualiza una persona existente.  

- **DELETE** `/api/personas/{id}/`  
  Elimina una persona.  

---

### 2. Filtrar Persona por Número de Documento

- **GET** `/api/personas/documento/{documento}/`  
  Busca una persona específica por su número de documento.  

---

### 3. CRUD de Tareas

- **GET** `/api/tareas/`  
  Lista todas las tareas registradas.  

- **POST** `/api/tareas/`  
  Crea una nueva tarea.  

- **GET** `/api/tareas/{id}/`  
  Obtiene una tarea por su ID.  

- **PUT** `/api/tareas/{id}/`  
  Actualiza una tarea existente.  

- **DELETE** `/api/tareas/{id}/`  
  Elimina una tarea.  

---

### 4. Filtrar Tareas por Fecha

- **GET** `/api/tareas/fecha/{fecha}/`  
  Obtiene todas las tareas programadas para una fecha específica (formato: YYYY-MM-DD).  

---

### 5. Filtrar Tareas por Rango de Fechas

- **GET** `/api/tareas/rango-fechas/{start_date}/{end_date}/`  
  Obtiene todas las tareas dentro de un rango de fechas.  

---

### 6. Filtrar Tareas por Persona

- **GET** `/api/tareas/persona/{id}/`  
  Obtiene todas las tareas asignadas a una persona específica.  

---

## 🏃‍♂ Inicio Rápido

1. *Clonar el repositorio*
   ```bash
   git clone <tu-repositorio>
   cd <nombre-proyecto>
   ```

2. *Crear entorno virtual*
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. *Instalar dependencias*
   ```bash
   pip install -r requirements.txt
   ```

4. *Ejecutar migraciones*
   ```bash
   python manage.py migrate
   ```

5. *Iniciar servidor*
   ```bash
   python manage.py runserver
   ```

👉 La API estará disponible en: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 📚 Documentación Completa

Para ver ejemplos detallados de requests/responses, casos de uso y testing:  
[Ver Documentación Completa en Postman](https://documenter.getpostman.com/view/39723796/2sB3Hhu34U#intro)

Incluye:  
- Ejemplos de requests con cURL.  
- Estructura detallada de respuestas.  
- Casos de error y manejo.  
- Colección de Postman para importar.  

---

## 🛠 Tecnologías

- Django 4.x  
- Django REST Framework  
- Python 3.8+  

---

## 🤝 Contribuir

1. Fork el proyecto.  
2. Crea tu rama de feature:  
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Commit tus cambios:  
   ```bash
   git commit -m "Agregar nueva funcionalidad"
   ```
4. Push a la rama:  
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request.  

---
