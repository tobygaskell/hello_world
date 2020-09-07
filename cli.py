from sys import argv
import player.Player as player 
import pull.main as pull 
import display.logo as test 


def main():
    if argv[1] == "pull":
        pull.check(argv[2:])
        pass 
    if argv[1] == "test":
        test.display_logo('https://media.api-sports.io/football/teams/33.png') 

if __name__ == '__main__':
    main()


# aqi key = c353bf85damsh1032ad157d425a6p15acc8jsn697e609db7c1