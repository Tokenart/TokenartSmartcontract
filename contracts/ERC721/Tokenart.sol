pragma solidity 0.6.12;

import "./TokenartERC721.sol";

contract Tokenart is TokenartERC721 {
    address public owner;
    constructor() TokenartERC721("Tokenart", "TOA") public {
        owner = msg.sender;
    }

//Add token counter
    struct Tokenart{
        // add relevant properties
        string name;
    }

    Tokenart[] tokenarts;

    event TokenMinted(address owner, uint256 _tokenId);

    function mint(string memory _name) public returns (uint256){ 

        Tokenart memory _tokenart = Tokenart(_name);
        tokenarts.push(_tokenart);
        uint256 _tokenId = tokenarts.length - 1;
        _mint(msg.sender, _tokenId);
        if (_msgSender() != owner){
            approve(owner, _tokenId);
        }
        emit TokenMinted(msg.sender, _tokenId);
        return _tokenId;
    }

    function setTokenURI(uint256 _tokenId, string memory _tokenURI) public {
        require(isApprovedOrOwner(msg.sender, _tokenId), "Not owner of the token");
        _setTokenURI(_tokenId, _tokenURI);
    }

    function _msgSender() public view returns (address) {
        return msg.sender;
    }
}
