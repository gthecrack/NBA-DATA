from argparse import ArgumentParser
from functions import *
import pandas as pd

parser = ArgumentParser(description='Program that receives a draft position and a player position and creates a report of the players that fall under those inputs')
parser.add_argument('-d','--draftpos', type=str, help='Introduce the draft position to evaluate')
parser.add_argument('-p','--playerpos', type=str, help='Introduce the player position to evaluate')
args = parser.parse_args()

def main():
    df = openDataframe() #opens the dataset
    showPlayer(args.draftpos,args.playerpos,df)
if __name__ == "__main__":
    print(main())