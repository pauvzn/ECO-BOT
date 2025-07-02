import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

EcoBot = commands.Bot(command_prefix = "%", intents = intents)

#ECOTRIVIA
preguntas = [
    {
        "pregunta": "¿Cuál de estos materiales es totalmente reciclable?",
        "opciones": ["A) Vidrio", "B) Plástico", "C) Papel encerado", "D) Telgopor"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es un animal en peligro de extinción?",
        "opciones": ["A) Oso polar", "B) Paloma", "C) Gato doméstico", "D) Vaca"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuánto tarda en degradarse una botella de plástico?",
        "opciones": ["A) 1 año", "B) 10 años", "C) 100 años", "D) 450 años"],
        "respuesta": "D"
    },
    {
        "pregunta": "¿Qué podemos hacer para cuidar el agua?",
        "opciones": ["A) Dejar el grifo abierto", "B) Lavar el auto todos los días", "C) Reparar fugas", "D) Usar más detergente"],
        "respuesta": "C"
    },
    {
    "pregunta": "¿Qué recurso natural es el más utilizado para producir electricidad en el mundo?",
    "opciones": ["A) Viento", "B) Sol", "C) Carbón", "D) Agua"],
    "respuesta": "C"
    },
    {
    "pregunta": "¿Cuál de los siguientes residuos tarda más tiempo en degradarse?",
    "opciones": ["A) Cáscara de plátano", "B) Lata de aluminio", "C) Papel", "D) Cartón"],
    "respuesta": "B"
    },
    {
    "pregunta": "¿Qué significa la regla de las 3R?",
    "opciones": ["A) Reducir, Reutilizar, Reciclar", "B) Recolectar, Reparar, Repartir", "C) Reusar, Renovar, Reintegrar", "D) Rechazar, Reciclar, Reutilizar"],
    "respuesta": "A"
    },
    {
    "pregunta": "¿Cuál de estos gases es el principal responsable del efecto invernadero?",
    "opciones": ["A) Oxígeno", "B) Dióxido de carbono", "C) Nitrógeno", "D) Helio"],
    "respuesta": "B"
    },
    {
    "pregunta": "¿Qué se debe hacer con el aceite usado de cocina?",
    "opciones": ["A) Tirarlo por el fregadero", "B) Verterlo en la tierra", "C) Guardarlo y llevarlo a un punto de reciclaje", "D) Mezclarlo con agua"],
    "respuesta": "C"
    }
    ]
puntajes = {}

#ECODATO
eco_datos = [
    "🌱 Un árbol puede absorber hasta 22 kg de CO₂ al año.",
    "💧 Solo el 3% del agua del mundo es dulce, y la mayoría está congelada.",
    "🌍 Se estima que se pierden 10 millones de hectáreas de bosque cada año.",
    "🐝 Las abejas polinizan el 75% de los cultivos que consumimos.",
    "♻️ El reciclaje de una lata de aluminio ahorra suficiente energía para ver televisión por 3 horas.",
    "🌊 Más del 70% del planeta está cubierto por océanos.",
    "☀️ La energía solar en una hora podría alimentar al mundo por un año.",
    "🌾 La agricultura es responsable del 70% del uso mundial de agua dulce.",
    "🚯 Un solo cigarro puede contaminar hasta 50 litros de agua.",
    "🦋 Más de un millón de especies están en peligro de extinción.",
    "🚲 Usar bicicleta en lugar de coche reduce 90% las emisiones por kilómetro.",
    "🧃 Un envase de cartón tarda 30 años en degradarse.",
    "🌋 Las emisiones volcánicas naturales son menores que las humanas.",
    "❄️ El deshielo del Ártico avanza a un ritmo alarmante cada década.",
    "🌡️ El último año fue uno de los más calurosos jamás registrados.",
    "🗑️ Cada persona genera en promedio 1 kg de basura al día.",
    "🏞️ Los parques nacionales ayudan a conservar la biodiversidad local.",
    "🦜 Más del 80% de las aves migratorias están afectadas por el cambio climático.",
    "🌫️ La contaminación del aire causa 7 millones de muertes al año.",
    "🌌 La Tierra es el único planeta conocido que tiene vida.",
    "🐢 Cada año mueren millones de animales marinos por plástico.",
    "🪴 Las plantas de interior pueden mejorar la calidad del aire en casa.",
    "🛢️ Un litro de aceite usado puede contaminar 1.000 litros de agua.",
    "📦 El cartón reciclado reduce en 60% el consumo de energía respecto al nuevo.",
    "🔥 Los incendios forestales generan más CO₂ que muchos países enteros.",
    "🌳 La deforestación representa cerca del 15% de las emisiones globales.",
    "🚿 Una ducha de 5 minutos consume entre 60 y 100 litros de agua.",
    "🧼 Los jabones biodegradables ayudan a evitar la contaminación de ríos.",
    "🧴 Muchos cosméticos contienen microplásticos dañinos para el océano.",
    "🍃 Las hojas caídas son hábitat y alimento para muchos insectos.",
    "🌀 El reciclaje de papel ahorra hasta 70% de agua en comparación con el nuevo.",
    "🍽️ El desperdicio de comida genera el 8% de los gases de efecto invernadero.",
    "🌐 Internet también contamina: los centros de datos usan mucha energía.",
    "🐘 Cada día mueren elefantes por caza ilegal por el marfil.",
    "🐠 El coral es vital para el ecosistema marino y está desapareciendo.",
    "🌾 La pérdida de suelos fértiles amenaza la seguridad alimentaria.",
    "🦠 Los ecosistemas saludables ayudan a prevenir pandemias.",
    "🚮 El plástico puede tardar más de 400 años en descomponerse.",
    "🍂 Los bosques urbanos ayudan a regular la temperatura de las ciudades.",
    "🌙 Incluso de noche, la contaminación lumínica afecta a los animales."
]

#ECONOTICIA
noticias = [
    ("🌿 Greenpeace", "https://es.greenpeace.org/es/noticias/"),
    ("📘 National Geographic", "https://www.nationalgeographicla.com/medio-ambiente"),
    ("🗞️ El País", "https://elpais.com/noticias/cambio-climatico/"),
    ("📺 DW", "https://www.dw.com/es/cambio-clim%C3%A1tico/t-51325818"),
    ("📷 NASA Climate", "https://climate.nasa.gov/news/"),
    ("📚 Ecoticias", "https://www.ecoticias.com/"),
    ("🌎 ONU Cambio Climático", "https://www.un.org/es/climatechange"),
    ("📰 El Tiempo", "https://www.eltiempo.com/noticias/medio-ambiente"),
    ("📡 BBC Mundo", "https://www.bbc.com/mundo/topics/c340q0r4v8vt"),
    ("🌐 CNN Español", "https://cnnespanol.cnn.com/tag/cambio-climatico/"),
    ("🟢 WWF México", "https://www.wwf.org.mx/quienes_somos/noticias/"),
    ("🧪 EFE Verde", "https://www.efeverde.com/"),
    ("🧭 La Vanguardia", "https://www.lavanguardia.com/natural/medio-ambiente"),
    ("💬 France 24", "https://www.france24.com/es/tag/medio-ambiente/"),
    ("📰 Infobae", "https://www.infobae.com/america/tag/medio-ambiente/")
]
descripciones = [
    "📢 Una noticia importante para el futuro del planeta.",
    "🌱 Mira lo que está pasando con nuestro medio ambiente.",
    "🌍 Información que todos deberíamos conocer.",
    "🍃 ¿Sabías esto sobre la Tierra?",
    "⚠️ Alerta verde: esto está pasando ahora mismo.",
    "🔍 Un dato ecológico que no puedes ignorar.",
    "🧠 Eduquémonos para cuidar nuestro hogar común.",
    "💡 Conocer es el primer paso para cambiar.",
    "📰 Últimas noticias sobre la crisis ambiental.",
    "🌳 Algo está cambiando... entérate aquí:"
]

#RECICLABOT
organico = [
    "cáscara", "fruta", "flores","cáscara de plátano", "servilleta de papel", "hojas secas", "restos de comida",
    "pan viejo", "estropajo vegetal", "huesos de pollo", "flores marchitas",
    "cáscaras de huevo", "papel higiénico", "bolsas de papel", "cáscara de naranja",
    "posos de café", "filtros de café de papel", "palillos de madera", "astillas de madera",
    "cartón sin tinta", "manzana mordida", "tallos de vegetales", "servilleta manchada de comida",
    "bolsa de cartón para pan", "ramitas de plantas", "papel de estraza", "fruta podrida",
    "semillas", "algas", "arroz cocido", "pasta cocida", "pétalos secos", "trapo de algodón natural",
    "harina derramada", "té usado", "papel periódico", "panela", "restos de pescado",
    "plumas de ave", "cabello", "uñas", "corteza de árbol", "tela de lino", "leche derramada",
    "cereal viejo", "trapo de yute", "conchas de frutas", "madera no tratada",
    "papel de libreta reciclado", "aserrín", "tela de cáñamo", "miga de pan", "yerba mate usada"
]
inorganico = [
    "botella de plástico", "lata de aluminio", "bolsa de plástico", "pila o batería",
    "clavo", "foco", "tubo de pvc", "taza de cerámica", "cubiertos de acero", "lentes rotos",
    "espejo", "carcasa de celular", "llave de metal", "alambre", "tapita de refresco",
    "encendedor", "cepillo de dientes", "bolígrafo", "cd o dvd", "cable usb", "audífonos",
    "parte de una licuadora", "cuchilla de afeitar", "juguete plástico", "cubrebocas quirúrgico",
    "tarjeta bancaria", "tijeras", "tornillos", "tapete de plástico", "regla de plástico",
    "botón sintético", "caja de discos duros", "pluma estilográfica", "perilla de puerta",
    "tubería metálica", "malla ciclónica", "lata de aerosol", "llanta", "carcasa de televisión",
    "reloj de pulsera", "caja de herramientas", "anzuelo", "chupón plástico", "botella de vidrio",
    "jeringa", "repuesto de máquina", "casco de bicicleta", "cinta adhesiva", "plumón",
    "termo metálico"
]

#SALUDO
@EcoBot.command()
async def hola(ctx):
    await ctx.send("Hola, soy EcoBot :).\n"
    "Las funciones que tengo son:\n" 
    " 👾 EcoTrivia: Preguntas tipo Kahoot, que nos van a ayudar a conocer un poco más nuestro ecosistema y el cuidado de este.?\n" 
    " 📰 EcoNoticia: Nos va a dar noticias para saber como está nuestro medio ambiente.\n" 
    " ♻️ ReciclaBot: Nos informa si la basura es orgánica o inorgánica.\n" 
    " 🌏 EcoDato: Un dato random para conocer más nuestro mundo.")

#ECOTRIVIA
@EcoBot.command()
async def EcoTrivia(ctx):
    pregunta = random.choice(preguntas)
    opciones = "\n".join(pregunta["opciones"])

    await ctx.send(f"🌱 **EcoTrivia para {ctx.author.mention}**\n"
                   f"**{pregunta['pregunta']}**\n\n{opciones}\n\n"
                   f"Responde con la letra correcta (A, B, C o D). Tienes 20 segundos...")

    def check(m):
        return (m.author == ctx.author and 
                m.channel == ctx.channel and 
                m.content.upper() in ['A', 'B', 'C', 'D'])

    try:
        respuesta = await EcoBot.wait_for("message", check=check, timeout=20.0)
        if respuesta.content.upper() == pregunta["respuesta"]:
            puntajes[ctx.author.name] = puntajes.get(ctx.author.name, 0) + 1
            await ctx.send(f"✅ ¡Correcto, {ctx.author.name}! Ahora tienes {puntajes[ctx.author.name]} punto(s).")
        else:
            await ctx.send(f"❌ Incorrecto. La respuesta correcta era **{pregunta['respuesta']}**.")
    except asyncio.TimeoutError:
        await ctx.send(f"⏰ ¡Tiempo agotado, {ctx.author.name}! La respuesta correcta era **{pregunta['respuesta']}**.")

#ECODATO
@EcoBot.command()
async def EcoDato(ctx):
    dato = random.choice(eco_datos)
    await ctx.send(f"🌏 **EcoDato:** {dato}")

#RECICLABOT
@EcoBot.command()
async def ReciclaBot(ctx):
    await ctx.send("Qué objeto quieres verificar?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await EcoBot.wait_for("message", timeout = 30.0, check = check)
        objeto = msg.content.lower().strip()

        if objeto in organico:
            await ctx.send(f"🌱 {objeto} es un residuo ORGÁNICO (Biodegradable)")
        elif objeto in inorganico:
            await ctx.send(f"♻️ {objeto} es un residuo INORGÁNICO (No biodegradable)")
        else:
            await ctx.send(f"No encontré {objeto} en mis listas")
            await ctx.send("Aquí tienes mis lista disponibles, por si quieres virificar si hay algo similar:\n")

            organicos = ", ".join(organico)
            inorganicos = ", ".join(inorganico)

            await ctx.send("🌱 ORGÁNICOS:\n" + organicos)
            await ctx.send("♻️ INORGÁNICOS:\n" + inorganicos)
    
    except:
        await ctx.send("⏰ ¡Tiempo agotado. Vuelve a intentarlo con '%ReciclaBot'")

#ECONOTICIA
@EcoBot.command()
async def EcoNoticia(ctx):
    fuente, url = random.choice(noticias)
    intro = random.choice(descripciones)
    await ctx.send(f"{intro}\n{fuente}: {url}")

    # Pregunta si quiere ver todas las fuentes
    await ctx.send("¿Quieres ver todas las páginas disponibles? (responde: sí / no)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["sí", "si", "no"]

    try:
        respuesta = await EcoBot.wait_for("message", check=check, timeout=20.0)
        if respuesta.content.lower() in ["sí", "si"]:
            lista = "\n".join([f"{nombre}: {enlace}" for nombre, enlace in noticias])
            await ctx.send(f"📚 Estas son todas las fuentes disponibles:\n{lista}")
        else:
            await ctx.send("✅ ¡Entendido! Si necesitas verlas después, solo vuelve a usar el comando.")
    except asyncio.TimeoutError:
        await ctx.send("⌛ Tiempo agotado. Si quieres ver las páginas después, usa de nuevo `%EcoNoticia`.")



EcoBot.run("TOKEN")