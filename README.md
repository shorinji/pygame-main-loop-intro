# pygame-main-loop-intro

## Intro

Many beginners struggle with displaying varying player graphics and animation in Pygame. 
Purpose of this guide is to help you understand Pygame's event-driven structure and write a better main loop.

Displaying a temporary player animation (firing a gun, walking a direction) is often something beginners implement by running an entire animation inside the event-handling code. If the spacebar key triggers fire, then the fire animation is shown inside the event-handler for the space key.
This is not the correct way, since it locks up the entire program until that animation is done.
To handle this properly we need to understand the role of the main loop, and how to work event-driven.

## Main loop

The main loop or main rendering loop is used to run your Pygame program in a way suitable for displaying graphics. 
Each round through the main loop displays 1 frame of graphics. It is your priority as a developer to not interfere with this loop, like slowing it down with heavy calculations or to go on sidetracks with alternative loops inside.

A proper main loop (in my opinion) should be divided into separate stages or phases with different responsibilities:

### Stages

1. handle events
2. run game logic
3. display graphics

#### handle events

Stage inputs: events from pygame
Stage outputs: changes to game state variables

#### run game logic

Stage inputs: game state variables
Stage outputs: changes to game state variables

#### display graphics

Stage inputs: game state variables
Stage outputs: updated graphics on screen

