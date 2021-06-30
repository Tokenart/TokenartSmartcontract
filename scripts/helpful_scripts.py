from brownie import *
OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def get_breed(token_id):
    token_switch = token_id % 3
    switch = {0: "Movie", 1: "Audio", 2: "Image"}
    return switch[token_switch]