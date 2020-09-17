# hasukoRPG
A discord bot to manage custom RPG. Python 3.8

# Flags
* `-d` or `--debug` Use to turn of the debug mode
* `-t` or `--token` Specify the discord bot token
* `-u` or `--user Specify the user to the database
* `-p` or `--password` Specify the password to the database
* `-n` or `--db-name` Specify the database name

# Discord Commands
* `MG!new_character` ( ARGS: @USERTAG ) - use this to create a new character and store it in the database
* `MG!show_character` ( ARGS: @USERTAG ) - use this to get a character from the database
* `MG!delete_character` ( ARGS: @USERTAG ) - use this to delete a character from the database
* `MG!edit_character` ( ARGS: @USERTAG, field ) - use this to edit a provided field 
* `MG!character_field` ( ARGS: @USERTAG field ) - use this to get a provided field 
* `MG!check_money` ( ARGS: none ) - use this to check your money
* `MG!earn_money` ( ARGS: none ) - use this to earn some amount of money. You can do it only 1 time per hour.

## Fields
- [x] name
- [x] surname
- [x] age
- [x] sex
- [x] sexual_orientation
- [x] super_power
- [x] personality
- [x] appearance
- [x] history
- [x] gold
