from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    priority_fee = networks.active_provider.priority_fee
    max_base_fee = int(networks.active_provider.base_fee * 1.2) + priority_fee
    compass = "0xB54E2c37645fd42F09C93B50B29648a9Cc4F6065"
    uniswap_v2_router = "0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 0
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 0
    project.limit_order_uniswap_v2.deploy(
        compass, uniswap_v2_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=priority_fee, sender=acct)

# 0xBb4FAc66AffD17365C447C837fd0A2F064313d64