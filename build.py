#!/usr/bin/env python3
# Generator voor peugeottuningclub.nl - onafhankelijk kennisplatform over Peugeot-tuning.
import os, json, html, hashlib

def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE="https://peugeottuningclub.nl"
SITE="Peugeot Tuning Club"
EMAIL="info@peugeottuningclub.nl"
AUTEUR="Bas Koopman"
AUTEUR_ROL="Techniekredacteur"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site")
CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "car":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13l2-5a3 3 0 0 1 3-2h8a3 3 0 0 1 3 2l2 5"/><path d="M3 13h18v4H3z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg>',
 "wrench":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3a5 5 0 0 0-4.6 7L3 17.4 6.6 21l7.4-7.4A5 5 0 1 0 15 3z"/></svg>',
 "gauge":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18a8 8 0 1 1 16 0"/><line x1="12" y1="18" x2="16" y2="11"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Kennisbank","/kennisbank/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Contact","/contact/")]

def head(title,desc,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta name="theme-color" content="#14181F">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
  <nav class="nav" id="nav">
    <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Peugeot Tuning Club</b><span>Kennisplatform</span></span></a>
    {nav}
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap">
  <div class="cols">
    <div>
      <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Peugeot Tuning Club</b><span>Kennisplatform</span></span></a>
      <p class="note">Peugeot Tuning Club is een onafhankelijk kennisplatform over het modificeren van Peugeot-modellen. Het platform verkoopt geen onderdelen, voert geen werkzaamheden uit en heeft geen band met Peugeot of Stellantis.</p>
    </div>
    <div><h4>Kennis</h4>
      <a href="/kennisbank/">Kennisbank</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
    <div><h4>Informatie</h4>
      <a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
  </div>
  <div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
  <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div>
</div></footer>
</body></html>"""

def crumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}
def crumbs_html(items):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]; o.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="ph": o.append(f"<p>{b[1]}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
        elif b[0]=="warn": o.append(f'<div class="warn"><p>{esc(b[1])}</p></div>')
    return "".join(o)
def byline():
    return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

RDW="Modificaties moeten voldoen aan de eisen van de RDW. Wijzigingen aan constructie, verlichting, uitlaatgeluid of banden kunnen keuringsplichtig zijn en kunnen gevolgen hebben voor de verzekering. Twijfel wegnemen kan bij de RDW zelf of bij een erkend keuringsstation."

ITEMS=[
 {"slug":"peugeot-205-gti","naam":"Peugeot 205 GTI","kind":"Model","b":False,
  "resume":"De hatchback die in de jaren tachtig de maatstaf zette, en tot vandaag het meest bewerkte Peugeot-model is.",
  "specs":[("Bouwjaren","1984 tot 1994"),("Motoren","1.6 en 1.9 XU"),("Gewicht","Circa 850 kg"),("Aandrijving","Voorwielen")],
  "secties":[("Waarom het gewicht alles bepaalt","Met ongeveer 850 kilo is de 205 GTI naar moderne maatstaven extreem licht. Dat verklaart waarom een bescheiden vermogenswinst hier meer effect heeft dan bij een zware auto, en waarom de meeste ervaren bouwers eerst naar ophanging en remmen kijken voordat er vermogen bij komt."),
   ("Aandachtspunten bij een exemplaar","Roest in de achterschermen, de bodemplaat en rond de achteras is het grootste risico. De achteras zelf staat bekend om ingelopen naaldlagers, wat zich uit in scheve wielstanden en ongelijkmatige bandenslijtage. Beide zijn te herstellen, maar bepalen sterk wat een auto waard is."),
   ("Wat er meestal als eerste gebeurt","Een revisie van de achteras, nieuwe schokdempers en veren, en een grondige beurt aan de remmen. Pas daarna komen inlaat, uitlaat en motormanagement in beeld.")],
  "punten":["Licht gewicht maakt elke wijziging voelbaar","Achteras is het bekendste slijtagepunt","Onderdelenvoorziening is nog altijd goed","Originaliteit weegt zwaar in de waarde"]},
 {"slug":"peugeot-106-rallye","naam":"Peugeot 106 Rallye","kind":"Model","b":False,
  "resume":"Een kale, lichte homologatie-uitvoering zonder luxe, gebouwd rond een hoogtoerige motor.",
  "specs":[("Bouwjaren","1993 tot 1998"),("Motoren","1.3 en 1.6 TU"),("Gewicht","Circa 825 kg"),("Aandrijving","Voorwielen")],
  "secties":[("Kaalheid als uitgangspunt","De Rallye werd bewust zonder stuurbekrachtiging, elektrische ramen en isolatie geleverd. Dat maakt de auto licht en direct, maar ook onvriendelijk in dagelijks gebruik. Wie er een straatauto van maakt, voegt vaak juist comfort toe in plaats van vermogen."),
   ("Hoogtoerig van huis uit","De motor levert zijn vermogen ver in het toerenbereik. Bewerkingen die dat karakter versterken, zoals een andere nokkenas of een aangepaste inlaat, gaan ten koste van bruikbaarheid onderin. De keuze tussen circuit en straat wordt hier al gemaakt."),
   ("Zeldzaamheid","Het aantal originele exemplaren daalt gestaag. Auto's die nog in oorspronkelijke staat verkeren, worden inmiddels vaker bewaard dan bewerkt.")],
  "punten":["Minimalistisch en licht","Vermogen zit hoog in het toerenbereik","Onbewerkte exemplaren worden schaars","Comfort toevoegen is een veelgemaakte keuze"]},
 {"slug":"peugeot-306-gti-6","naam":"Peugeot 306 GTI-6","kind":"Model","b":False,
  "resume":"Een grotere hatchback met zesbak en een onderstel dat door velen als het beste van zijn tijd wordt beschouwd.",
  "specs":[("Bouwjaren","1996 tot 2001"),("Motor","2.0 16V XU10J4RS"),("Versnellingen","Zes"),("Gewicht","Circa 1200 kg")],
  "secties":[("Het onderstel als hoofdrol","De 306 staat bekend om zijn achteras met passieve meesturing, die de auto in bochten opvallend neutraal maakt. Veel eigenaren laten de geometrie met rust en richten zich op dempers en bussen, omdat de basis al goed is."),
   ("De zesbak","De zesversnellingsbak was destijds uitzonderlijk in dit segment en heeft korte verhoudingen. Dat maakt de auto levendig, maar zorgt voor hoge toerentallen op de snelweg. Een andere eindoverbrenging is een gangbare aanpassing voor wie veel kilometers maakt."),
   ("Slijtage en onderhoud","Rubbers en bussen zijn na dertig jaar vrijwel altijd toe aan vervanging. Dat is minder spectaculair dan vermogenswinst, maar bepaalt in de praktijk hoe de auto rijdt.")],
  "punten":["Onderstel geldt als referentie","Korte verhoudingen door de zesbak","Bussen en rubbers zijn het aandachtspunt","Ruimer bruikbaar dan de kleinere modellen"]},
 {"slug":"peugeot-206-rc","naam":"Peugeot 206 RC","kind":"Model","b":False,
  "resume":"De sportiefste 206, met een tweeliter viercilinder en een duidelijk stuggere afstemming dan de gewone uitvoeringen.",
  "specs":[("Bouwjaren","2003 tot 2007"),("Motor","2.0 16V EW10J4S"),("Vermogen","Circa 130 kW"),("Gewicht","Circa 1160 kg")],
  "secties":[("Een andere motor dan de rest","De RC kreeg een sterk aangepaste versie van de tweeliter, met onder meer een andere cilinderkop en inlaat. Onderdelen zijn daardoor minder uitwisselbaar met andere 206-uitvoeringen dan vaak gedacht."),
   ("Afstemming van fabriek","De auto is van origine stug geveerd. Verder verlagen levert op straat snel meer nadeel dan voordeel op; veel eigenaren kiezen daarom voor betere dempers in plaats van kortere veren."),
   ("Praktijkpunten","De koppeling en het tweemassavliegwiel zijn bekende kostenposten. Onderhoudshistorie weegt bij dit model zwaarder dan de kilometerstand.")],
  "punten":["Eigen motorvariant, minder uitwisselbaar","Van fabriek al stug afgeveerd","Onderhoudshistorie is doorslaggevend","Dempers boven kortere veren"]},
 {"slug":"peugeot-208-gti","naam":"Peugeot 208 GTi","kind":"Model","b":False,
  "resume":"De moderne interpretatie, met een turbomotor die zich met software en luchtstroom eenvoudiger laat aanpassen dan de oudere blokken.",
  "specs":[("Bouwjaren","2012 tot 2019"),("Motor","1.6 THP turbo"),("Vermogen","Circa 147 tot 153 kW"),("Gewicht","Circa 1160 kg")],
  "secties":[("Turbo verandert de aanpak","Bij een atmosferische motor kost elke pk moeite. Bij een turbomotor zit er ruimte in de fabrieksafstemming, waardoor software een grotere rol speelt dan mechanische ingrepen. Dat verlaagt de drempel, maar verhoogt de belasting op koppeling, koeling en aandrijflijn."),
   ("Wat er meestal meegroeit","Wie het vermogen verhoogt, loopt vaak binnen afzienbare tijd tegen de grenzen van de koppeling en de intercooler aan. Die posten horen bij de begroting, niet als verrassing achteraf."),
   ("Bekende aandachtspunten","De THP-motorfamilie staat bekend om koolstofafzetting op de inlaatkleppen en om de distributieketting bij oudere uitvoeringen. Onderhoud vooraf voorkomt problemen achteraf.")],
  "punten":["Software heeft groot effect","Koppeling en koeling groeien mee","Koolstofafzetting is een bekend punt","Moderne elektronica vraagt zorgvuldigheid"]},
 {"slug":"ophanging-en-wegligging","naam":"Ophanging en wegligging","kind":"Onderwerp","b":True,
  "resume":"De ingreep met het grootste effect op rijplezier, en tegelijk de meest onderschatte in complexiteit.",
  "specs":[("Ingreep","Onderstel"),("Effect","Zeer groot"),("Keuring","Vaak relevant"),("Volgorde","Als eerste")],
  "secties":[("Verlagen is geen doel op zich","Een lager zwaartepunt helpt, maar een auto die te ver verlaagd is verliest veerweg en wordt op slecht wegdek onhandelbaar. De veerweg die overblijft bepaalt of de auto grip houdt, niet de hoogte op de foto."),
   ("Dempers boven veren","Bij een dertig jaar oude auto zijn de dempers vrijwel altijd versleten. Nieuwe dempers met de originele veren geven meestal meer verbetering dan een verlagingsset op oude dempers. De combinatie moet bovendien op elkaar afgestemd zijn."),
   ("Bussen en geometrie","Versleten rubberbussen laten de wielgeometrie onder belasting verlopen. Vervangen daarvan, gevolgd door een uitlijning, is een goedkope ingreep met een groot effect op de stabiliteit.")],
  "punten":["Veerweg is belangrijker dan hoogte","Dempers eerst, dan pas veren","Bussen bepalen de geometrie","Uitlijnen hoort er altijd bij"]},
 {"slug":"inlaat-en-uitlaat","naam":"Inlaat en uitlaat","kind":"Onderwerp","b":True,
  "resume":"Luchtstroom in en uit de motor, waar de winst vaak kleiner is dan verwacht en de geluidsregels streng zijn.",
  "specs":[("Ingreep","Luchtstroom"),("Effect","Beperkt tot matig"),("Keuring","Geluidseisen"),("Volgorde","Na basis")],
  "secties":[("Losse filters vallen vaak tegen","Een open filter in de motorruimte zuigt warme lucht aan, wat de vulling verslechtert. Zonder afscherming en een aanvoer van koude lucht levert het geluid op en zelden vermogen. Een goed doorstromend filter in de originele kast presteert vaak beter."),
   ("Uitlaat en tegendruk","Een ruimere uitlaat helpt alleen als de originele daadwerkelijk beperkend is. Bij atmosferische motoren met een matig vermogen is dat vaak niet zo, en verschuift een te ruime uitlaat het koppel naar boven, wat op straat juist hinderlijk is."),
   ("Geluid is een juridische grens","Het toegestane geluidsniveau ligt vast en wordt gecontroleerd. Een uitlaat zonder demping of zonder katalysator maakt een auto niet toegelaten op de openbare weg, ongeacht de technische winst.")],
  "punten":["Koude lucht is bepalender dan het filter","Tegendruk niet zomaar wegnemen","Geluidseisen zijn hard","Katalysator verwijderen is niet toegestaan"]},
 {"slug":"motormanagement","naam":"Motormanagement en software","kind":"Onderwerp","b":True,
  "resume":"Bij moderne motoren zit de grootste winst in de software, met een navenant grotere verantwoordelijkheid.",
  "specs":[("Ingreep","Software"),("Effect","Groot bij turbo"),("Keuring","Emissie-eisen"),("Volgorde","Na hardware")],
  "secties":[("Waarom er ruimte in zit","Fabrikanten stemmen af op wereldwijde brandstofkwaliteit, extreme temperaturen en lange garantietermijnen. Die marges verklaren waarom aanpassingen winst kunnen opleveren, en tegelijk waarom die marges er niet voor niets zijn."),
   ("Volgorde is bepalend","Software afstemmen op hardware die nog moet komen, is dubbel werk. De gebruikelijke volgorde is eerst de mechanische kant op orde brengen, daarna afstemmen op een rollenbank met uitlezing van luchtverhouding en klopgedrag."),
   ("Emissie en registratie","Aanpassingen die de emissie beïnvloeden of onderdelen zoals de roetfilter buiten werking stellen, zijn niet toegestaan en worden bij de keuring vastgesteld. Dat is los van de technische discussie een harde grens.")],
  "punten":["Marges bestaan, maar niet zonder reden","Hardware eerst, software daarna","Rollenbank geeft controle","Emissieonderdelen blijven intact"]},
 {"slug":"remmen","naam":"Remmen","kind":"Onderwerp","b":True,
  "resume":"De ingreep die het minst opvalt en het meest oplevert, zeker bij auto's die op circuit komen.",
  "specs":[("Ingreep","Remsysteem"),("Effect","Groot"),("Keuring","Altijd relevant"),("Volgorde","Vroeg")],
  "secties":[("Groter is niet automatisch beter","Een grotere remschijf verhoogt de warmtecapaciteit, maar zonder passende klauwen, remdrukverdeling en banden verandert de remweg nauwelijks. Bij lichte auto's is het grip van de band vaak eerder de grens dan de remkracht."),
   ("Vloeistof en leidingen","Remvloeistof neemt vocht op en verliest daardoor kookpunt. Bij herhaald hard remmen leidt dat tot een zachte pedaal. Verse vloeistof en stalen leidingen geven een merkbaar vaster pedaalgevoel voor beperkte kosten."),
   ("Blokken passend bij gebruik","Blokken voor circuitgebruik werken pas bij hoge temperatuur en presteren koud juist slechter. Voor een straatauto is dat een verslechtering, geen verbetering.")],
  "punten":["Band is vaak eerder de grens","Verse vloeistof geeft vast pedaal","Stalen leidingen zijn goedkope winst","Blokken kiezen op werkelijk gebruik"]},
]
def item(s): return next(x for x in ITEMS if x["slug"]==s)
MODELLEN=[x for x in ITEMS if x["kind"]=="Model"]
ONDERWERPEN=[x for x in ITEMS if x["kind"]=="Onderwerp"]

GIDSEN=[
 {"slug":"tunen-en-de-rdw","titel":"Tunen en de RDW: wat mag wel en wat niet","ic":"shield",
  "resume":"Modificaties zijn toegestaan binnen grenzen. Die grenzen liggen bij constructie, geluid, verlichting en emissie.",
  "body":[("p","Een auto aanpassen is in Nederland toegestaan, maar niet onbeperkt. De regels draaien om vier gebieden: constructieve veiligheid, geluid, verlichting en emissie. Wie daarbinnen blijft, houdt een auto die de keuring doorstaat en verzekerd blijft."),
   ("h2","Constructieve wijzigingen"),("p","Aanpassingen aan draagconstructie, ophangingspunten of stuurinrichting kunnen keuringsplichtig zijn. Een verlagingsset uit de handel met een goedkeuringsnummer geeft doorgaans minder discussie dan zelfgemaakte oplossingen."),
   ("h2","Geluid"),("ul",["Het geluidsniveau van de uitlaat is aan grenzen gebonden en wordt bij controle gemeten.","Een uitlaat zonder demper of met verwijderde katalysator is niet toegestaan op de openbare weg.","Klepuitlaten die op de weg openstaan vallen onder dezelfde eisen."]),
   ("h2","Verlichting"),("p","Verlichting moet van het juiste type zijn, de juiste kleur hebben en correct afgesteld staan. Xenon- of ledlampen in een koplamp die daar niet voor bedoeld is, geeft verblinding en is een afkeurpunt."),
   ("h2","Emissie"),("p","Het verwijderen of buiten werking stellen van emissieonderdelen is niet toegestaan. Bij de keuring wordt dit vastgesteld, en bij dieselmotoren wordt tegenwoordig ook op deeltjesaantal gemeten."),
   ("warn","Naast de keuring speelt de verzekering. Niet gemelde wijzigingen kunnen bij schade tot problemen met de dekking leiden. Melden vooraf voorkomt discussie achteraf."),
   ("h2","Bij twijfel"),("p","De RDW geeft uitsluitsel over specifieke wijzigingen, en een erkend keuringsstation kan een auto vooraf beoordelen. Dat is goedkoper dan een afkeuring of een discussie na schade.")]},
 {"slug":"beginnen-met-tunen","titel":"Beginnen met tunen: de volgorde die werkt","ic":"wrench",
  "resume":"De meest gemaakte fout is beginnen met vermogen. Onderhoud, remmen en onderstel gaan daaraan vooraf.",
  "body":[("p","Bij een auto van twintig tot veertig jaar oud levert achterstallig onderhoud vrijwel altijd meer op dan een vermogenswinst van een paar procent. Dat is minder spannend, maar het bepaalt hoe de auto rijdt."),
   ("h2","Stap een: de auto op orde"),("p","Distributie, koeling, bougies, filters en vloeistoffen. Een motor die niet gezond is, reageert onvoorspelbaar op elke aanpassing, en een afstemming op een versleten basis is weggegooid geld."),
   ("h2","Stap twee: banden"),("p","Banden zijn de enige verbinding met het wegdek en bepalen zowel remweg als bochtsnelheid. Een set goede banden verandert een lichte auto sterker dan de meeste motorische ingrepen, en kost minder."),
   ("h2","Stap drie: remmen en onderstel"),("ul",["Verse remvloeistof en goede blokken.","Dempers vervangen voordat er veren bij komen.","Versleten bussen vervangen en daarna uitlijnen.","Pas daarna nadenken over verlagen."]),
   ("h2","Stap vier: vermogen"),("p","Met een gezonde basis is duidelijk wat een aanpassing daadwerkelijk oplevert. Zonder die basis is elk resultaat een gok, omdat onduidelijk blijft wat de winst veroorzaakte."),
   ("callout","Een rollenbankmeting vooraf en achteraf maakt het verschil meetbaar. Zonder nulmeting blijft elke claim over vermogenswinst een aanname.")]},
]

ARTIKELEN=[
 {"slug":"rijden-op-curacao","titel":"Rijden op Curaçao: regels, wegdek en de verzekering van een huurauto","cat":"Praktijk","datum":"2026-09-26","datum_nl":"26 september 2026","lees":5,
  "resume":"Rechts rijden en een Nederlands rijbewijs maken de start eenvoudig. Het wegdek, het verkeer buiten Willemstad en de verzekering vragen meer aandacht.",
  "body":[("p","Wie thuis veel met auto's bezig is, kijkt op vakantie met andere ogen naar het verkeer. Op Curaçao valt dan vooral op hoe vertrouwd de basis is en hoe anders de omstandigheden zijn. Er wordt rechts gereden, de borden lijken op wat in Europa gebruikelijk is en een geldig Nederlands rijbewijs is voldoende. De verschillen zitten in het wegdek, in wat er onderweg op de weg kan opduiken en in de manier waarop een huurauto verzekerd is."),
   ("h2","Regels die thuis ook gelden"),("p","De gordel is verplicht voor alle inzittenden, ook op de achterbank. Bellen met de telefoon in de hand is achter het stuur niet toegestaan. Rijbewijs en huurcontract horen tijdens elke rit in de auto te liggen, omdat daar bij een controle naar wordt gevraagd. Kinderen zitten het veiligst in een zitje dat past bij lengte en gewicht; verhuurders kunnen dat meestal leveren als het bij de reservering wordt aangegeven."),
   ("h2","Snelheid, borden en rotondes"),("p","De maximumsnelheden liggen lager dan op Nederlandse wegen en kunnen al na een paar honderd meter wisselen, bijvoorbeeld bij het binnenrijden van een wijk of dorp. Er wordt op snelheid gecontroleerd, ook buiten de stad. Op kruisingen bepalen borden en markeringen wie voorrang heeft, en een stopbord betekent volledig stilstaan, ook als er niemand aankomt. Op de hoofdroutes rond Willemstad liggen veel rotondes. Wie die met lage snelheid nadert en de richtingaanwijzer tijdig gebruikt, voegt zonder moeite in tussen het lokale verkeer."),
   ("h2","Grip op een warm en stoffig wegdek"),("p","Voor wie op weggedrag let, is dit het opvallendste verschil. Het asfalt wordt overdag erg warm en ligt vaak onder een dunne laag zand en stof. Dat geeft minder grip dan het uiterlijk doet vermoeden, vooral in bochten en bij stevig remmen. Valt er na een droge periode een flinke bui, dan komen olie en vuil los en is het wegdek een tijd glad. Soms blijft er ook water op de weg staan."),
   ("p","Buiten de hoofdwegen worden de wegen smaller en heuvelachtiger, met bochten zonder overzicht, kuilen en losse stenen in de berm. De laatste meters naar kleinere baaien zijn vaak onverhard. Met een lage auto gaat dat stapvoets, met aandacht voor de onderkant en de velgen."),
   ("h2","Dieren, schemer en tanken"),("p","Op het platteland steken geiten en honden zonder aankondiging over, vaak net achter een bocht of heuveltop. Het wordt het hele jaar rond zeven uur 's avonds donker en veel landelijke wegen hebben geen verlichting, waardoor fietsers en voetgangers langs de kant laat zichtbaar zijn. Lange ritten naar het westen passen daarom het best overdag. Tankstations liggen vooral rond Willemstad en langs de grote wegen. Richting Westpunt worden ze schaars, dus een dag aan die kant van het eiland begint met een volle tank."),
   ("h2","De verzekering van een huurauto"),("p","Bij een huurauto kijkt een liefhebber al snel naar motor en uitrusting, maar de verzekering bepaalt meer hoe de vakantie verloopt. Op smalle wegen met grind en kuilen is een sterretje in de ruit of een kras op een velg sneller gebeurd dan thuis. Een all-risk verzekering met een beperkt eigen risico vangt dat op."),
   ("ph",'Bij <a href="https://www.autohurenopcuracao.nl/">AutohurenopCuracao.nl</a> rijden jonge, goed onderhouden auto\'s met all-risk verzekering, die op het vliegveld of bij het verblijf kunnen worden afgeleverd. Ook <a href="https://www.huurauto-curacao.com/">Huurauto-Curacao.com</a> verhuurt met all-risk, van compacte auto\'s en kleine SUV\'s tot zevenpersoonsauto\'s.'),
   ("p","Wat een autoliefhebber bij de overname toch altijd doet: de auto rondlopen, het profiel van de banden bekijken, de airconditioning testen en bestaande krassen op het overdrachtsformulier laten zetten. Een paar foto's bij daglicht voorkomen discussie bij het inleveren."),
   ("h2","Vertrouwd rijden met oog voor het eiland"),("p","Rijden op Curaçao vraagt voor Nederlanders weinig gewenning: rechts houden, borden volgen en de snelheid aanpassen. Het verschil zit in de details die een liefhebber herkent. Het wegdek geeft minder grip dan het lijkt, het platteland heeft zijn eigen verkeer en het donker valt vroeg. Wie daar rekening mee houdt, op tijd tankt en kiest voor een huurauto met een goede verzekering, bereikt elke baai en elk uitzichtpunt van het eiland zonder zorgen.")]},
 {"slug":"waarom-lichte-autos-sneller-voelen","titel":"Waarom een lichte auto sneller voelt dan hij is","cat":"Techniek","datum":"2026-07-12","datum_nl":"12 juli 2026","lees":4,
  "resume":"Vermogen per kilo verklaart maar een deel. Massatraagheid bepaalt hoe direct een auto reageert.",
  "body":[("p","Een 205 GTI met honderd pk voelt levendiger dan een moderne auto met twee keer zoveel vermogen. Het cijfer op papier verklaart dat niet volledig."),
   ("h2","Vermogen per kilo"),("p","De eerste verklaring is rekenkundig: minder massa per pk betekent snellere acceleratie. Bij ruim achthonderd kilo weegt elke pk zwaarder mee dan bij een auto van anderhalve ton."),
   ("h2","Traagheid bij richtingverandering"),("p","Belangrijker voor het gevoel is hoe snel een auto van richting verandert. Massa moet bij elke stuurbeweging versneld en afgeremd worden. Een lichte auto reageert daardoor directer, ook bij dezelfde bochtsnelheid."),
   ("h2","Wat isolatie doet"),("p","Moderne auto's zijn zwaarder door veiligheid en comfort, maar ook stiller en stabieler. Die stilte dempt de indruk van snelheid. Een auto zonder isolatie geeft meer prikkels bij dezelfde snelheid.")]},
 {"slug":"onderdelen-voor-oude-modellen","titel":"Onderdelen voor oude modellen: waar het schuurt","cat":"Praktijk","datum":"2026-06-24","datum_nl":"24 juni 2026","lees":4,
  "resume":"Voor sommige modellen is vrijwel alles leverbaar, voor andere loopt het spaak op één specifiek onderdeel.",
  "body":[("p","De beschikbaarheid van onderdelen bepaalt in de praktijk of een project vlot verloopt of maanden stil komt te liggen."),
   ("h2","Slijtdelen zijn zelden het probleem"),("p","Remmen, filters, distributie en ophangingsdelen worden voor de populaire modellen nog steeds gemaakt, deels door onafhankelijke fabrikanten. Daar zit de vertraging meestal niet."),
   ("h2","Waar het wel misgaat"),("ul",["Modelspecifiek plaatwerk en bumpers.","Interieurdelen en bekleding in de originele stof.","Elektronica en instrumenten.","Ruiten en rubbers voor kleine oplages."]),
   ("h2","Donorauto's"),("p","Voor onderdelen die niet meer gemaakt worden, is een donorauto vaak de enige route. Dat verklaart waarom complete maar afgeschreven exemplaren nog steeds gevraagd zijn."),
   ("h2","Vooraf inventariseren"),("p","Nagaan wat er leverbaar is voordat een project begint, voorkomt de situatie waarin een auto uit elkaar ligt in afwachting van één onvindbaar onderdeel.")]},
]

def tile(s):
    return f"""<a class="tile{' b' if s['b'] else ''}" href="/kennisbank/{s['slug']}/"><span class="tt"></span>
  <span class="tb"><span class="kind">{esc(s['kind'])}</span><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:92].rsplit(' ',1)[0])}...</p></span></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijk kennisplatform over het modificeren van Peugeot-modellen, met aandacht voor techniek en regelgeving."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    mod="".join(tile(s) for s in MODELLEN[:3]); ond="".join(tile(s) for s in ONDERWERPEN)
    gids="".join(f'<div class="card{" blue" if g["ic"]=="shield" else ""}"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("Peugeot Tuning Club | kennisplatform over Peugeot-tuning",
      "Onafhankelijk kennisplatform over het modificeren van Peugeot-modellen. Techniek per model, onderwerpen als ophanging en remmen, en de regels van de RDW.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['car']}Kennisplatform</span>
  <h1>Peugeot tunen, <em>met kennis van zaken</em></h1>
  <p class="lead">Techniek per model, uitleg per onderwerp en duidelijkheid over wat de RDW toestaat. Geen onderdelenverkoop, geen loze vermogensclaims.</p>
  <div class="hero-actions"><a class="btn btn-orange" href="/kennisbank/">Naar de kennisbank {IC['arrow']}</a><a class="btn btn-ghost-l" href="/gidsen/tunen-en-de-rdw/">Wat mag wel en niet</a></div>
  <div class="hero-meta"><span>{IC['check']}5 modellen</span><span>{IC['check']}4 onderwerpen</span><span>{IC['check']}Regelgeving apart behandeld</span></div></div>
  <div class="hero-art"><img src="/assets/img/hero-auto.svg" alt="Illustratie van een verlaagde hatchback" width="500" height="340"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['car']}Modellen</span><h2>Per model bekeken</h2>
  <p class="lead">Wat een model kenmerkt, waar de slijtage zit en wat de verstandige eerste stappen zijn.</p></div>
  <div class="grid cols-3">{mod}</div>
  <p style="margin-top:22px"><a class="more" href="/kennisbank/">Alle modellen {IC['arrow']}</a></p></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['wrench']}Onderwerpen</span><h2>Waar de winst werkelijk zit</h2>
  <p class="lead">Ophanging, luchtstroom, software en remmen, met de volgorde die in de praktijk het beste werkt.</p></div>
  <div class="grid cols-2">{ond}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Regels en aanpak</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['gauge']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Iets aan te vullen?</h2><p>Ervaringen met een model, een correctie of een onderwerp dat ontbreekt: de redactie leest mee.</p>
  <a class="btn btn-orange" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_kb():
    path="/kennisbank/"; c=[("Home","/"),("Kennisbank",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Kennisbank","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/kennisbank/{s['slug']}/"} for i,s in enumerate(ITEMS)]},crumb(c)]
    h=head("Kennisbank | modellen en onderwerpen | "+SITE,"Alle modellen en technische onderwerpen op een rij, met specificaties, aandachtspunten en praktische volgorde.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Kennisbank</span><h1>Modellen en onderwerpen</h1>
  <p class="lead">Vijf modellen en vier technische onderwerpen, elk met de punten die in de praktijk het verschil maken.</p></div>
  <h2 style="margin-bottom:18px">Modellen</h2><div class="grid cols-3">{"".join(tile(s) for s in MODELLEN)}</div>
  <h2 style="margin:38px 0 18px">Onderwerpen</h2><div class="grid cols-2">{"".join(tile(s) for s in ONDERWERPEN)}</div>
</div></section>"""
    write(path,h+footer())

def p_item(s):
    path=f"/kennisbank/{s['slug']}/"; c=[("Home","/"),("Kennisbank","/kennisbank/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in ITEMS if x["slug"]!=s["slug"] and x["kind"]==s["kind"]][:3]
    h=head(f"{s['naam']} | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose">
  <span class="eyebrow">{IC['wrench'] if s['b'] else IC['car']}{esc(s['kind'])}</span><h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}
  <h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:18px">{pt}</ul>
  <div class="warn"><p><strong>Let op de regelgeving.</strong> {esc(RDW)}</p></div>
  {byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Verder in de kennisbank</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | regels en aanpak | "+SITE,"Gidsen over de regels van de RDW bij modificaties en over de volgorde waarin tunen in de praktijk werkt.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h1>Gidsen</h1>
  <p class="lead">Twee onderwerpen die los staan van een specifiek model: wat is toegestaan, en in welke volgorde loont het.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over techniek en praktijk | "+SITE,"Artikelen over de techniek achter tunen en over de praktijk van sleutelen aan oudere modellen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['gauge']}Nieuws</span><h1>Artikelen</h1>
  <p class="lead">Achtergrond bij wat er in de werkplaats en op de weg gebeurt.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['gauge']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over Peugeot Tuning Club | wat dit platform is | "+SITE,
      "Peugeot Tuning Club is een onafhankelijk kennisplatform over het modificeren van Peugeot-modellen, zonder verkoop en zonder band met de fabrikant.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een kennisplatform, geen werkplaats</h1>
  <p class="lead">Peugeot Tuning Club verzamelt technische kennis over het aanpassen van Peugeot-modellen, met evenveel aandacht voor wat er mag als voor wat er kan.</p>
  <h2>Waarom dit platform bestaat</h2>
  <p>Informatie over tunen ligt verspreid over forums, video's en verkooppagina's, en loopt door elkaar met marketing. Wat ontbreekt is een plek waar techniek, praktijk en regelgeving naast elkaar staan, zonder dat er iets verkocht hoeft te worden.</p>
  <h2>Regelgeving hoort erbij</h2>
  <p>Een aanpassing die technisch werkt maar niet door de keuring komt, is geen oplossing. Daarom staat bij elk onderwerp waar de grenzen liggen op het gebied van constructie, geluid, verlichting en emissie.</p>
  <div class="callout"><p><strong>Geen band met de fabrikant.</strong> Dit platform is onafhankelijk en heeft geen relatie met Peugeot of Stellantis. Modelnamen worden uitsluitend gebruikt om te beschrijven waar een artikel over gaat.</p></div>
  <h2>Wat hier niet gebeurt</h2>
  <p>Er worden geen onderdelen verkocht, geen werkzaamheden uitgevoerd en geen vermogenscijfers geclaimd die niet onderbouwd zijn. Aanpassingen die de auto onveilig of niet toegelaten maken, worden niet beschreven als optie.</p>
  <h2>Correcties</h2>
  <p>Wie een fout ziet of praktijkervaring wil delen die iets aanvult, kan dat melden. Onderbouwde correcties worden verwerkt.</p>
  <p style="margin-top:16px"><a class="btn btn-dark" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/kennisbank/">Naar de kennisbank</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#bas","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de kennisbank en de gidsen van Peugeot Tuning Club.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['wrench']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Bas schrijft de kennisbank, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Uit de werkplaats</h2>
  <p>Bas werkte jaren als monteur bij een onafhankelijk garagebedrijf, waar geregeld auto's binnenkwamen met aanpassingen die op papier veelbelovend waren en in de praktijk vooral problemen gaven. Die combinatie van techniek en praktijk vormt de basis van dit platform.</p>
  <h2>Nuchter over vermogen</h2>
  <p>Rond tunen circuleren veel getallen die niemand heeft gemeten. Op deze site staan geen vermogenswinsten die niet te onderbouwen zijn, en waar een claim onzeker is wordt dat vermeld.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto. Dat past bij een site waar de techniek centraal staat.</p>
  <h2>Contact</h2>
  <p>Correcties, aanvullingen en vragen komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of aanvulling voor Peugeot Tuning Club? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:700">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een technische correctie, met onderbouwing.</li><li>Praktijkervaring met een model of aanpassing.</li><li>Een onderwerp dat nog ontbreekt in de kennisbank.</li></ul>
  <h2>Waar niet</h2>
  <p>Dit platform verkoopt geen onderdelen, voert geen werkzaamheden uit en geeft geen keuringsadvies voor een specifieke auto. Voor dat laatste zijn de RDW en een erkend keuringsstation de aangewezen weg.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>Peugeot Tuning Club is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend de gegevens die in dat bericht staan, en die worden alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. De kennisbank is een goed vertrekpunt.</p>
  <p><a class="btn btn-orange" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/kennisbank/">Naar de kennisbank</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/kennisbank/","/gidsen/","/nieuws/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/kennisbank/{s['slug']}/" for s in ITEMS]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.peugeottuningclub.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_kb()
    for s in ITEMS: p_item(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
