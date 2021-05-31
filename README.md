# hack-cade-2021
Snake V2.0  
password is ~~59vff36vfb~~ changed on linode so not anymore haha  

Devpost: <https://devpost.com/software/snake-2-0>  
Demo: <https://youtu.be/lVMGMdsv19Q> - /ipfs/Qmds73tTMB4wzW71fPVKYrCf3YzsXCSjEbgMTuxypZqUmM (might not be up on ipfs btw but just putting it here for future proofing)

## Categories 
- Linode Cloud - IRC Server Hosting
- Video Game Remix

## Inspiration
Knowing we could modernize an old classic game, our minds immediately went to Snake. Everyone has played Snake and we've been playing it since we were kids. With this history and experience with the game, we came up with Snake 2.0.
## What it does
Snake 2.0 has all the classic elements of Snake: the fruit, the snake growing and dying after hitting yourself. But we added an element of competition. Now for each game, there are two snakes, and each player tries to get their opponent to die so that they can win the game.
## How we built it
We first started making the classic snake game in Pygame. Then to implement the multiplayer aspect, we set up sending messages to an IRC channel for each game. This way we can share the data between the applications and create multiplayer. Every time the player moves their snake, it transmits that information to the other game which updates with the new information.
## Challenges we ran into
As with any worthwhile task, it was difficult and there were many challenges. One of the primary challenges was setting up the collision to detect whether a player hit their body with their head. According to the original game, the player should die when this happened, and we wanted to implement that. However, we had difficulty when lengthening the snake it activated the collision and killed the player. Another difficulty we had was syncing both of the games and reducing lag. There was a lot of information that needs to be shared between the applications to make it run smoothly and to allow for proper multiplayer. It was difficult to synchronize the sharing of data so that the same movement was happening on both screens
## Accomplishments that we're proud of
There were many accomplishments that made us proud throughout the project but one of the many accomplishments was when we were finally able to sync both games so that the players were truly playing each other simultaneously. It was a monumental accomplishment and was the most important part of our project.
## What we learned
We learned a lot about communication between programs and learned about using a communications protocol in a custom application. We gained a lot of experience in debugging and the protocols used to communicate between programs.
## What's next for Snake 2.0
There are many updates we are looking forward to doing such as adding a time constraint, power-ups, and more. There is a lot of potential for adding more features with such an open-concept game.
