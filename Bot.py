import discord 

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt")
        
    #Wenn meine Nachricht gepostet wird 
