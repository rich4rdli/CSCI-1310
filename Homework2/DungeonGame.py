print ("Welcome to Richard's dungeon!")
location = "kitchen"
direction = "a"
while (direction != "q"): 
	  
	if location == "kitchen":
		direction = input("You are in the kitchen. There are doors to the west (w), south (s), and east (e).")
		if direction == "w":
			location = "hallway"
		elif direction == "s":
		    location = "furnace"
		elif direction == "e":
			location = "living room"
		else:
			location = "kitchen"
			    
	elif location == "living room":
		direction = input("You are in the living room. There is a door to the west (w).")
		if direction == "w":
			location = "kitchen"
		else:
			location = "living room"
				
	elif location == "furnace":
		print("You entered the furnace and fried yourself to death!")
		direction = "q"
	
	elif location == "hallway":
		direction = input("You are in the hallway. There are doors to the south (s), north (n) and east (e).")
		if direction == "s":
			location = "library"
		elif direction == "e":
			location = "kitchen"
		elif direction == "n":
			location = "garden"
		else:
			location = "hallway"
	
	elif location == "library":
		print("You are in the library. You found the princess! You are a hero!")
		direction = "q"
			
	elif location == "labyrinth":
		direction = input("You are in the labyrinth. There are doors to the east (e) and down (d).")
		if direction == "d":
			location = "oubliette"
		elif direction == "e":
			location = "garden"
		else:
			location = "labyrinth"
			
	elif location == "oubliette":
		direction = input("You are in the oubliette. The dungeon master chains you and slowly tortures you to death.")
		direction = "q"
		
	elif location == "garden":
		direction = input("You are in the garden. There are doors to the west (w) and south (s).")
		if direction == "s":
			location = "hallway"
		elif direction == "w":
			location = "labyrinth"
		else:
			location = "garden"
		
	else:
		print()
		
print("Goodbye!")		
	
	
			        
			 
		
