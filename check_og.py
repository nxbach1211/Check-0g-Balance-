from web3 import Web3

# 0G-Newton-Testnet configuration
RPC_URL = "https://lightnode-json-rpc-0g.grandvalleys.com"
CHAIN_ID = 16600  # 0x40d8

# Connect to 0G-Newton-Testnet
web3 = Web3(Web3.HTTPProvider(RPC_URL))

def check_balance(address):
    try:
        # Verify connection
        if not web3.is_connected():
            raise Exception("Failed to connect to 0G-Newton-Testnet")

        # Ensure address is valid
        if not web3.is_address(address):
            return f"Invalid address: {address}"

        # Convert to checksum address
        checksum_address = web3.to_checksum_address(address)

        # Get balance in Wei
        balance_wei = web3.eth.get_balance(checksum_address)

        # Convert Wei to 0G (native token)
        balance_0g = web3.from_wei(balance_wei, 'ether')

        return balance_0g

    except Exception as e:
        return f"Error for {address}: {str(e)}"

def read_addresses_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and filter out empty lines
            addresses = [line.strip() for line in file if line.strip()]
        return addresses
    except FileNotFoundError:
        return "Error: diachi.txt file not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_results_to_file(results, file_path):
    try:
        with open(file_path, 'w') as file:
            for result in results:
                file.write(result + '\n')
        return True
    except Exception as e:
        return f"Error writing to file: {str(e)}"

# Main execution
if __name__ == "__main__":
    file_path = "diachi.txt"
    addresses = read_addresses_from_file(file_path)

    if isinstance(addresses, str):
        print(addresses)  # Print error message if file reading failed
    else:
        results = []
        for address in addresses:
            balance = check_balance(address)
            result = f"Balance for {address}: {balance} 0G"
            print(result)
            results.append(result)

        # Write results to ketqua.txt
        write_result = write_results_to_file(results, "ketqua.txt")
        if write_result is True:
            print("Results successfully written to ketqua.txt")
        else:
            print(write_result)