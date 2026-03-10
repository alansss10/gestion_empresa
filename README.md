# 🥐 Dulce Herencia — Gestió d'Inventari per a Pastisseria Artesanal

Aplicació web de gestió interna desenvolupada amb Django per al negoci de pràctiques del curs. Permet controlar l'estoc de productes artesanals de manera senzilla i visual.

✨ Funcionalitats

Gestió de Categories — Crear, editar i eliminar categories (Bolleria, Tartes, etc.)
Gestió de Productes — Control de nom, preu, estoc i etiqueta vegana per a cada producte
Alerta d'estoc baix — Els productes amb menys de 5 unitats es marquen automàticament en vermell
Etiqueta Vegà — Badge visual als productes que ho requereixin
Interfície artesanal — Disseny personalitzat amb Bootstrap 5 i Google Fonts

Relació d'entitats 
Categoria
    nom
Producte 
    nom
    categoria
    preu
    stock
    vegano

🛠️ Eines utilitzades
EinaVersióÚsPython3.13Llenguatge principalDjango5.xFramework web i ORMSQLite—Base de dades localBootstrap 55.3Maquetació i dissenyGoogle Fonts—Tipografia artesanalGit + GitHub—Control de versionsGemini (IA)—Suport en la generació de codi

📦 Instal·lació pas a pas
Requisits previs

Python 3.10 o superior instal·lat
Git instal·lat

1. Clonar el repositori
bashgit clone https://github.com/el-teu-usuari/dulce-herencia.git
cd dulce-herencia
2. Crear i activar l'entorn virtual
bash# Crear l'entorn
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Linux / macOS)
source venv/bin/activate
3. Instal·lar dependències
bashpip install django
4. Aplicar les migracions
bashpython manage.py migrate
5. Crear l'usuari administrador
bashpython manage.py createsuperuser
6. Executar el servidor
bashpython manage.py runserver
7. Accedir a l'aplicació
URLDescripcióhttp://127.0.0.1:8000/Vista pública amb el llistat de producteshttp://127.0.0.1:8000/adminPanell d'administració (CRUD complet)

⚠️ Dificultats trobades i solucions
Canvi d'enfocament del negoci
A mig projecte es va decidir canviar de gestió de treballadors a pastisseria. Això va requerir esborrar les migracions anteriors i tornar a definir els models des de zero.
Error TemplateDoesNotExist
Django no trobava les plantilles HTML. Es va solucionar configurant la ruta correcta a DIRS dins de settings.py:
python'DIRS': [BASE_DIR / 'templates'],
Lògica visual d'estoc
Implementar la detecció d'estoc baix directament als templates de Django va requerir entendre com funcionen les etiquetes {% if %} dins del context de la vista.

📝 Avaluació personal del resultat
El resultat final és una aplicació funcional, reproduïble i coherent amb els requisits de l'exercici. S'ha aconseguit:

Com a punt de millora, una versió més avançada podria incloure un historial de moviments d'estoc, un sistema de comandes o autenticació per a la vista pública.

© 2026 Dulce Herencia · Projecte de pràctiques