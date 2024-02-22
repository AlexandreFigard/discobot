from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
import os 


class Welcome(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.channel = os.getenv('WELCOME_CHANNEL_ID')

	@Cog.listener()
	async def on_member_join(self, member):
		await self.bot.get_channel(self.channel).send(f"Bienvenue sur **{member.guild.name}** {member.mention}!")

	@Cog.listener()
	async def on_member_remove(self, member):
		await self.bot.get_channel(self.channel).send(f"{member.display_name} a abandonné le navire !")


def setup(bot):
	bot.add_cog(Welcome(bot))
