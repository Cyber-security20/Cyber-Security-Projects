import ipaddress
from rich.console import Console
from rich.table import Table


class SubnetCalculator():

    def __init__(self):
        self.ip = None
        self.cidr = None

    def calculate(self):

        network = ipaddress.IPv4Network(f"{self.ip}/{self.cidr}", strict=False)
        self.network_address = network.network_address
        self.broadcast_address = network.broadcast_address
        self.usuable_hosts = network.num_addresses - 2

        # print(self.network_address)
        # print(self.broadcast_address)
        # print(self.usuable_hosts)

    def get_input(self):
        ip_address_input = input("Enter in your IP address:")
        cidr_input = int(input("Enter in your subnet mask: "))

        self.ip = ip_address_input
        self.cidr = cidr_input

        # print(f"IP address Input: {str(ip_address_input)}")
        # print(f"CIDR Input: /{str(cidr_input)}")

    def display_results(self):
        print("=========================================================================================================")
        console = Console()
        table = Table(title="IP address Breakdown")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("IP Address", str(self.ip))
        table.add_row("CIDR", str(self.cidr))
        table.add_row("Network Address", str(self.network_address))
        table.add_row("Broadcast Address", str(self.broadcast_address))
        table.add_row("Usable Host", str(self.usuable_hosts))

        console.print(table)
        print("=========================================================================================================")

    def main(self):

        self.get_input()
        self.calculate()
        self.display_results()


x = SubnetCalculator()
x.main()