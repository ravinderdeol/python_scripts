from etherscan import Etherscan

eth = Etherscan("YOUR ETHERSCAN API KEY")

# dictionary of gas prices
gas_oracle = eth.get_gas_oracle()

# gas prices
safe_gas = gas_oracle["SafeGasPrice"]
proposed_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"]

# message on seperate lines
message = f"Safe Gas Price: {safe_gas} Gwei \n Proposed Gas Price: {proposed_gas} Gwei \n Fast Gas Price: {fast_gas} Gwei"

print(message)
