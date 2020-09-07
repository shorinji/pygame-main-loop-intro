# pygame-main-loop-intro

## Intro

Many beginners struggle with displaying dynamic player graphics and animation in Pygame. 
Purpose of this guide is to help understand Pygame's event-driven structure and helps on write a better main loop.

Displaying a temporary player animation (firing a gun, walking a direction) is often something beginners implement by running an entire animation inside the event-handling code. If the spacebar key triggers fire, then the fire animation is displayed inside the event-handler for the space key.
This is not the correct way, since it locks up the entire program until that animation is done.
To handle this properly we need to understand the role of the main loop, and how to keep it running smoothly.

## Main loop

The *main loop* or *main rendering loop* is used to run your Pygame program in a way suitable for displaying graphics. 
Each round through the main loop displays 1 frame of graphics. It is your priority as a developer to not interfere with this loop, like slowing it down with heavy calculations or to go on sidetracks with alternative loops inside.

A proper main loop (in my opinion) should be divided into separate stages or phases with different responsibilities.

### Stages

1. Handle events
2. Run game logic
3. Display graphics

#### Handle events

- Stage inputs: events from pygame
- Stage outputs: changes to game state variables

This stage turns keyboard events (and other events) into changes to your state variables. You need to invent variables as you need them. For example: view state (is start screen or playing screen shown), player state (walking, shooting, idle etc), moving direction (up, down etc), a timer or a frame count. These variables are used to send information into subsequent stages. Your event handler should go through all events currently queued up. This can be done by iterating over *pygame.event.get()* and only acting on events you are interested in.


#### Run game logic

- Stage inputs: game state variables
- Stage outputs: changes to game state variables

This stage is used for general calculations. It can be based on different kinds of state like

- state you setup before the main loop
- state depending on keyboard or mouse input
- state based on previous round through the main loop
- state read from pygame

The output of this stage should be to prepare everything you need to display the next frame of graphics


#### Display graphics

- Stage inputs: game state variables
- Stage outputs: updated graphics on screen

The final stage is where we take all prepared state variables we need and update the graphics on screen using pygame calls. It is good to pre-calculate everything as far as possible.

### Discussion

As you might notice the stages each have clear role, but the lines between them can be fuzzy. Perhaps your code will be much simpler if you decide to have certain logic inside the event handling (special keyboard handling for menus compared to normal play). Perhaps you would like to display graphics as step 1, handle events as step 2, and run logic as step 3. The order is not set in stone. What I have described is what makes the most sense to me. 

Look me up in the Facebook Pygame group if you have comments on this setup. 
