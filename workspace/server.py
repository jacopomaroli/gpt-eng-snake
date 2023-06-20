import asyncio
import json
import websockets
from game import Game

async def game_loop(game):
    while True:
        game.update()
        if game.winner != None:
            break
        await asyncio.sleep(0.1)

async def handle_player(websocket, path, game):
    player_index = len(game.players)
    game.players.append(None)
    await websocket.send(json.dumps({"playerIndex": player_index}))
    async for message in websocket:
        game.players[player_index].move(message)

async def handle_game(websocket, path, game):
    while True:
        await websocket.send(json.dumps(game.__dict__))
        await asyncio.sleep(0.1)

async def main():
    game = Game()
    game.start()
    game_loop_task = asyncio.create_task(game_loop(game))
    async with websockets.serve(lambda websocket, path: handle_player(websocket, path, game), "localhost", 8000):
        await asyncio.gather(game_loop_task)
    game.end()

asyncio.run(main())
