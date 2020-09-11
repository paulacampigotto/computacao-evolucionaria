import pygame
import random


def generateMaze():
    with open('labirinto.txt', 'r') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines] 

    maze = []
    i = 0
    for line in lines:
        maze.append([])
        for cell in line:
            if(cell in ['0', '1', '2', '3']):
                maze[i].append(int(cell))
        i+=1

    return maze


def mazeBoard(gameDisplay):
    for i in range(1,height+1):
        for j in range(1,width+1):
            if maze[i-1][j-1] == 0:
                pygame.draw.rect(gameDisplay, black, [size*j,size*i,size,size])
            elif maze[i-1][j-1] == 2:
                pygame.draw.rect(gameDisplay, green, [size*j,size*i,size,size])
            elif maze[i-1][j-1] == 3:
                pygame.draw.rect(gameDisplay, red, [size*j,size*i,size,size])
            else:
                pygame.draw.rect(gameDisplay,black,[size*j,size*i,size,size],1)
    pygame.display.update()

def updateBoard(gameDisplay):
    for i in range(1,height+1):
        for j in range(1,width+1):
            if (i-1, j-1) in getPositions(population[0]):
                pygame.draw.rect(gameDisplay, pink, [size*j,size*i,size,size])

    pygame.display.update()

def generateRandomPopulation():
    lastDirection = ""
    actualLine = 10
    actualColumn = 1
    pop = []
    for j in range(populationSize):
        ch = []
        for i in range(dimension):
            while True:
                cell = random.choice(domain)
                if cell == '→' and maze[actualLine][actualColumn+1] != 0 and (lastDirection != '←' or (maze[actualLine+1][actualColumn] == 0 and maze[actualLine-1][actualColumn] == 0 and maze[actualLine][actualColumn+1] == 0)):
                    ch.append(cell)
                    actualColumn+=1
                    lastDirection = cell
                    break
                if cell == '←' and maze[actualLine][actualColumn-1] != 0 and (lastDirection != '→' or (maze[actualLine+1][actualColumn] == 0 and maze[actualLine-1][actualColumn] == 0 and maze[actualLine][actualColumn-1] == 0)):
                    ch.append(cell)
                    actualColumn-=1
                    lastDirection = cell
                    break
                if cell == '↑' and maze[actualLine+1][actualColumn] != 0 and (lastDirection != '↓' or (maze[actualLine-1][actualColumn] == 0 and maze[actualLine][actualColumn+1] == 0 and maze[actualLine][actualColumn-1] == 0)):
                    ch.append(cell)
                    actualLine+=1
                    lastDirection = cell
                    break
                if cell == '↓' and maze[actualLine-1][actualColumn] != 0 and (lastDirection != '↑' or (maze[actualLine+1][actualColumn] == 0 and maze[actualLine][actualColumn-1] == 0 and maze[actualLine][actualColumn+1] == 0)):
                    ch.append(cell)
                    actualLine-=1
                    lastDirection = cell
                    break
        pop.append(ch)
    return pop


def getPositions(chrom):
    positions = []
    line = 10
    column = 1
    positions.append((line,column))
    for i in chrom:
        if i == '→':
            positions.append((line, column+1))
            column+=1
        elif i == '←':
            positions.append((line, column-1))
            column-=1
        elif i == '↑':
            positions.append((line+1, column))
            line+=1
        elif i == '↓':
            positions.append((line-1, column))
            line-=1
    return positions

def pprint(vector):
    for i in vector:
        print(i)



def main():

    global maze, size, height, width, white, black, red, green, pink, domain, populationSize, dimension, chrom, population

    domain = ['→','←','↑','↓']

    populationSize = 1
    dimension = 100
    chrom = []

    maze = generateMaze()

    population = generateRandomPopulation()
    print(population[0])
    #pprint(getPositions(population[0]))
   
    size = 25
    height = 30
    width = 25
    white,black,red,green,pink = (255,255,255),(0,0,0),(255,0,0),(0,255,0),(252,97,154)
    gameDisplay = pygame.display.set_mode((700,800))
    pygame.display.set_caption("Labirinto")
    gameDisplay.fill(white)
    end = False
    
    mazeBoard(gameDisplay)

    updateBoard(gameDisplay)

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()