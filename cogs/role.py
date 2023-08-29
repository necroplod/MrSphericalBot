import discord
import settings
from discord.ext import commands

class CountrySelectAdd(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Россиянин", emoji="🇷🇺", description="Россия"),
            discord.SelectOption(label="Белорус", emoji="🇧🇾", description="Беларусь"),
            discord.SelectOption(label="Украинец", emoji="🇺🇦", description="Украина"),
            discord.SelectOption(label="Казахстанец", emoji="🇰🇿", description="Казахстан"),
            discord.SelectOption(label="СНГ", emoji="🏴", description="СНГ"),
            discord.SelectOption(label="Европеец", emoji="🇪🇺", description="Европа"),
        ]
        super().__init__(placeholder="Добавить роль", max_values=1, min_values=0, options=options, custom_id = 'role:countryadd')

    async def callback(self, interaction: discord.Interaction):
        ru = interaction.guild.get_role(997425518460817470)
        by = interaction.guild.get_role(1142936988723462144)
        ua = interaction.guild.get_role(997425520675397682)
        kz = interaction.guild.get_role(997425521736568842)
        eu = interaction.guild.get_role(1109087511592058960)
        cis = interaction.guild.get_role(1109087164219789314)
        roles = interaction.user.roles

        def check(r):
            listt = [ru, by, ua, kz, cis, eu]
            listt.remove(r)
            for rr in listt:
                if rr in roles:
                    return False
            return True
        async def process(rolee):
            if rolee not in roles:
                await interaction.user.add_roles(rolee)
                return True


        if self.values[0] == "Россиянин": give = ru
        if self.values[0] == "Белорус": give = by
        if self.values[0] == "Украинец": give = ua
        if self.values[0] == "Казахстанец": give = kz
        if self.values[0] == "СНГ": give = cis
        if self.values[0] == "Европеец": give = eu

        if check(give):
            if await process(give):
                await interaction.response.send_message(f'*Роль <@&{give.id}> успешно выдана!*', ephemeral = True)
        if check(give) is False:
            await interaction.response.send_message(f'*У Вас уже есть одна из ролей стран!\nУберите ее и повторите попытку.*', ephemeral = True)

class CountrySelectRemove(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Россиянин", emoji="🇷🇺", description="Россия"),
            discord.SelectOption(label="Белорус", emoji="🇧🇾", description="Беларусь"),
            discord.SelectOption(label="Украинец", emoji="🇺🇦", description="Украина"),
            discord.SelectOption(label="Казахстанец", emoji="🇰🇿", description="Казахстан"),
            discord.SelectOption(label="СНГ", emoji="🏴", description="СНГ"),
            discord.SelectOption(label="Европеец", emoji="🇪🇺", description="Европа"),
        ]
        super().__init__(placeholder="Убрать роль", max_values=1, min_values=0, options=options, custom_id = 'role:countryremove')

    async def callback(self, interaction: discord.Interaction):
        ru = interaction.guild.get_role(997425518460817470)
        by = interaction.guild.get_role(1142936988723462144)
        ua = interaction.guild.get_role(997425520675397682)
        kz = interaction.guild.get_role(997425521736568842)
        eu = interaction.guild.get_role(1109087511592058960)
        cis = interaction.guild.get_role(1109087164219789314)
        roles = interaction.user.roles

        def check():
            listt = [ru, by, ua, kz, cis, eu]
            for rr in listt:
                if rr in roles:
                    return True
            return False
        async def process(rolee):
            if rolee in roles:
                await interaction.user.remove_roles(rolee)
                return False


        if self.values[0] == "Россиянин": give = ru
        if self.values[0] == "Белорус": give = by
        if self.values[0] == "Украинец": give = ua
        if self.values[0] == "Казахстанец": give = kz
        if self.values[0] == "СНГ": give = cis
        if self.values[0] == "Европеец": give = eu

        if check() and await process(give) is False:
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно убрана!*', ephemeral = True)
        if check() is False:
            await interaction.response.send_message(f'*У Вас нет ни одной роли!*', ephemeral = True)

class AccessSelectAdd(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Нюхай космос", emoji="🌌", description="Что стоишь? Нюхай!"),
            discord.SelectOption(label="Дискуссии", emoji="💢", description="Ладно."),
        ]
        super().__init__(placeholder="Добавить роль", max_values=1, min_values=0, options=options, custom_id = 'role:accessadd')

    async def callback(self, interaction: discord.Interaction):
        dis = interaction.guild.get_role(997425508608397312)
        space = interaction.guild.get_role(1046403300435697754)
        roles = interaction.user.roles

        def check(rr):
            if rr in roles:
                return True
            return False
        async def process(rolee):
            if rolee not in roles:
                await interaction.user.add_roles(rolee)
                return True


        if self.values[0] == "Нюхай космос": give = space
        if self.values[0] == "Дискуссии": give = dis

        if await process(give) and check(give) is False:
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно выдана!*', ephemeral = True)
        if check(give):
            await interaction.response.send_message(f'*Роль уже выдана!*', ephemeral = True)

class AccessSelectRemove(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Нюхай космос", emoji="🌌", description="Что стоишь? Нюхай!"),
            discord.SelectOption(label="Дискуссии", emoji="💢", description="Ладно."),
        ]
        super().__init__(placeholder="Убрать роль", max_values=1, min_values=0, options=options, custom_id = 'role:accessremove')

    async def callback(self, interaction: discord.Interaction):
        dis = interaction.guild.get_role(997425508608397312)
        space = interaction.guild.get_role(1046403300435697754)
        roles = interaction.user.roles

        def check(rr):
            if rr in roles:
                return True
            return False
        async def process(rolee):
            if rolee in roles:
                await interaction.user.remove_roles(rolee)
                return False


        if self.values[0] == "Нюхай космос": give = space
        if self.values[0] == "Дискуссии": give = dis

        if check(give) and await process(give) is False:
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно убрана!*', ephemeral = True)
        if check(give) is False:
            await interaction.response.send_message(f'*У Вас нет ни одной ролм!*', ephemeral = True)

class GenderSelectAdd(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Парень", emoji="👦", description="Парень, не более."),
            discord.SelectOption(label="Девушка", emoji="👧", description="Ладно."),
        ]
        super().__init__(placeholder="Добавить роль", max_values=1, min_values=0, options=options, custom_id = 'role:genderadd')

    async def callback(self, interaction: discord.Interaction):
        man = interaction.guild.get_role(997425535263191100)
        woman = interaction.guild.get_role(997425536190132265)
        roles = interaction.user.roles

        def check():
            listt = [man, woman]
            for rr in listt:
                if rr in roles:
                    return True
            return False

        if self.values[0] == "Парень": give = man
        if self.values[0] == "Девушка": give = woman

        if give not in roles and check() is False:
            await interaction.user.add_roles(give)
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно выдана!*', ephemeral=True)
        if check():
            await interaction.response.send_message(f'*Возможно получить только одну роль!*', ephemeral=True)

class NotifySelectAdd(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Подписчик", emoji="🔔", description="Уведомления о выходе видосов"),
            discord.SelectOption(label="Новости", emoji="📰", description="Новости сервера"),
            discord.SelectOption(label="Опросы", emoji="📊", description="Опросы и голосования"),
            discord.SelectOption(label="Оживляй чат, лол", emoji="🐒", description="Особенная роль"),
            discord.SelectOption(label="Ивенты", emoji="🎈", description="Ивенты")
        ]
        super().__init__(placeholder="Добавить роль", max_values=1, min_values=0, options=options, custom_id = 'role:notifyadd')

    async def callback(self, interaction: discord.Interaction):
        sub = interaction.guild.get_role(997425507836645506)
        news = interaction.guild.get_role(997425506960015410)
        poll = interaction.guild.get_role(997425510265135145)
        deadchat = interaction.guild.get_role(997425504485384253)
        event = interaction.guild.get_role(1146028746680311839)
        roles = interaction.user.roles

        def check(rr):
            if rr in roles:
                return True
            return False
        async def process(rolee):
            if rolee not in roles:
                await interaction.user.add_roles(rolee)
                return True


        if self.values[0] == "Подписчик": give = sub
        if self.values[0] == "Новости": give = news
        if self.values[0] == "Опросы": give = poll
        if self.values[0] == "Оживляй чат, лол": give = deadchat
        if self.values[0] == "Ивенты": give = event


        if await process(give) and check(give) is False:
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно выдана!*', ephemeral = True)
        if check(give):
            await interaction.response.send_message(f'*Роль уже выдана!*', ephemeral = True)

class NotifySelectRemove(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Подписчик", emoji="🔔", description="Уведомления о выходе видосов"),
            discord.SelectOption(label="Новости", emoji="📰", description="Новости сервера"),
            discord.SelectOption(label="Опросы", emoji="📊", description="Опросы и голосования"),
            discord.SelectOption(label="Оживляй чат, лол", emoji="🐒", description="Особенная роль"),
            discord.SelectOption(label="Ивенты", emoji="🎈", description="Ивенты")
        ]
        super().__init__(placeholder="Убрать роль", max_values=1, min_values=0, options=options, custom_id = 'role:notifyremove')

    async def callback(self, interaction: discord.Interaction):
        sub = interaction.guild.get_role(997425507836645506)
        news = interaction.guild.get_role(997425506960015410)
        poll = interaction.guild.get_role(997425510265135145)
        deadchat = interaction.guild.get_role(997425504485384253)
        event = interaction.guild.get_role(1146028746680311839)
        roles = interaction.user.roles

        def check(rr):
            if rr in roles:
                return True
            return False
        async def process(rolee):
            if rolee in roles:
                await interaction.user.remove_roles(rolee)
                return True


        if self.values[0] == "Подписчик": give = sub
        if self.values[0] == "Новости": give = news
        if self.values[0] == "Опросы": give = poll
        if self.values[0] == "Оживляй чат, лол": give = deadchat
        if self.values[0] == "Ивенты": give = event

        if check(give) and await process(give):
            await interaction.response.send_message(f'*Роль <@&{give.id}> успешно убрана!*', ephemeral = True)
        if check(give) is False:
            await interaction.response.send_message(f'*У Вас нет данной роли!*', ephemeral = True)

class CountryView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CountrySelectAdd())
        self.add_item(CountrySelectRemove())

class AccessView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(AccessSelectAdd())
        self.add_item(AccessSelectRemove())

class NotifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(NotifySelectAdd())
        self.add_item(NotifySelectRemove())

class GenderView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(GenderSelectAdd())

class role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def role(self, ctx):
        country = discord.Embed(
            title = "・▬▬▬ Откуда вы? ▬▬▬・",
            description = "<a:1041076662546219168:1041076662546219168> :flag_ru: — <@&997425518460817470>\n<a:1041076662546219168:1041076662546219168> :flag_ua: — <@&997425520675397682>\n<a:1041076662546219168:1041076662546219168> :flag_by: — <@&1142936988723462144>\n<a:1041076662546219168:1041076662546219168> :flag_kz: — <@&997425521736568842>\n<a:1041076662546219168:1041076662546219168> :flag_black: — <@&1109087164219789314>\n<a:1041076662546219168:1041076662546219168> :flag_eu: — <@&1109087511592058960>",
            color = 0xdd8d03
        )
        access = discord.Embed(
            title = "・▬▬▬ Роли Доступа ▬▬▬・",
            description = "<a:1041076662546219168:1041076662546219168> 🔭 — <@&1046403300435697754> — Доступ к <#1046391794977480704>\n<a:1041076662546219168:1041076662546219168> 🗯 — <@&997425508608397312> — Дискуссии.",
            color = 0xdd8d03
        )
        notify = discord.Embed(
            title = "・▬▬▬ Уведомления ▬▬▬・",
            description = '<a:1041076662546219168:1041076662546219168> :bell: — <@&997425507836645506> — Уведомление о новых видео\n<a:1041076662546219168:1041076662546219168> :newspaper: — <@&997425506960015410> — Новости сервера\n<a:1041076662546219168:1041076662546219168> :bar_chart: — <@&997425510265135145> — Опросы и голосования\n<a:1041076662546219168:1041076662546219168> :monkey: — <@&997425504485384253> —  Особенная роль. Единственная из автовыдаваемых ролей, изменяющая цвет. Вы берете эту роль на свой страх и риск!\n<a:1041076662546219168:1041076662546219168> :balloon: — <@&1146028746680311839> — Уведомления о новых ивентах.',
            color = 0xdd8d03
        )
        gender = discord.Embed(
            title = "・▬▬▬ Пол ▬▬▬・",
            description = "<a:1041076662546219168:1041076662546219168> :boy: — <@&997425535263191100>\n<a:1041076662546219168:1041076662546219168> :girl: — <@&997425536190132265>",
            color = 0xdd8d03
        )
        country.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        access.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        notify.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        gender.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)

        await ctx.send(embed = country, view = CountryView())
        await ctx.send(embed = access, view = AccessView())
        await ctx.send(embed = notify, view = NotifyView())
        await ctx.send(embed = gender, view = GenderView())


async def setup(client):
    await client.add_cog(role(client))