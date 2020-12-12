import discord 

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt")
        
    #Wenn meine Nachricht gepostet wird 
    async def on_message(self, message):
        print ("Nachricht von " + str(message.author) + " enthält " + str(message.content)
              
 client = MyClient()
 client.run("0KX_oE1i9T_GQe_m8CKh88OTImlU3PuR")
