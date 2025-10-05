# Seguridad Aplicada – OWASP ASVS Nivel 2

Este documento describe los controles de seguridad implementados en el proyecto *haiti-tts*, alineados con el estándar OWASP Application Security Verification Standard (ASVS) Nivel 2. El objetivo es garantizar la protección de datos sensibles, la integridad del sistema y la mitigación de riesgos comunes en aplicaciones web y de procesamiento de voz.

---

## 1. Autenticación segura

- Se utiliza autenticación basada en tokens JWT con firma HMAC y expiración configurable.
- Las contraseñas se almacenan usando bcrypt con factor de coste 12.
- Se aplican políticas de complejidad mínima en contraseñas (longitud, caracteres especiales).
- No se permiten credenciales por defecto en entornos productivos.

---

## 2. Gestión de sesiones

- Los tokens de sesión expiran tras 30 minutos de inactividad.
- Las cookies (si se usan) incluyen atributos `Secure`, `HttpOnly` y `SameSite=Strict`.
- No se almacena información de sesión en el cliente fuera del token.

---

## 3. Validación de entradas

- Todos los endpoints de la API utilizan modelos `pydantic` para validar tipos, rangos y formatos.
- Se rechazan entradas fuera de esquema o con caracteres peligrosos.
- Se escapan entradas antes de ser almacenadas o mostradas.

---

## 4. Protección contra inyecciones

- Se utiliza SQLAlchemy para evitar inyecciones SQL.
- No se ejecutan comandos shell con entradas del usuario.
- Se escapan entradas en logs, respuestas HTML y cabeceras.

---

## 5. Cifrado de datos sensibles

- Todo tráfico en entornos remotos se realiza por HTTPS con TLS 1.2 o superior.
- Las grabaciones de voz se cifran en reposo usando AES-256.
- No se almacenan datos sensibles sin cifrado ni en texto plano.

---

## 6. HTTPS obligatorio

- Se configura HTTPS en entornos de staging y producción mediante certificados válidos (ej. Let's Encrypt).
- Se fuerza redirección automática de HTTP a HTTPS.
- Se documenta el uso de HTTPS en `infra/` y en las guías de despliegue.

---

## 7. Riesgos mitigados

- Inyección SQL y de comandos
- Exposición de datos sensibles
- Sesiones inseguras o persistentes
- Validación insuficiente de entradas
- Tráfico no cifrado

---

## 8. Referencias

- [OWASP ASVS Nivel 2](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)