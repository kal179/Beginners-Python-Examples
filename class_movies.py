

class movie:

	def __init__ ( self, title, director, rating, budget, box_office, cast, description ):
		self.title = title
		self.director = director
		self.rating = rating
		self.budget = budget
		self.box_office = box_office
		self.cast = cast
		self.description = description

	def view_all( self ):
		print( "Title : {}".format( self.title ) )
		print( "Director : {}".format( self.director ) )
		print( "Rating : {}".format( self.rating ) )
		print( "Budget : {} million USD".format( self.budget ) )
		print( "Box office : {} million USD".format( self.box_office ) )
		print( "Cast : {}".format( self.cast ) )
		print( "Description : {}".format( self.description ) )
		print(" ")	

	def comment_movie( self ):
		
		if self.rating >= 4:
			return( "It is a must watch movie.\n" )
		
		elif 4 > self.rating > 2:
			return( "It is a good movie.\n" )
		
		else:
			return( "It is a poor movie.\n" )	

movies = {}

def add():
	get_title = str(input( "Title of movie : " ))
	get_director = str(input( "Director of movie : " ))
	get_rating = float(input( "Rating of movie : " ))
	get_budget = float(input( "Budget of the movie : " ))
	get_box_office = float(input( "Box office earnings of the movie : " ))
	get_cast = str(input( "Cast of the movie : " ))
	get_description = str(input( "Description of the movie : " ))

	movies[get_title] = movie( get_title, get_director, get_rating, get_budget,  get_box_office, get_cast, get_description )

def view_movie():
	which_movie = str(input( "Movie : " ))
	if which_movie not in movies:
		return( "Movie Not in list!" )
	else:
		print( movies[which_movie].view_all() )
		print( movies[which_movie].comment_movie() )

print("Hello,")
while ( True ):			
	print(" ")
	start_or_end = str(input( "Start or End : " ))
	if ( start_or_end.strip() == "Start" ):
		
		op = str(input( "Add or View : " ))

		if op.strip() == "Add":
			print(" ")
			print( add() )
		
		elif op.strip() == "View":
			print(" ")
			print( view_movie() )
		
		else:
			print(" ")
			print( "Invalid Input Try again!" )
			continue

		continue	
	
	elif ( start_or_end == "End" ):				
		break

	else:
		print( "Invalid Input.Try Again!" )	
		continue


