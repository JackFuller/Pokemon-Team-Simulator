import csv
import Pokemon

def getPokemonTeam(filePath):
    team = []
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:       
                #Pull Move Data
                moves = [] 
                for x in range(4):   
                    indent  = x * 6 
                    move = Pokemon.MoveData(row[9 + indent],row[10 + indent],row[11 + indent],row[12+ indent],row[13+indent],row[14+indent])     
                    moves.append(move)
                team.append(Pokemon.PokemonData(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],moves)) 
                line_count += 1
    return team


teamOne = getPokemonTeam(r'Data\TeamTwo.csv')
teamTwo = getPokemonTeam(r'Data\TeamTwo.csv')


member = teamOne[0]
typeOne = Pokemon.typings.get(member.elementOne)
typeTwo = Pokemon.typings.get(member.elementTwo)

for x in range(18):
    typeOneWeaknessFactor = Pokemon.typeChart[x][typeOne]
    typeTwoWeaknessFactor = 0
    if typeTwo != "Null":
        typeTwoWeaknessFactor = Pokemon.typeChart[x][typeTwo]

    overallWeakness = typeOneWeaknessFactor + typeTwoWeaknessFactor
    if overallWeakness == 0:
        print(f"Charizard is immume to {x}")
    elif overallWeakness == 2:
        print(f"Charizard is weak to: {x}")
    elif overallWeakness == 4:
        print(f"Charizard is super weak to: {x}")
        
    


# for member in teamOne:  
#     print(member.name)
#     for x in range(18):

#     for move in member.moves:
#         print(move.name)