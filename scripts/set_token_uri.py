from brownie import *
from scripts.helpful_scripts import get_breed
from .contract_addresses import *

metadata_dic = {
    "tokenart0": "https://gateway.pinata.cloud/ipfs/QmWhpxpHDFDw19XpbLedJQ8TPMA2Btok7jQMSb9dfWPuti",
    "tokenart1": "https://gateway.pinata.cloud/ipfs/QmXBwn4e7JmUnZceknK1g9x4BcSxvba2mXynjgmJa8MaZk"
}


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

def main():
    load_accounts()
    mint = False
    print("Working on " + network.show_active())
    token_art_address = CONTRACTS[network.show_active()]["tokenart2"]

    tokenart = Tokenart.at(token_art_address)
    number_of_tokens = tokenart.totalSupply()
    print("No of tokens is: "+ str(number_of_tokens))
    if mint ==True:
        mint_token_art(tokenart)
    for token_id in range(number_of_tokens):
        breed = get_breed(token_id)
        if not tokenart.tokenURI(token_id).startswith("https://"):
            print("Setting token URI of{}".format(token_id))
            set_tokenURI(token_id, tokenart, metadata_dic["tokenart"+str(token_id)])
        else:
            print("Skipping ")

    
def set_tokenURI(token_id, nft_contract, tokenURI):

    nft_contract.setTokenURI(token_id, tokenURI, {"from": accounts[0]})
    print("You can view nft at")
    print("Please give upto 20 minutes and hit refresh metadata button")


def mint_token_art(tokenart):
    tokenart.mint("Good one", {"from":accounts[0]})