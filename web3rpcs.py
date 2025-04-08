import random
import requests
import time

_RPC_LIST = [
    "https://carrot.megaeth.com/rpc",
    "https://eth.llamarpc.com",
    "https://rpc.flashbots.net"
]

def is_rpc_working(url, timeout=1.5):
    try:
        start = time.time()
        response = requests.post(url, json={"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}, timeout=timeout)
        if response.status_code == 200:
            latency = time.time() - start
            return latency
    except:
        pass
    return float('inf')

def rpcs(private_key=None):
    best_rpc = None
    lowest_latency = float('inf')

    for rpc in _RPC_LIST:
        latency = is_rpc_working(rpc)
        if latency < lowest_latency:
            best_rpc = rpc
            lowest_latency = latency

    if best_rpc:
        print(f"✅ Best RPC selected: {best_rpc} (latency: {lowest_latency:.2f}s)")
        return best_rpc
    else:
        fallback = random.choice(_RPC_LIST)
        print(f"⚠️ No fast RPC found, using fallback: {fallback}")
        return fallback
