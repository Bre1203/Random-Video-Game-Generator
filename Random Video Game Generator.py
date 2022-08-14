import random
print("What video game do you want to play today?")

video_game_list={
"Horror game":["Outlast","Layers of Fear","Amnesia:Rebirth","Outlast 2","The evil within"],
"Action game":["Uncharted 4","Last of us","Grand theft Auto 5","Assassin's Creed Syndicate","Last of us 2"],
"Multiplayer game":["Call of duty:Warzone","Fortnight","Destiny 2","Rocket League","Apex Legends","Fall Guys"],
"Sandbox game":["Minecraft","Rust","Astroneer","The Sims 4","Terraria","No Man's Sky","Cities:Skylines"]}


category = random.choice(list(video_game_list.keys()))
game = random.choice(video_game_list[category])

if category == "Action game":
    print("You will play an " + category)
    print("called "+ game)
else:
  print("You will play a " + category)
  print("called " + game)
