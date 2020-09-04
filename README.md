# pygame-main-loop-intro

## Intro

Many beginners struggle with displaying varying player graphics and animation in Pygame. 
Purpose of this guide is to help you understand Pygame's event-driven structure and write a better main loop.

Displaying a temporary player animation (firing a gun, walking a direction) is often something beginners implement by running an entire animation inside the event-handling code. If the spacebar key triggers fire, then the fire animation is shown inside the event-handler for the space key.
This is not the correct way, since it locks up the entire program until that animation is done.
To handle this properly we need to understand the role of the main loop, and how to work event-driven.

## Main loop

The *main loop* or *main rendering loop* is used to run your Pygame program in a way suitable for displaying graphics. 
Each round through the main loop displays 1 frame of graphics. It is your priority as a developer to not interfere with this loop, like slowing it down with heavy calculations or to go on sidetracks with alternative loops inside.

A proper main loop (in my opinion) should be divided into separate stages or phases with different responsibilities:

### Stages

1. handle events
2. run game logic
3. display graphics

#### handle events

- Stage inputs: events from pygame
- Stage outputs: changes to game state variables

This stage turns keyboard events (and other events) into changes to your state variables. You need to invent variables as you need them, for example: game state (is start screen or "playing" screen shown), player state (walking, shooting, idle etc), moving direction, a time or a frame count. These variables are used to send information into subsequent stages.


#### run game logic

- Stage inputs: game state variables
- Stage outputs: changes to game state variables

This stage is used for general calculations. It can be based on different kinds of state: 

- state you setup before the main loop
- state depending on keyboard or mouse input
- state based on previous round through the main loop

The output of the stage should be to prepare everything you need to redisplay the graphics for this frame.


#### display graphics

- Stage inputs: game state variables
- Stage outputs: updated graphics on screen

The final stage is where we take all prepared state variables needed and update the graphics on screen using pygame. Everything should be pre-calculated in the logic stage as far as possible.
