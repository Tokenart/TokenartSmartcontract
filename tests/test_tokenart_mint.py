from brownie import accounts, web3, Wei, reverts
from brownie.network.transaction import TransactionReceipt
from brownie.convert import to_address
import pytest
from brownie import Contract


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


@pytest.fixture(scope = 'module', autouse=True)
def tokenart(Tokenart):
    tokenart = Tokenart.deploy({"from": accounts[0]})
    return tokenart

def test_mint_nft(tokenart):
    tokenart.mint("Name", {"from": accounts[5]})

def test_transfer(tokenart):
    _from = accounts[5]
    _to = accounts[3]
    tokenId = tokenart.mint("Name", {"from": _from}).return_value
    tokenart.transferFrom(_from,_to,tokenId, {"from":accounts[5]})

def test_transfer(tokenart):
    _from = accounts[5]
    _to = accounts[3]
    tokenId = tokenart.mint("Name", {"from": _from}).return_value
    tokenart.transferFrom(_from,_to,tokenId, {"from":accounts[0]})

