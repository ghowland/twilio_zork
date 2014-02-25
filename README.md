## Twilio-Zork

Really basic implementation of a Zork-type text based adventure game based on Twilio's text-to-speech.

This is meant to plug into my DropSTAR Python webserver, so if you want to run it you'll need to port it to an equivalent system.

## Data Example

```
west_of_house:
  name: West of House.
  info: You are standing in an open field west of a white house, with a boarded front door.  There is a small mailbox here.

  options:
    8:
      room: south_of_house
    
    2:
      room: north_of_house
    
    4:
      room: forest_west_of_house
    
    6:
      error: The door is boarded and you can't remove the boards.

forest_west_of_house:
  name: Forest
  info: This is a forest, with trees in all directions.  To the east, there appears to be sunlight.

  options:
    6:
      room: west_of_house
    
    4:
      error: You would need a machete to go further west.  You hear in the distance the chirping of a song bird.
    
    2:
      error: You would need a machete to go further north.  You hear in the distance the chirping of a song bird.
    
    8:
      error: You would need a machete to go further south.  You hear in the distance the chirping of a song bird.
  
```
