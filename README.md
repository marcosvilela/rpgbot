# RPGBot 
A simple dice-roller bot for Discord, based on a original RPG system created by Gabriel Bione Berçot. 

# Combat rules
## Attack test
The attacking player rolls a d20 and adds their Precision modifier to the result using the $rollatk command.
The deffending player (or master) rolls a d20 and adds their Agility modifier to the result using the $rolldef command.
If $rollatk >= $rolldef, the Attack succeeds and damage is calculated.
If $rollatk < $rolldef, the Attack fails and the turn ends.
## Damage calculation
After the attack succeeds, the player rolls a d20 and adds their Strength or Wisdom modifiers (Strength for physical attacks, Wisdom for magical attacks) using the $rolldmg command. The result is then subtracted by the attacked player's Constitution attribute to yield the total damage.

