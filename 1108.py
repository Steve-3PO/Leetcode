# Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:

        # simply replace all occurences of dots to given string
        address = address.replace(".", "[.]")

        return address