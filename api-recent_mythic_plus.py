#!/usr/bin/python3

import discord

from discord.ext import commands,tasks
import requests
import json
import os

parameters = {
    "name": "ezalum",
    "region": "us",
    "realm": "barthilas",
}

response = requests.get("https://raider.io/api/v1/characters/profile", params=parameters)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())



