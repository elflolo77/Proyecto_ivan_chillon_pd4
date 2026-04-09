# ARQUITECTURA POR CAPAS

## Descripción
Cine Flolix está estructurado utilizando el patrón de Diseño Arquitectónico de Software por Capas (N-Tier Architecture), específicamente la variante de **Onion Architecture / Clean Architecture** adaptada a un caso sencillo. El objetivo es aislar la lógica de dominio del resto del sistema.

## Capas

### 1. `domain` (Dominio)
Contiene las entidades centrales de negocio:
- **`Entrada`**: Representa un ticket vendido.
- **`Pelicula`**: Entidad base y sus clases especializadas (`PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica`).
- **`Sala`**: Representa un espacio físico del cine con aforo limitado y tecnología.
- **`Sesion`**: Relaciona una Película, con una Sala y una fecha/hora.
- **`RepositorioCine` (Interfaz)**: Define el contrato de persistencia para desacoplar el dominio.
*Restricción*: El Dominio no depende de nada, y nada más importa aquí.

### 2. `application` (Aplicación)
Contiene los "Casos de Uso".
- **`ServicioCine`**: Orquesta y coordina las operaciones entre el Dominio y el Repositorio. Aquí reside la lógica de precios y se orquesta la venta o devolución de entradas.
*Restricción*: Esta capa depende del Dominio, y del contrato (Interfaz), pero nunca implementa directamente detalles técnicos de BD.

### 3. `infrastructure` (Infraestructura)
Detalles técnicos y persistencia.
- **`RepositorioMemoria`**: Implementa la interfaz `RepositorioCine`. Utiliza diccionarios y listas en memoria para volcar el estado temporal de la aplicación.
- **`datos_iniciales`**: Genera registros de prueba (mock) listos para usar en la aplicación.

### 4. `presentation` (Presentación)
Interfaz de usuario (CLI).
- **`MenuCine`**: Toma las entradas del usuario (teclado), imprime salidas (consola) e invoca los métodos correspondientes en `ServicioCine`.
*Restricción*: La presentación se comunica con Aplicación, y jamás habla directo con Infraestructura.
