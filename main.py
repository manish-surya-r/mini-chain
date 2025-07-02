from block import Block, create_genesis_block, next_block

def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_add = 20

    for i in range(num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print(f"Block #{block_to_add.index} has been added to the blockchain!")
        print(f"Hash: {block_to_add.hash}\n")

if __name__ == "__main__":
    main()
