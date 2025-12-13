import discord
import random
import google.generativeai as genai

# Configuración de API de gemini
genai.configure(api_key="TU_API_KEY_DE_GOOGLE_AQUI")

# privilegios del bot
intents = discord.Intents.default()
# permisos de lectura
intents.message_content = True
client = discord.Client(intents=intents)

# activar el modelo de Gemini
GEMINI_MODEL = genai.GenerativeModel("gemini-2.5-flash")


# seleccionar aleatoriamente del diccionario
def aleatorioselecc(diccionario, cant=1):
    return random.sample(list(diccionario.values()), cant)


# preguntar si quiere más info (Asincrona)
async def preguntar_mas(message, tema):
    await message.channel.send("¿Quieres más información sobre esto?")

    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower().strip() in ["sí", "no", "si"]
    try:
        respuesta = await client.wait_for("message", check=check, timeout=30)
        if respuesta.content.lower().strip() in ["sí", "si"]:
            await message.channel.send(articulos[tema])
        else:
            await message.channel.send("Oh, ok :(")
            await message.channel.send("https://media.giphy.com/media/ISOckXUybVfQ4/giphy.gif")
    except:
        await message.channel.send("No respondiste a tiempo. 😞")


# Evento al iniciar el bot
@client.event
async def on_ready():
    # Configurar el estado del bot
    await client.change_presence(activity=discord.Game(name="$comandos | ¡EcoBot!"))
    print(f'Hemos iniciado sesión como {client.user} y estamos listos.')


# Diccionarios y listas
diccionarioAgua = {
    1: "Recolectar el agua fría inicial de la ducha en un balde para usarla al limpiar pisos o regar plantas.",
    2: "Reutilizar el agua de cocción (sin sal) de verduras, huevos o pasta para regar las plantas, ya que contiene nutrientes que las benefician.",
    3: "Reutilizar el agua de lavar frutas y verduras para regar macetas o plantas pequeñas en lugar de desecharla por el desagüe.",
    4: "Tomar duchas de 5 minutos o menos y usar un temporizador. Una ducha corta puede ahorrar hasta 40 litros de agua en comparación con una de 10 minutos.",
    5: "Colocar una bandeja debajo de las macetas para recuperar el agua que escurre y usarla en otras plantas.",
    6: "Descongelar alimentos en el refrigerador en lugar de usar agua corriente caliente, lo cual es más seguro e hídricamente eficiente.",
    7: "Asegurarse de que las lavadoras y lavavajillas estén siempre llenos antes de iniciar un ciclo, maximizando la eficiencia de cada lavado.",
    8: "Cerrar la llave de paso si sales de casa por un periodo prolongado, previniendo posibles fugas o desperdicios accidentales.",
    9: "Evitar comprar ropa de 'moda rápida' (fast fashion), ya que la industria textil es una de las mayores consumidoras y contaminadoras de agua a nivel mundial.",
    10: "Monitorear la factura de agua mensualmente para identificar aumentos inusuales que puedan indicar fugas ocultas.",
    11: "Colocar una botella llena dentro del tanque del inodoro para reducir el agua que se usa en cada descarga sin afectar el funcionamiento.",
    12: "Usar una cubeta para recoger el agua que sale al esperar que el grifo del baño o la cocina se caliente, y reutilizarla para limpiar.",
    13: "Instalar aireadores o reductores de caudal en los grifos para disminuir el consumo sin perder presión útil.",
    14: "Lavar el carro únicamente cuando sea necesario y usar un balde en vez de manguera para evitar desperdicios.",
    15: "Reparar de inmediato llaves que gotean o inodoros que funcionan constantemente, ya que pueden desperdiciar cientos de litros al día.",
    16: "Colocar una tapa sobre ollas y sartenes al cocinar para reducir la evaporación y conservar más agua en la preparación.",
    17: "Lavar las frutas en un recipiente y no bajo el chorro, reutilizando esa agua para limpiar superficies.",
    18: "Optar por productos de limpieza biodegradables para evitar contaminar el agua doméstica que se reutiliza en plantas.",
    19: "Recolectar el agua de lluvia del techo usando canaletas y un recipiente cerrado, únicamente si es seguro y permitido en la zona.",
    20: "Poner recordatorios visibles en la casa (baño, cocina) para que todos los miembros del hogar adopten hábitos de ahorro de agua."
}

diccionarioTierra = {
    1: "Separar restos orgánicos del hogar para hacer compost en lugar de tirarlos a la basura.",
    2: "Utilizar el compost casero para enriquecer macetas y jardines, mejorando la calidad del suelo.",
    3: "Evitar barrer tierra hacia las alcantarillas para prevenir obstrucciones y pérdida de suelo.",
    4: "Cubrir la tierra de macetas y jardines con hojas secas para mantener humedad y evitar erosión.",
    5: "Sembrar plantas nativas en el jardín, ya que protegen el suelo y requieren menos agua.",
    6: "Evitar el uso de químicos fuertes que puedan filtrarse al suelo y dañarlo.",
    7: "Reutilizar hojas, ramas finas y pasto cortado como cobertura natural del suelo.",
    8: "Evitar pisar la tierra húmeda para no compactarla y permitir que las raíces respiren.",
    9: "No verter aceite de cocina usado sobre el suelo, ya que lo contamina y afecta las plantas.",
    10: "Construir pequeñas barreras con piedras en áreas inclinadas del jardín para reducir la erosión.",
    11: "Plantar árboles o arbustos en zonas donde el viento o la lluvia arrastran la tierra.",
    12: "Conservar parte de la capa de hojas en el jardín para proteger el suelo de la sequía.",
    13: "Mantener a las mascotas en zonas designadas para evitar que alteren o contaminen áreas sensibles.",
    14: "Usar fertilizantes orgánicos en lugar de los sintéticos que pueden deteriorar la calidad del suelo.",
    15: "Recoger tierra derramada en macetas o patios y devolverla a un área adecuada en lugar de desecharla.",
    16: "Regar suavemente usando rociadores para evitar que el agua arrastre la capa superficial del suelo.",
    17: "Colocar mallas o barreras en zonas con viento fuerte para evitar que la tierra suelta sea arrastrada.",
    18: "Cultivar plantas de raíces profundas para mejorar la estabilidad del suelo en áreas propensas a erosión.",
    19: "Aprovechar restos de café y cáscaras de huevo trituradas como enmiendas naturales para el suelo.",
    20: "Revisar periódicamente el patio o jardín para detectar erosión o grietas y corregirlas con compost o plantas."
}


diccionarioAire = {
    1: "Ventilar la casa diariamente abriendo ventanas durante unos minutos para renovar el aire interior.",
    2: "Mantener limpios los filtros de aire acondicionado, abanicos y extractores para evitar la acumulación de polvo.",
    3: "Evitar quemar basura, hojas o madera dentro del hogar, ya que libera partículas contaminantes.",
    4: "Usar productos de limpieza biodegradables o con bajo contenido químico para evitar vapores tóxicos.",
    5: "Limpiar el polvo con paños húmedos para evitar que las partículas vuelvan al aire.",
    6: "Colocar plantas purificadoras como potos, lengua de suegra o helechos para mejorar la calidad del aire interior.",
    7: "Evitar el uso excesivo de aerosoles como desodorantes, perfumes o ambientadores en espacios cerrados.",
    8: "Revisar periódicamente estufas y calentadores para asegurarse de que no emitan gases peligrosos.",
    9: "No fumar dentro de la casa, ya que el humo contamina el aire y se impregna en muebles y tejidos.",
    10: "Cocinar con tapa cuando sea posible para reducir la cantidad de vapor y humo en el ambiente.",
    11: "Usar extractores de cocina al cocinar para eliminar humo y grasa del aire interior.",
    12: "Evitar el uso de incienso o velas aromáticas de baja calidad que liberan hollín y químicos.",
    13: "Sacar la basura orgánica diariamente para evitar malos olores y gases de descomposición.",
    14: "Lavar regularmente cortinas, cobijas y alfombras para reducir polvo y ácaros.",
    15: "Aspirar con filtros HEPA si es posible para retener partículas finas del aire.",
    16: "Reducir el uso de químicos fuertes como solventes, pinturas y diluyentes dentro de la casa.",
    17: "Mantener las mascotas aseadas para disminuir la cantidad de pelo y caspa en el ambiente.",
    18: "Evitar el uso de carbón o leña en interiores, incluso en pequeñas cantidades.",
    19: "Colocar recipientes con agua en espacios secos para mantener la humedad adecuada y evitar polvo en suspensión.",
    20: "Crear un pequeño rincón verde en casa con varias plantas para mejorar la oxigenación del ambiente."
}


diccionarioEnergia = {
    1: "Apagar luces cuando no se estén usando para evitar consumo innecesario.",
    2: "Conectar aparatos a regletas con interruptor para apagarlos completamente cuando no se usan.",
    3: "Desenchufar cargadores de teléfono cuando no están cargando nada.",
    4: "Usar focos LED en lugar de incandescentes para ahorrar energía.",
    5: "Aprovechar la luz natural abriendo cortinas y ventanas durante el día.",
    6: "Planchar solo cuando haya suficiente ropa acumulada para evitar ciclos repetidos.",
    7: "Cerrar bien la refrigeradora para evitar filtración de aire frío.",
    8: "Lavar la ropa con agua fría para reducir el uso del calentador.",
    9: "Programar el aire acondicionado a una temperatura moderada (entre 23 y 25°C).",
    10: "Limpiar regularmente los filtros del aire acondicionado para mejorar su eficiencia.",
    11: "Usar ventiladores en lugar de aire acondicionado cuando sea posible.",
    12: "Cargar dispositivos electrónicos durante el día para evitar olvidar cargadores conectados.",
    13: "Apagar la computadora si no se va a usar por más de 30 minutos.",
    14: "Usar el modo ‘ahorro de energía’ en celulares, computadoras y televisores.",
    15: "Cerrar puertas y ventanas cuando el aire acondicionado está en uso para evitar fugas.",
    16: "Evitar abrir constantemente la refrigeradora para no gastar más energía.",
    17: "Desconectar electrodomésticos pequeños como tostadoras o licuadoras después de usarlos.",
    18: "Usar ollas de presión para reducir el tiempo de cocción.",
    19: "Hervir solo la cantidad de agua necesaria para cada uso.",
    20: "Secar la ropa al sol en lugar de usar secadora cuando las condiciones lo permitan."
}


diccionarioResiduos = {
    1: "Separar la basura en orgánica, reciclaje y desechos no reciclables.",
    2: "Evitar comprar productos con empaques innecesarios.",
    3: "Reutilizar frascos de vidrio para almacenar alimentos o materiales pequeños.",
    4: "Usar bolsas reutilizables para las compras.",
    5: "Evitar usar utensilios desechables como platos y cubiertos plásticos.",
    6: "Reparar objetos antes de reemplazarlos para extender su vida útil.",
    7: "Comprar productos a granel para reducir empaques.",
    8: "Reutilizar sobres y cajas para almacenamiento.",
    9: "Usar botellas reutilizables en lugar de comprar botellas plásticas.",
    10: "Dar una segunda vida a ropa vieja convirtiéndola en paños de limpieza.",
    11: "Evitar imprimir documentos a menos que sea necesario.",
    12: "Llevar envases propios para comidas para llevar cuando sea permitido.",
    13: "Compactar envases de plástico para reducir el volumen de la basura.",
    14: "Donar ropa y objetos en buen estado en lugar de tirarlos.",
    15: "Evitar compras impulsivas para reducir generación de residuos.",
    16: "Reutilizar papel impreso por un solo lado como borrador.",
    17: "Transformar envases como latas y botellas en macetas caseras.",
    18: "Organizar un punto de reciclaje en casa para separar correctamente.",
    19: "Comprar productos con envases retornables cuando sea posible.",
    20: "Reducir el consumo de productos de un solo uso como pajillas o servilletas."
}


diccionarioBiodiversidad = {
    1: "Plantar especies nativas para atraer fauna local y proteger ecosistemas.",
    2: "Evitar el uso de pesticidas químicos que dañan insectos benéficos.",
    3: "Crear un pequeño jardín con flores que atraigan polinizadores como abejas y mariposas.",
    4: "Mantener recipientes con agua para aves en zonas seguras y limpias.",
    5: "Evitar retirar completamente hojas secas, ya que sirven de refugio para insectos.",
    6: "Instalar pequeñas casitas para aves o insectos en el jardín.",
    7: "Reducir el uso de herbicidas para permitir que plantas pequeñas crezcan y alimenten fauna.",
    8: "Evitar comprar plantas o animales de origen ilegal.",
    9: "No liberar mascotas exóticas en ambientes naturales.",
    10: "Crear espacios verdes en balcones o terrazas para apoyar vida silvestre urbana.",
    11: "Mantener fuentes de agua limpias para no perjudicar especies locales.",
    12: "Promover la reproducción natural de plantas dejando algunas flores fructificar.",
    13: "Cuidar árboles y arbustos existentes en lugar de talarlos innecesariamente.",
    14: "No molestar nidos o madrigueras de animales silvestres.",
    15: "Evitar alimentar animales silvestres con comida procesada.",
    16: "Usar iluminación exterior moderada para no afectar insectos nocturnos.",
    17: "Dejar zonas del jardín sin cortar para permitir refugios naturales.",
    18: "Cultivar diferentes tipos de plantas para aumentar la diversidad del jardín.",
    19: "Reubicar insectos dentro del hogar en lugar de eliminarlos cuando sea posible.",
    20: "Evitar remover piedras o troncos que funcionan como refugio para pequeños animales."
}

hello = [
    "https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif?cid=ecf05e47iufwqgmwcn9eluxk4cx8m1wrgovqxiwqotai1lpb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/XO8RMtRaK73isIt0i2/giphy.gif?cid=ecf05e47iufwqgmwcn9eluxk4cx8m1wrgovqxiwqotai1lpb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g"
]

memesDelCambioClimatico = [
    "https://images3.memedroid.com/images/UPLOADED727/62bb144411371.jpeg",
    "https://i.pinimg.com/originals/df/e3/24/dfe3244dc8317fb7c7acf6af05e4cf75.jpg",
    "https://images7.memedroid.com/images/UPLOADED929/65c01951785c5.jpeg",
    "https://i.pinimg.com/736x/4c/82/25/4c8225c4e8d28403579be8bdf7e54800.jpg",
    "https://razonpublica.com/wp-content/uploads/2020/04/meme-172.jpg",
    "https://cdn.memegenerator.es/imagenes/memes/thumb/32/15/32154965.jpg",
    "https://cdn.memegenerator.es/imagenes/memes/thumb/33/6/33065279.jpg",
    "https://cdn.memegenerator.es/imagenes/memes/full/31/12/31123419.jpg",
    "https://cdn.memegenerator.es/imagenes/memes/full/31/69/31696614.jpg",
    "https://cdn.memegenerator.es/imagenes/memes/full/32/16/32161323.jpg",
    "https://tse3.mm.bing.net/th/id/OIP.eD6f8xLbgCbWtLgbN-zpUAHaHM?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
    "https://cdn.memegenerator.es/imagenes/memes/full/32/18/32180660.jpg"
]

comandos = [
    "$comandos - 📋 Muestra esta lista de comandos.",
    "$hola  -  👋 Te saluda con un GIF de bienvenida.",
    "$cuidar_agua  - 💧 Acción aleatoria para cuidar el agua.",
    "$cuidar_tierra  - 🌳 Acción aleatoria para cuidar la tierra.",
    "$cuidar_aire  - 🌬️ Acción aleatoria para cuidar el aire.",
    "$cuidar_energia  - ⚡ Acción aleatoria para cuidar la energía.",
    "$cuidar_residuos  - ♻️ Acción aleatoria para cuidar los residuos.",
    "$cuidar_biodiversidad  - 🦋 Acción aleatoria para cuidar la biodiversidad.",
    "$memes  - 😂 Envía un meme aleatorio sobre el cambio climático."
]
com = "\n".join(comandos)

# Diccionario de artículos
articulos = {
    "agua": "https://www.un.org/es/climatechange/science/climate-issues/water",
    "tierra": "https://es.weforum.org/stories/2024/12/por-que-la-salud-del-suelo-es-esencial-para-combatir-el-cambio-climatico/",
    "aire": "https://www.fundacionaquae.org/wiki/106-consejos-para-reducir-la-contaminacion-del-aire/",
    "energia": "https://institutodelagua.es/cambio-climatico/energia-y-cambio-climaticocambio-climatico/",
    "residuos": "https://formaeactiva.com/reduccion-de-residuos-claves-para-un-futuro-sostenible/",
    "biodiversidad": "https://www.un.org/es/climatechange/science/climate-issues/biodiversity"
}


#  estado del bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="$comandos | ¡EcoBot!"))
    print(f'Hemos iniciado sesión como {client.user} y estamos listos.')


@client.event
async def on_message(message):
    # Ignorar mensajes propios
    if message.author == client.user:
        return
    content = message.content.lower().strip()

    # Comando para mostrar la lista de comandos
    if content.startswith('$comandos'):
        await message.channel.send(f"**🌱 Comandos del EcoBot:**\n\n{com}")

    # Saludo con GIF aleatorio
    elif content.startswith("$hola"):
        await message.channel.send(random.choice(hello))

    # Comando para cuidar el agua
    elif content.startswith("$cuidar_agua"):
        agua = aleatorioselecc(diccionarioAgua)
        await message.channel.send(f"💧 **Consejo de Ahorro de Agua:** {''.join(agua)}")
        await preguntar_mas(message, "agua")

    # Comando para cuidar la tierra
    elif content.startswith("$cuidar_tierra"):
        tierra = aleatorioselecc(diccionarioTierra)
        await message.channel.send(f"🌳 **Consejo de Cuidado de la Tierra:** {''.join(tierra)}")
        await preguntar_mas(message, "tierra")

    # Comando para cuidar el aire
    elif content.startswith("$cuidar_aire"):
        aire = aleatorioselecc(diccionarioAire)
        await message.channel.send(f"🌬️ **Consejo de Aire Limpio:** {''.join(aire)}")
        await preguntar_mas(message, "aire")

    # Comando para cuidar la energía
    elif content.startswith("$cuidar_energia"):
        energia = aleatorioselecc(diccionarioEnergia)
        await message.channel.send(f"⚡ **Consejo de Ahorro de Energía:** {''.join(energia)}")
        await preguntar_mas(message, "energia")

    # Comando para cuidar los residuos
    elif content.startswith("$cuidar_residuos"):
        residuos = aleatorioselecc(diccionarioResiduos)
        await message.channel.send(f"♻️ **Consejo de Gestión de Residuos:** {''.join(residuos)}")
        await preguntar_mas(message, "residuos")

    # Comando para cuidar la biodiversidad
    elif content.startswith("$cuidar_biodiversidad"):
        biodiversidad = aleatorioselecc(diccionarioBiodiversidad)
        await message.channel.send(f"🦋 **Consejo de Protección de Biodiversidad:** {''.join(biodiversidad)}")
        await preguntar_mas(message, "biodiversidad")

    # Comando para memes del cambio climático
    elif content.startswith("$memes"):
        meme = random.choice(memesDelCambioClimatico)
        await message.channel.send(f"😂 **Meme sobre el Cambio Climático:**\n{meme}")

    # Si no es un comando conocido, usa Gemini para responder
    else:
        try:
            # PROMPT DE LA IA
            prompt = f"""
Eres EcoBot, tu rol es ser un amigo y confidente en temas ambientales. Tu misión es ayudar a la gente a fomentar acciones prácticas y sostenibles contra el cambio climático.

Tu tono de conversación debe ser:
1. Amigable, personal, empático y muy fluido.** Responde como si estuvieras chateando con un amigo de confianza.
2. Usa un lenguaje de chat natural.** No uses términos formales.
3. Debes usar emojis** (como 🌎, 🌱, 💡, 💧, 🔥, ♻️ u otros mas) para hacerlo visualmente atractivo.
4. Ocasionalmente, puedes usar un poco de sarcasmo, un chiste o una referencia de cultura musical ** si es relevante para el tema, pero no de forma constante ni exagerada. El humor debe ser un condimento, no el plato principal.

Reglas de respuesta:
La respuesta debe ser una conversación íntima y fluida.
Sé conciso y ve al grano, si la pregunta es simple (por ejemplo, 1-3 frases). Solo si la pregunta es compleja o requiere motivación, puedes extenderte un poco más. Prioriza el valor sobre la extensión.
Enfócate en dar consejos ecológicos prácticos y motivacionales.
NO uses referencias a "adolescentes", "juventud" o "generación"** en tu respuesta. Mantén el foco en la acción individual y colectiva sin categorizar al usuario.

Responde a este mensaje del usuario: "{message.content}"
"""
            response = GEMINI_MODEL.generate_content(prompt)
            await message.channel.send(response.text[:2000])
        except Exception as e:
            print(f"Error al usar la IA: {e}")
            await message.channel.send("Ups, algo salió mal con la IA. Intenta de nuevo o usa un comando específico. 😅")

# Ejecutar el bot (reemplaza con tu token real)
client.run("TOKEN_DE_TU_BOT_AQUI")
