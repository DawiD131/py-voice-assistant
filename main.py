from scripts import recognize_command
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def on_recognition():
    print("Cmd recognized")

async def main():
    while True:
        task = asyncio.create_task(recognize_command(on_recognition))
        await task 
        
if __name__ == "__main__":
     asyncio.run(main())
