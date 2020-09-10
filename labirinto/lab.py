import pygame


def generateMaze():
    with open('labirinto.txt', 'r') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines] 

    maze = []
    i = 0
    for line in lines:
        maze.append([])
        for cell in line:
            maze[i].append(int(cell))
        i+=1

    return maze

def main():

    maze = generateMaze()
    size = 25
    height = 30
    width = 25
    white,black,red = (255,255,255),(0,0,0),(255,0,0)
    gameDisplay = pygame.display.set_mode((700,800))
    pygame.display.set_caption("Labirinto")
    gameDisplay.fill(white)
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        for i in range(1,height+1):
            for j in range(1,width+1):
                if maze[i-1][j-1] == 1:
                    pygame.draw.rect(gameDisplay, black, [size*j,size*i,size,size])
                else:
                    pygame.draw.rect(gameDisplay,black,[size*j,size*i,size,size],1)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()