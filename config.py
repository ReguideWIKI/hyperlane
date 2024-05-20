RANDOMIZE = True

MIN_PAUSE = 30
MAX_PAUSE = 60

MAX_GWEI = 100

PAUSE_BETWEEN_RETRIES = 1
CHECK_GWEI = False
RETRIES = 1

# --- Bridges --- #
nautilus_bridge = False
merkly = False

# --- NFT --- #
get_mint = True
womex = False
zeroway = False
nogem = True


# --- Bridges --- #

class NautilusBridgeConfig:
    from_chain = 'Nautilus'  # BSC / Nautilus
    token = 'ZBC'
    amount = [50, 100]
    use_percentage = True
    bridge_percentage = [0.5, 0.5]


# --- NFT --- #

class GetMintConfig:
    from_chain = ['BASE']
    to_chain = ['ARB']


class NogemConfig:
    action = ['FT']  # FT / NFT

    # --- FT --- #
    mint = True
    from_chain = ['BASE']
    to_chain = ['POLYGON']
    bridge_all_tokens = True
    percent_to_bridge = [0.05, 0.1]

    # --- NFT --- #
    from_chain_nft = ['BASE']
    to_chain_nft = ['POLYGON']
