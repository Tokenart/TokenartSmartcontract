from brownie import *

def load_accounts():
    if network.show_active() in ['mainnet', 'bsc-test', 'matic-test']:
        # replace with your keys
        accounts.load("token_art")
    # add accounts if active network is goerli
    if network.show_active() in ['goerli', 'ropsten','kovan','rinkeby']:
        # 0xa5C9fb5D557daDb10c4B5c70943d610001B7420E 
       #Note: Only to deploy. Dont send eth to this address
        accounts.add('55a24ceff28920d9fe1d9c2ac20be0424b8b1aec43909e13bc6991e43eb36de5')
        # 0x9135C43D7bA230d372A12B354c2E2Cf58b081463

def deploy_token_art():
    deployer = accounts[0]
    token_art = Tokenart.deploy({"from": deployer},publish_source=True)

def main():
    load_accounts()
    deploy_token_art()