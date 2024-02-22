from asyncio import sleep
from datetime import datetime, timezone
from glob import glob

import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File, DMChannel
from discord import Intents
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,
								  CommandOnCooldown)
from discord.ext.commands import when_mentioned_or, command, has_permissions
from dotenv import load_dotenv

OWNER_IDS = [238039924178157568]
COGS = [path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)

load_dotenv(dotenv_path="/app/.env")

class Bot(BotBase):
	def __init__(self):
		self.ready = False
		self.guild = None
		self.TOKEN=os.environ['BOT_TOKEN']
		self.scheduler = AsyncIOScheduler(timezone="Europe/Paris")

		super().__init__(owner_ids=OWNER_IDS, intents=Intents().all(),help_command=None)

		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"Loading cog : {cog}")

	def run(self, version):
		self.VERSION = version
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("Connected to Discord. Not ready to receive commands.")
		await self.register_commands()

	async def on_disconnect(self):
		print("Disconnected")

	async def on_ready(self):
		if not self.ready:
			self.guild = self.get_guild(os.environ["SERVER_ID"])
			self.scheduler.start()
			self.ready = True
			print("Now ready to receive commands")

		else:
			print("The bot has reconnected")

bot = Bot()