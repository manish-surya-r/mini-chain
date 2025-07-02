import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        sha.update(block_string.encode())
        return sha.hexdigest()

def create_genesis_block():
    """
    Create the first block in the blockchain (block #0)
    """
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    """
    Generate a new block based on the previous block
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
