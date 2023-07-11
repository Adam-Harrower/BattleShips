# Battle Ships 

## Battle ships is a Python terminal game of chance, Which runs using Code Institues mock terminal Heroku.
* Users try to blow up the computers battle ships before all their ammo all runs out.
* Each battle ship occupies one sqaure on the baord.

### Here is a liver version of my game.
![battleship screen](https://github.com/Adam-Harrower/my-full-template/assets/125028133/77f23330-16a7-44c9-89eb-8b82881dffb1)

## How to play.
* Battle ships is a baord game usually played between two players, In this version, it is a one player game playing agaisnt the computer. 
* The player first guesses a row to target and then a column. 
* Ships hit are marked with a X and a miss is marked with a ~ on the board.
* The player has ten shots to shoot all the battle ships before the game ends. 

## Features
* Random board generation.
* Ships are randomly placed on the board by the computer.
* The player connot see the ships location on the board.

![battleship screen1](https://github.com/Adam-Harrower/my-full-template/assets/125028133/ba60fd8a-c15d-44af-94d9-65519d976851)

* 

![battleship screen2](https://github.com/Adam-Harrower/my-full-template/assets/125028133/1361ad1e-f306-49ff-b8d0-367dbf52b78f)

* Input validation and error checking.
* You cannot outside of the row or column.
* You must start with the row number before the column letter.
* You cannot target the same area twice.


![battleship screen3](https://github.com/Adam-Harrower/my-full-template/assets/125028133/85a2044b-5a2e-4bf4-8f67-7bee635987d2)

## Testing
* I have manually tested the game usning the following:
* I have tested the game on the terminal within Gitpod.
* Given invalid inputs, Letters for rows instead of numbers and vise versa to check for error messages.
* I have targeted the same area on the board more than once to check for error messages.
* I have depolyed to the Heroku terminal.

## Bugs 
* The game runs fine on the terminal but not on the Heruko terminal. 
* I dont know how to fix that issue.

## Deployment 
* Steps for deployment.
* Crete new Heruko app.
* Set the buildpacks to python and NodeJS in the correct order.
* Linked Heroku to the correct Gitpod repository.
* Clicked on Deploy.

## Credits 
* Code Institue for the depolyment terminal. 

