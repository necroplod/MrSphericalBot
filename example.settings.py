class channels:
    welcome = 0
    bugs = 0
    suggest = [0, 0]
    todo = 0
    art_id = 0
    archive_art_id = 0
    logs = 0
    punishments_name = 0
    art = 0
    mod_notify = 0
    archive_art = 0
    mod_chat = 0
    tickets = '〔🎯〕───・Тикеты・─────┐'
    tickets_count = 0
    wilds = 0
    proof = 0
    ticket_notify = 0
    tech_ticket = 0
    appeal_notify = 0
    recruit = 0
    event_logs = 0
class stats:
    all = 0
    members = 0
    bots = 0
    boosts = 0
    status = 0

    all_rp = 0
    members_rp = 0
class roles:
    manage_tickets = 1071141626866569286
    mods_tickets = 1071505429462519938
    poll_role = 997425510265135145
    senior_mod = 1102550171948154900
    mute = 1090003567793938442
class logs:
    msg = 0
    role = 0
    ticket = 0
    welcome = 0
    server = 0
class misc:
    ticketdb = 0
    guild = 0
    dev = 0
    tickets_count = 0
    avatar_url = 'https://cdn.discordapp.com/avatars/959849629321666560/79e05274a4a0059dd2dd0c46a7370b21.webp?size=1024'
    footer = 'Мистер Сферический | Все права защищены'
class openai:
    key = "pk-XXXXXXX"
    url = "https://api.openai.com/v1"
class extensions:
    cogs = [
        'cogs.adm',
        'cogs.dev',
        'cogs.info',
        'cogs.suggest',
        'cogs.welcome',
        'cogs.ticket',
        'cogs.stats',
        'cogs.role',
        'cogs.rp',
        'cogs.theme',
        'cogs.events'
    ]
    handlers = [
        'handlers.error',
        'handlers.logs'
    ]
