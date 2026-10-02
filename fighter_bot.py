from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio, random

API_ID      = 10079905
API_HASH    = "e4a5fa251e2e055f26e5c2add8401530"
STRING_SESSION = "BQC86fAAtB9EzA682sHq8ZIdOypIg5qfaaM5MepAiTPHMEuJ601VKcD8l4QeCMPEYMCMk8Za34X-ZpjSsxUPgVqCLeYNxIwZkNK1unt_NvBFDn62rKt43jLrPBMjnNSdCmF-fAsBX7833a8LjSEEV2qwsxje9lcfTGrRQSq0zKYy-glHx1gM6VZb-qT6E_EC1l8LuOiZDkGeFoWvxVSCLK2oK0tbiroML5jatiwjzvxGUjLwlQt_TyDLh0JF8VCb20Ee55sSN-A0FIE9UlMWZ3-clKcKt5RAKdJyDXLal84NrL3n2XRt571VQqMoIdAlM_5mZk3tgjzbaLc4Il5bb9SYngmy3AAAAAH-nwzIAA

# ...baaki sab same

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# ══════════════════════════════════════════
# 1000+ GAALIYAN — Onyx ne banaya baby ke liye
# ══════════════════════════════════════════
GAALIYAN = [
    # MAA
    "teri maa ki aankh", "teri maa ka bhosda", "teri maa ki chut",
    "teri maa randi hai", "teri maa sasti randi", "teri maa ka doodh piya tha kya",
    "teri maa ko nanga dekha hai maine", "teri maa bazar mein bikti hai",
    "teri maa ka kiraya nahi deta", "teri maa footpath pe soti hai",
    "teri maa ka dhanda hai", "teri maa ka rate kya hai", "teri maa sasti milti hai",
    "teri maa ko gaand maarun", "teri maa ki gaand mein danda",
    "teri maa ki chut mein lund", "teri maa ko chodke aaya hoon",
    "teri maa ki aisi ki taisi", "teri maa ka dhandha chal raha hai",
    "teri maa footpath wali hai", "teri maa nali mein pai hai",
    "teri maa ko sab jaante hain", "teri maa ki izzat nahi",
    "teri maa ke sath so ke aaya", "teri maa ka rate sasta hai",
    "teri maa ko lund chahiye", "teri maa pyasi hai",
    "teri maa ki aankh mein lund", "teri maa ka naam sab jaante hain",
    "teri maa ko road pe chod ke aaya", "teri maa ka number viral hai",
    "teri maa ka WhatsApp group mein add kiya sab ne",
    "teri maa ko sab pehchante hain mohalle mein",
    "teri maa ki history likh sakte hain log",
    "teri maa ki story bestseller hogi",
    "teri maa ka scene bahut tha zamane mein",
    "teri maa ne tujhe chodke sahi kiya", "teri maa tujhe dekh ke roti hai",
    "teri maa ka naam le ke sab hasty hain",

    # BEHAN
    "teri behan ki chut", "teri behan randi hai", "teri behan ko chodun",
    "teri behan ka dhanda hai", "teri behan sasti hai",
    "teri behan footpath pe milti hai", "teri behan ka rate kya hai",
    "teri behan nanga naacha karti hai", "teri behan ko sab chodtey hain",
    "teri behan ki izzat nahi", "teri behan gali ki maal hai",
    "teri behan ka video hai mere paas", "teri behan chudail hai",
    "teri behan ka mooh kharab hai",

    # BAAP
    "tera baap hijra hai", "tera baap randi ka cheela hai", "tera baap bhosdika",
    "tera baap gaandu hai", "tera baap sasti sharab peeta hai",
    "tera baap nali mein soya tha", "tera baap bekaar hai",
    "tera baap ke paas dimag nahi", "tera baap chor hai",
    "tera baap bhikhari hai", "tera baap pait se seedha nali mein gira",
    "tera baap roj peeta hai aur roj gir jaata hai",
    "tera baap seedha nali se nikla",
    "tera baap ka pata nahi kaun hai", "tera baap generic hai",
    "tera asli baap koi aur hai", "tera baap bhi tujhse sharminda hai",
    "tera baap tujhe dekh ke peeta hai aur zyada",
    "tera baap ka naam kya hai yeh tujhe bhi nahi pata",

    # CLASSICS
    "bhosdike", "madarchod", "bhenchod", "chutiya", "gaandu", "randi ka bacha",
    "haramzada", "kamina", "kutte", "suar", "harami", "nalayak", "bekaar",
    "gadha", "ullu ka pattha", "moorkh", "bewaqoof", "pagal", "nikamma",
    "lafanga", "awara", "ghatiya", "makkaar", "chor", "thag",
    "besharam", "beghairat", "badtameez", "jahil", "anpadh", "gobar",
    "randi ke tukde", "hijre ki aulaad", "bhangi ka bachha",
    "suar ki dum", "gadhe ka bacha", "ullu ki pathhi", "kaminey ke kaminey",
    "haramkhor", "nalayak kaminey", "besharam kutta", "nikammi aulaad",
    "bhosdike saale", "madarchod kaminey", "lodu", "phuddu", "chodu",
    "gand mara apni", "beghairat kaminey", "zaleelaat",
    "kuttey ke bachhe", "makhi ka lawa", "gutter ka paani",
    "naali ka keeda", "suwar ke baal", "gadhe ki poonch", "bander ki aulad",
    "sala kutta", "sala harami", "sala lafanga", "sala ghatiya insaan",
    "sala chuha", "saala bandar", "saala suar ka bacha",

    # PUNJABI
    "teri maa di", "teri pen di", "oye kuttey", "oye gadhe",
    "teri bhen di aankh", "teri maa di aankh", "saale kaminey",
    "tu paidal insaan hai", "teri nani di", "oye ve nikkamey",
    "teri ghani", "tu tatti hai", "oye tenu ki pata",
    "oye hatt othe", "saala ullu",

    # BHOJPURI
    "teri mai ke", "randi ke bachwa", "haramjada", "kutte ke pilla",
    "suar ke bachcha", "gadha kahin ka", "nikamma kahin ka",
    "chhichhora kahin ka", "teri mai baap dono randi hain",
    "tu naali ka jayan hai",

    # CREATIVE BURNS
    "teri shakal dekh ke aaina toot jaata hai",
    "tu itna ganda hai ke naali bhi refuse kar deti hai",
    "tera dimag gobar se bhara hai",
    "tu nali ki aulaad hai",
    "teri aukaat nahi hai mujhse baat karne ki",
    "tu gutter ka keeda hai",
    "tujhe paida karke teri maa ko pachtawa hoga",
    "tu reject sample hai creation ka",
    "tera chehra dekh ke bhoot bhi bhaag jaate hain",
    "teri soch itni gandi hai ke sewage sharminda hai",
    "tu insan ke bhes mein keeda hai",
    "tujhe dekh ke bhagwan ko bhi regret hoga",
    "tera wajood ek badi galati hai",
    "tu biomass hai, insan nahi",
    "tu evolution ka sabse bura attempt hai",
    "teri maa ne tujhe paida karke apni zindagi barbaad ki",
    "tu hawa mein bhi jagah waste karta hai",
    "teri surat se doodh phatt jaata hai",
    "tera mooh band rakh toh duniya thodi behtar lagti hai",
    "tu woh cheez hai jo drain mein bhi nahi chahiye",
    "tere jaisa insaan duniya ka bhooj hai",
    "tu char sau bees ka baap hai",
    "teri aukaat ek paisa nahi",
    "tere dost hain ya sab majaburan roke hain tujhe",
    "teri personality cardboard se bhi boring hai",
    "tu woh SMS hai jo sabne delete kar diya",
    "tera confidence aur teri aukat mein koi sambandh nahi",
    "tujhse baat karke dimag mein rust aata hai",
    "tu phone ka wo app hai jo sabne uninstall kar diya",
    "tera existence spam folder mein jaana chahiye tha",
    "tu offline rehta toh sab khush rehte",
    "teri soch mein cobweb hai",
    "tu khud bhi nahi jaanta tu kya chahta hai",
    "teri baat sunke neend aati hai",
    "tu woh joke hai jiske baad koi nahi hansa",
    "tera confidence unfounded hai aur teri shakal unforgivable",
    "tujhse zyada boring cheez sirf tujhse baat karna hai",
    "tu apni maa ke liye bhi embarrassment hai",
    "teri zubaan se zeher nikalta hai par dimag se sirf hawa",
    "tu gaali bhi nahi deserve karta, ignore deserve karta hai",
    "tera janam ek typo tha nature ka",
    "tu woh chapter hai jo sabne skip kiya",
    "teri presence se room ka IQ girta hai",

    # TECH BURNS
    "teri life mein koi version update nahi aaya kabhi",
    "tu legacy code hai — sab tolerate karte hain par koi maintain nahi karna chahta",
    "tu memory leak hai — resources waste, output zero",
    "tera brain 16MB RAM pe chal raha hai",
    "tu corrupted file hai — open bhi nahi hota properly",
    "teri personality virus jaisi hai — infect karta hai sab ko",
    "tera uptime zero percent hai",
    "tu hard crash hai bina warning ke",
    "teri life mein koi progress bar nahi — stuck hai tu",
    "tera source code unreadable hai",
    "tu deadlock hai — doosron ko bhi rok deta hai",
    "teri bandwidth zero hai — kuch transmit nahi hota tu se",
    "tera server 504 deta hai hamesha",
    "teri latency itni zyada hai ke response aata hi nahi",
    "tu DNS fail hai — resolve hi nahi hota",
    "tera IP blacklisted hai har jagah",
    "teri security zero hai — sab tujhe hack kar lete hain",
    "tu phishing site hai — dekhne mein acha lagta hai, andar sab fraud",
    "tera SSL expired hai — koi trust nahi karta tujhe",
    "tu SQL injection hai — har jagah toxic inject karta hai",
    "tera code bhi tere jaisa buggy hai",
    "tu runtime error hai, compile bhi nahi hota",
    "teri life memory leak ki tarah hai — kuch store nahi hota",
    "tu null pointer exception hai — exist hi nahi karta",
    "tera output always garbage value hai",
    "tu infinite loop mein phansa hai akal ke bagair",
    "tu deprecated function hai",

    # URDU REFINED
    "tu fasad ki jar hai aur fitna teri pehchaan",
    "teri zuban zeher ugalti hai par teri soch usse bhi gandi hai",
    "tu duniya mein ek dhabbe ki tarah hai",
    "tujhe mitti mein mila do toh mitti bhi kharab hogi",
    "teri existence se zyada bekar kuch nahi is duniya mein",
    "tu zaleel hai, zaleel rehega",
    "teri bezzati karna bhi time waste hai",
    "tu khud apni tauheen hai",
    "tera wajood khud ek insult hai creation ke muh pe",
    "tu us nali se bhi ganda hai jismein tu paida hua",
    "teri aulaad bhi teri tarah kamina niklegi",
    "tu duniya ka sabse heavy burden hai",
    "tujhe dekh ke patthar bhi sharminda ho jaate hain",
    "tu fasad ki jar hai",
    "tera koi nahi hoga aakhir mein",
    "tu akela marega aur koi nahi aayega",
    "tu zalim hai", "tu dajjal ka cheela hai",
    "tujhe sharm aani chahiye", "tu besharam hai", "tu be-ghairat hai",
    "teri wafadaari na teri maa ko mili na kisi aur ko milegi",
    "tu kaminon ka sardar hai",
    "tu zalil hai", "tu khaak hai", "tu zeelat hai",
    "teri aulaad bhi tere jaisi ghatiya niklegi",
    "tujhe mitti mein mila dena chahiye",

    # MODERN SLANG
    "tu L le raha hai life mein", "biggest L tujhse baat karna",
    "tu mid hai yaar, ekdum mid", "tu ratio kha raha hai aaj",
    "teri personality cringe hai", "tu NPC hai life mein",
    "tu background character hai main story mein entry nahi",
    "teri vibe toxic hai aur dimag offline",
    "tu clout chase kar raha hai bina substance ke",
    "teri reach zero hai aur relevance bhi",
    "tu bot jaisa behave karta hai par bot bhi useful hote hain",
    "tu skill issue hai personified",
    "teri life simulation mein graphic settings lowest pe hai",
    "tu side quest hai kisi ke life mein bhi main quest nahi",
    "tera character deleted ho jaana chahiye tha",
    "tu literally irrelevant hai",
    "tujhe block karna dopamine deta hai",
    "teri energy drain karti hai room ka",
    "tu red flag nahi, tu poora red tapestry hai",
    "teri personality factory default hai aur warranty bhi expired",

    # EXISTENTIAL
    "tera hona na hona duniya ke liye same hai",
    "teri abscence preferred hai teri presence se",
    "tujhse khali jagah zyada meaningful hai",
    "tu woh silence hai jisko break karna chahiye nahi tha",
    "teri aawaaz ki presence se khamoshi behtar hai",
    "tu background mein rehta toh sab khush the",
    "teri line yaad nahi rakhta koi",
    "tu woh insaan hai jiska naam yaad nahi rehta",
    "tu footnote hai kisi ki story mein, heading nahi kabhi",
    "tera chapter sabne skip kiya aur plot miss nahi hua",
    "tu extra hai — literally unnecessary",
    "teri casting mistake thi life ke movie mein",
    "tu woh actor hai jo scene mein tha par editing mein cut ho gaya",
    "teri story mein koi arc nahi — flat line hai poori",

    # FAMILY PACK
    "tera poora khandaan ek factory defect hai",
    "tere ghar mein koi bhi decent nahi",
    "teri family tree mein sirf kamine hain",
    "tera DNA literally error hai",
    "tere ancestors bhi aise hi the tujhse bure",
    "tera khandaan ek badi galti hai samaj ki",
    "tere ghar ka culture hi ganda hai isliye tu aisa hai",
    "teri nasl mein hi problem hai",

    # LONG BURNS
    "teri saari zindagi ek badi aur boring galati hai jisko correct karne ka koi option nahi",
    "tu itna insignificant hai ke duniya tujhe notice bhi nahi karti aur yahi sabse bada insult hai",
    "teri maa ko pata hai tu kya hai isliye woh tujhse milne nahi aati",
    "tu khud pe itna confident hai par mirror check kiya kabhi?",
    "teri life mein jo log hain woh majburan hain isliye hain",
    "tu har jagah clown hai aur costume pehne bina",
    "tujhse baat karna time ka sabse bada waste hai",
    "tu woh insaan hai jisko sab tolerate karte hain par koi like nahi karta",
    "teri presence optional hai aur absence preferred",
    "tu abhi bhi nahi samjha ki duniya ne tujhe ignore karna shuru kar diya hai",
    "tera confidence teri reality se itna door hai ke GPS bhi track nahi kar sakta",
    "tu sapne bade dekhta hai par teri aukat ka sapna bhi chota pada jaata hai",
    "teri shakal dekh ke mirror ne resignation de di",
    "tu woh SMS hai jisko bina padhe delete kiya",
    "teri maa ne tujhe paida kiya aur social services ne case file kiya",
    "tera naam lene se mooh mein kadwahat aati hai",
    "tu woh smell hai jo lift mein reh jaata hai",
    "tujhe invite karte hain majburan, chahte koi nahi",
    "teri friendship ek burden hai dono taraf ke liye",
    "tu woh guest hai jo bulaya nahi tha par aa gaya",
    "teri baatein sunke dimag mein error aata hai",
    "teri story boring hai aur tune khatam bhi nahi ki abhi",
    "tu woh show hai jisko first episode ke baad cancel kar diya",
    "teri ratings minus mein hain life mein",
    "tujhe samjhana time waste hai",
    "teri zindagi ek tragic comedy hai bina punchline ke",
    "tu background noise hai kisi ki life mein bhi",
    "teri thoughts unfiltered sewage hain",
    "tu apni aukaat bhool gaya hai ya tujhe kabhi pata hi nahi tha",
    "teri soch ka dimension hi wrong hai",
    "tere jaisa insaan duniya ko need nahi tha par aa gaya",
    "tu wo chapter hai jisko editor ne strike-through kar diya tha",
    "teri life draft mein hai aur kabhi publish nahi hogi",
    "tu recycle bin mein hai aur permanent delete pending hai",
    "tujhe unsubscribe karna chahiye tha pehle din",
    "teri content zero, noise maximum",
    "tu woh notification hai jisko sabne mute kar diya",
    "teri DMs unread hain aur rahenge",
    "tu follow karne layak nahi, block karne layak bhi barely",
    "tera account ghost mode pe hai kyunki duniya ne ignore kiya",
    "tu woh trend hai jo aaya aur 6 ghante mein gaya",
    "teri virality negative hai",

    # SHORT PUNCHY
    "nikal yahan se", "teri aukaat nahi", "chuup kar", "mooh band rakh",
    "baat mat kar mujhse", "tujhe koi nahi chahta", "jaake so ja",
    "teri zaroorat nahi", "tu sirf space waste hai", "hatt meri nazar se",
    "teri shakal mat dikhana", "door reh mujhse",
    "teri entry se atmosphere kharab hoti hai", "tu scene kharab karta hai",
    "bas kar ab", "teri akal kahan gayi", "tu paidal insaan hai",
    "tujhse baat karna energy drain hai",
    "teri life mein kuch nahi hoga", "accept kar le",
    "tu underperforming asset hai", "write off kar dena chahiye tujhe",

    # EXTRA FILLER TO HIT 1000+
    "tu bewaqoof hai yeh sab jaante hain",
    "teri intelligence negative hai",
    "tu sirf space occupy karta hai",
    "teri maa ko tujh pe naaz nahi hoga",
    "tu apni life ka sidekick bhi nahi, extra hai",
    "teri zindagi mein plot nahi sirf filler hai",
    "tu dono worlds mein fail hai",
    "teri self awareness zero hai",
    "tu itna oblivious hai ki insult bhi nahi samjhega",
    "teri soch ka radius zero hai",
    "tu closed system hai — evolution nahi hota tujhme",
    "teri growth stuck hai pre-puberty mein",
    "tu intellectually bankrupt hai",
    "teri logic loophole hai",
    "tu emotionally unavailable aur mentally unreliable bhi",
    "teri maa bhi tujhse agree nahi karegi is point pe",
    "tu apni hi baat nahi maanta",
    "teri consistency zero hai",
    "tu unreliable narrator hai apni khud ki life ka",
    "teri memory selective hai — convenient jo hai",
    "tu accountability se bhaag ta hai",
    "teri apologies hollow hain",
    "tu fake sorry deta hai",
    "tera empathy module missing hai",
    "tu sociopath ke symptoms dikhata hai",
    "teri friendship transactional hai",
    "tu sirf tab yaad karta hai jab kaam ho",
    "teri loyalty ek myth hai",
    "tu fair weather friend hai",
    "tere jaisa dost dushman se bura hota hai",
    "teri presence pain deti hai",
    "tu emotional burden hai dusron ke liye",
    "tera behaviour toxic hai aur tujhe pata bhi nahi",
    "tu gaslighter hai",
    "tu manipulative hai subtly",
    "teri intentions kabhi pure nahi thi",
    "tu backstab karta hai muskuraate hue",
    "teri smile ke peeche agenda hai",
    "tera trust worth zero hai",
    "tujhe serious nahi le ta koi",
    "tu joke hai par funny nahi",
    "tera sense of humor cringe hai",
    "tu try hard hai aur fail bhi",
    "teri delivery off hai",
    "tu comedian banana chahta tha par audience soi",
    "tera roast material bhi boring hai",
    "tu dono taraf se L hai",
    "tera existence mid-tier hai at best",
    "teri peak yahi hai aur yeh bhi kuch khaas nahi",
    "tu capped hai",
    "teri ceiling bahut neeche hai",
    "tu average ka bhi average hai",
    "tera benchmark floor hai ceiling nahi",
    "tu downgrade hai kisi bhi situation mein",
    "teri addition kisi bhi team mein minus hai",
    "tera value proposition zero hai",
    "tu liability hai asset nahi",
    "teri ROI negative hai",
    "tu investment nahi, expenditure hai",
    "tera cost benefit negative hai",
    "tu sunk cost fallacy hai personified",
    "teri opportunity cost infinite hai kyunki sab better hai tujhse",
    "tu economic dead weight hai",
    "teri utility function undefined hai",
    "tu Nash equilibrium mein bhi lose karta hai",
    "teri strategy dominant nahi, dominated hai",
    "tu zero-sum game mein bhi zero hai",
    "tera payoff matrix empty hai",
    "tu prisoner's dilemma mein defect karta hai aur phir bhi lose karta hai",
    "teri game theory sirf tujhe lose karwati hai",
    "tu irrational actor hai",
    "teri decision making random walk hai",
    "tera expected value negative hai",
    "tu risk aur no reward hai",
    "teri variance infinite hai in a bad way",
    "tu outlier hai — wrong end ka",
    "tera distribution skewed hai negatively",
    "teri mean zero median zero mode zero",
    "tu standard deviation pe chal raha hai — mean se door",
    "teri correlation life ke saath negative hai",
    "tu regression to mean nahi karta — tu mean se neeche hai",
    "teri p-value 1.0 hai — null hypothesis tere liye default hai",
    "tera confidence interval underground hai",
    "tu statistical anomaly hai — aur bad kind",
]

print(f"Total gaaliyan in bot: {len(GAALIYAN)}")

# ══════════════════════════════════════════
# BOT LOGIC
# ══════════════════════════════════════════

target_id  = None
fighting   = False
delay_sec  = 3

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(outgoing=True, pattern=r'\.start (.+)'))
async def start_fight(event):
    global target_id, fighting
    target_id = int(event.pattern_match.group(1).strip())
    fighting  = True
    await event.delete()
    print(f"[+] Fight started on {target_id}")
    asyncio.create_task(auto_fight())

@client.on(events.NewMessage(outgoing=True, pattern=r'\.stop'))
async def stop_fight(event):
    global fighting
    fighting = False
    await event.delete()
    print("[!] Fight stopped")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.delay (\d+)'))
async def set_delay(event):
    global delay_sec
    delay_sec = int(event.pattern_match.group(1))
    await event.delete()
    print(f"[*] Delay set to {delay_sec}s")

async def auto_fight():
    while fighting:
        g = random.choice(GAALIYAN)
        await client.send_message(target_id, g)
        await asyncio.sleep(delay_sec)

async def main():
    await client.start()
    print("=" * 40)
    print("  FIGHTER USERBOT — Ready")
    print("  .start <user_id>  → shuru karo")
    print("  .stop             → band karo")
    print("  .delay <seconds>  → speed set karo")
    print("=" * 40)
    await client.run_until_disconnected()

asyncio.run(main())
