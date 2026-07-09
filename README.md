# 🚀 Serverless Application (Python + AWS)

Este proyecto implementa una arquitectura Serverless utilizando **Serverless Framework v4**, **Python 3.13** y **AWS (API Gateway y Lambda)**. Cuenta con un pipeline automatizado de CI/CD mediante **GitHub Actions** que separa de forma segura los entornos de Desarrollo (`dev`) y Producción (`prod`).

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina local:

* [Node.js](https://nodejs.org/) (Versión 20 o 22 recomendada)
* [Python](https://www.python.org/) (Versión 3.13)
* [AWS CLI](https://aws.amazon.com/cli/) instalado y configurado

---

## 💻 Configuración Local

Sigue estos pasos para configurar el entorno de desarrollo en tu computadora:

### 1. Instalar Serverless Framework
Instala el CLI de Serverless de forma global en tu sistema utilizando npm:
```bash
npm install -g serverless
2. Configurar Credenciales de AWS
Configura tus llaves de acceso de AWS bajo el perfil local requerido por el proyecto (severlees):

Bash
aws configure --profile severlees
Te solicitará tu AWS Access Key ID, AWS Secret Access Key y la región predeterminada (ej. us-east-2).

3. Iniciar Sesión en Serverless (Licencia V4)
Autentica el CLI local con tu cuenta de Serverless Console para activar la licencia de la versión 4:

Bash
serverless login
🚀 Comandos de Desarrollo
Una vez configurado, puedes utilizar los siguientes comandos en tu terminal:

Probar la función localmente (Instantáneo):

Bash
serverless invoke local -f miPrimeraLambda
Desplegar en el entorno de desarrollo (dev):

Bash
serverless deploy
Nota: Al no especificar un stage, por defecto se creará e implementará el entorno dev.

🤖 Despliegue Automatizado (CI/CD con GitHub Actions)
El proyecto está configurado para que cada git push a la rama main despliegue automáticamente en el entorno de Producción (prod) de AWS.

Configuración de Secretos en GitHub
Para que el pipeline funcione, debes ir a tu repositorio en GitHub: Settings ➔ Secrets and variables ➔ Actions y agregar los siguientes tres secretos:

AWS_ACCESS_KEY_ID: Tu llave de acceso de AWS.

AWS_SECRET_ACCESS_KEY: Tu llave secreta de AWS.

SERVERLESS_ACCESS_KEY: Tu llave de consola/licencia generada desde el panel web de Serverless Framework.

Flujo de Trabajo
Cuando el código de la rama main se actualiza, GitHub Actions levanta un contenedor limpio, valida las credenciales y ejecuta de forma segura:

Bash
serverless deploy --stage prod
📂 Estructura del Proyecto
serverless.yml: Definición de la Infraestructura como Código (IaC).

handler.py: Archivo que contiene la lógica y las funciones Python de la Lambda.

.github/workflows/deploy.yml: Configuración del pipeline de automatización en GitHub.