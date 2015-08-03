# name: Andrea Furikova
# email: afurikova@yahoo.fr

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures"

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    network = dict(dict(list()))
    split_text = []
    if string_input == "": # returns an empty network if there is an empty string input
        return network
    
    for sentence in string_input[:-1].split("."):
        # cration of a split list with connections and liked games in sublist
        if sentence.find("connected to") != -1: # search for connections
            position = sentence.find("connected to")
            connections = sentence[position + 13:].split(", ")
            split_text.append(sentence[:position + 13].split() + [connections])           
        elif sentence.find("play") != -1: # search for liked games
            position = sentence.find("play")
            games = sentence[position + 5:].split(", ")
            split_text.append(sentence[:position + 5].split() + [games])
        
    for phrase in split_text:
        # cration of data structure
        name = phrase[0]
        if name not in network:
            network[name] = {"links":[], "played_games":[]}
        if "connected" in phrase: # adding connections to a sublist in a dictionary of the network
            connection = phrase[-1]
            network[phrase[0]]["links"] = connection
        if "play" in phrase: # adding liked games to a sublist in a dictionary of the network
            games = phrase[-1]
            network[name]["played_games"] = games    
    return network

#network = create_data_structure(example_input)
#print network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    if user not in network: # if the user not found 
        return
    if "links" not in network[user]: #if no connections found
        return []
    return network[user]["links"]
  

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user not in network: # if the user not found
        return
    if "played_games" not in network[user]: # if no games found
        return []
    return network[user]["played_games"]


# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

# verification if both users in network structure
def verify_users(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    return True

def add_connection(network, user_A, user_B):
    if not verify_users(network, user_A, user_B): # returns False if one of the users given as an argument not found
        return False
    if user_B in get_connections(network, user_A): # adding a new connection if not yet in the list or returns unchanged network
        return network
    network[user_A]["links"].append(user_B)
    return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user in network:
        # user found in the network structure
        return network
    network[user] = {"links": [], "played_games": games} # adding new contact
    return network


# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_union(alist, element):
    # elimination of doubled elements in a list
    if element not in alist:
        return alist.append(element)
    return alist            
    
def get_secondary_connections(network, user):
    list_of_connex = []
    if user not in network: # user not found
        return None
    if network[user]["links"] == []: # no connections found
        return []
    for connection in network[user]["links"]: # find all secondary connections in user's connections
        sublist = network[connection]["links"]
        if sublist != []: # put the secondary connection in a list if there is any
            for sec_connection in sublist:
                get_union(list_of_connex, sec_connection)
    return list_of_connex


# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    common_connex = 0
    list1, list2 = get_connections(network, user_A), get_connections(network, user_B)

    if not verify_users(network, user_A, user_B): # returns False if one of the users given as an argument not found
        return False    
    for user1 in list1:
        # searching for common users
        for user2 in list2:
            if user1 == user2:
                common_connex = common_connex + 1 # adding 1 if common connection found
        
    return common_connex

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def path_to_friend(network, user_A, user_B):
    if isinstance(user_A,str):
        # creating a list of user_A in order to keep nodes
        path = [user_A]
    else:
        path = user_A    
    last_user = path[-1]
    nodes = path[0:-1] # nodes to be checked with the last_user
    
    if not verify_users(network, last_user, user_B): # returns False if one of the users given as an argument not found
        return   
    if last_user in nodes:      
        # search for a duplication nodes in order to prevent never ending cycle
        return
    if user_B in network[last_user]["links"]:
        return path + [user_B]   
    if network[last_user]["links"] == []:
        return
    
    for user in network[last_user]["links"]:
        future_path = path_to_friend(network, path + [user], user_B)
        if future_path:
            return future_path
    return
	
    # your RECURSIVE solution here!

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

def MYOP():
    network = create_data_structure(example_input) # creation of a network structure
    network2 = create_data_structure('') # creatiion of a network structure with an empty string input
    print network
    print network2
    
    
    print get_connections(network, "Mercedes") == ['Walter', 'Robin', 'Bryant'] # find existing user
    print get_connections(network, "Viki") == None # user not in database
    
    print get_games_liked(network, "Olive") == ['The Legend of Corgi', 'Starfleet Commander'] # user and games found in database
    print get_games_liked(network, "Steve") == None # user not in database
    
    add_connection(network, "Ollie", "John") # adding a new connection
    add_connection(network, "Mercedes", "Jirka") # one of the user does not exist
    add_connection(network, "Mercedes", "Walter") # connection already exists
    print network
    
    add_new_user(network,'Benda',['Call of Duty','Quake','Doom']) # adding new a user
    add_new_user(network,'Freda',['Doom']) # adding an existing user
    print network
    
    print get_secondary_connections(network,"Thomas") == None # user not in database
    print get_secondary_connections(network,"Benda") == [] # user with no primary connections
    add_new_user(network,'Lucy',['Quake'])
    add_connection(network, "Benda", "Lucy")
    print get_secondary_connections(network,"Benda") == [] # no secondary connections
    print get_secondary_connections(network,"Debra") == ['John', 'Levi', 'Bryant', 'Ollie', 'Walter', 'Freda', 'Robin'] # getting an existing secondary connections
    
    print connections_in_common(network, "Mercedes", "John") == 2 # existing connections in common
    print connections_in_common(network, "Mercedes", "Benda") == 0 # no connections in common
    
    print path_to_friend(network, 'Robin', "Benda") == None # path does not exist, there is a loop that must be terminated
    print path_to_friend(network, 'John', "Mercedes")
    print path_to_friend(network, 'Freda', "Jennie")

MYOP()

