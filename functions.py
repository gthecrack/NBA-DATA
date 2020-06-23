import pandas as pd
import numpy as np
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo

def openDataframe(file='./clean_data.csv'):
    return pd.read_csv(file)

nba_players = players.get_players()
def getPlayerId(player_name):
    for player in nba_players:
        if player['full_name'].lower() == player_name.lower():
            return player['id']


def  getBasicInfo(player):
    x = getPlayerId(player)
    # Basic Request
    headers = commonplayerinfo.CommonPlayerInfo(x).get_dict()['resultSets'][0]['headers']
    #print(headers)
    values = commonplayerinfo.CommonPlayerInfo(x).get_dict()['resultSets'][0]['rowSet'][0]
    #print(values)
    basic_dict = dict(zip(headers,values))
    return basic_dict


def addingPlayerId(df):
    player_ids = []
    for e in df['Player']:
        #print(e)
        player_dict = getBasicInfo(e)
        #print(player_dict)
        player_ids.append(player_dict['PERSON_ID'])
    df['Player ID'] = player_ids
    return df

def addingDraftnumber(df):
    draft_numbers = []
    for e in df['Player']:
        #print(e)
        player_dict = getBasicInfo(e)
        #print(player_dict)
        draft_numbers.append(player_dict['DRAFT_NUMBER'])
    df['Draft number'] = draft_numbers
    return df

def addingJerseynumber(df):
    jersey_numbers = []
    for e in df['Player']:
        #print(e)
        player_dict = getBasicInfo(e)
        #print(player_dict)
        jersey_numbers.append(player_dict['JERSEY'])
    df['Jersey'] = jersey_numbers
    return df

def playerComparison(df,*players):
    return df[df['Player'].isin(players)]

def showPlayer(draftpos,playerpos,df):
    option_draft = [draftpos]
    option_position = [playerpos]
    return print(df[(df['Draft number'].isin(option_draft)) & (df['Pos'].isin(option_position))])