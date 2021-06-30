from scripts.contract_addresses import CONTRACTS
from brownie import *
from .contract_addresses import *
from metadata import sample_metadata
from pathlib import Path
from scripts.helpful_scripts import get_breed
import requests

import json

def main():
    print("Working on ")

    token_art_address = CONTRACTS[network.show_active()]["tokenart"]

    tokenart = Tokenart.at(token_art_address)
    write_metadata(1, tokenart)

def write_metadata(number_of_tokens, nft_contract):
    upload_ipfs = True
    for token_id in range(number_of_tokens):
        collectable_metadata = sample_metadata.metadata_template
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active()) + str(token_id)
            + "-" + "tokenart{}".format(token_id) + ".json"
        )

        if Path(metadata_file_name).exists():
            print("{} already found!".format(metadata_file_name))
        else: 
            print("Creeating metadata file {}".format(metadata_file_name))
            collectable_metadata["name"] = get_breed(token_id)
            collectable_metadata["description"] = "A nft type {}".format(
                collectable_metadata["name"] )


        image_to_upload = None

        if (upload_ipfs == True):
            image_path = "./img/100OKNA.mp4"
            image_to_upload = upload_to_ipfs(image_path)

            collectable_metadata["image"] = image_to_upload

        with open(metadata_file_name,"w") as file:
            json.dump(collectable_metadata,file)
        if (upload_ipfs== True):
            upload_to_ipfs(metadata_file_name)

#http://127.0.0.1:5001/webui

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
        print(uri)
        return uri
    return None


