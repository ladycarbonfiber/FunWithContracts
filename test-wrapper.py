import serpent
from pyethereum import tester, utils, abi
serpent_code = 'button.se'

state = tester.state()
contract = state.abi_contract(serpent_code)
o_1 = contract.press_button(sender=tester.k0, value = 10000)
o_2 = contract.press_button(sender=tester.k1, value = 10000)
state.mine(n=2, coinbase=tester.a0)
o_3 = contract.press_button(sender=tester.k2, value = 10000)
state.mine(n=4, coinbase=tester.a0)
o_4 = contract.press_button(sender=tester.k2, value = 10000)
print(str(o_4))
o_5 = contract.claim_treasure(sender=tester.k0)
o = contract.claim_treasure(sender=tester.k2)
print(str(o))