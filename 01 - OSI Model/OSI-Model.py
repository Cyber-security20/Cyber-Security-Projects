import os

from scapy.all import rdpcap, Ether, IP, TCP, UDP, ICMP
from rich.console import Console
from rich.table import Table

class Main():

    def __init__(self):
        self.file_name = None
        self.file_name_flag = False
        self.packets = None

    def find_file(self, file_name):
        for root, dirs, files in os.walk("C:/Users/cheet/Downloads"):
            # root = current folder path
            # dirs = subfolders
            # files = list of files in current folder
            if file_name in files:
                return os.path.join(root, file_name)
        else:
            print(f"{str(file_name)} could not be found")
            exit()

    def importing_file(self, file_path):
        self.file_name = file_path

        self.packets = rdpcap(file_path)
        print(f"Successfully loaded {len(self.packets)} packets from {self.file_name}")
        return self.packets

    def map_layers(self):
        self.layers = []

        for index, packet in enumerate(self.packets, start=1):
            local_layers_list = []
            if packet.haslayer(Ether):
                local_layers_list.append("layer 2 (Ethernet)")
                # self.layers.append(local_layers_list)
            if packet.haslayer(IP):
                local_layers_list.append("layer 3 (IP)")
                # self.layers.append(local_layers_list)
            if packet.haslayer(TCP):
                local_layers_list.append("layer 4 (TCP)")
                # self.layers.append(local_layers_list)
            if packet.haslayer(UDP):
                local_layers_list.append("layer 4 (UDP)")
                # self.layers.append(local_layers_list)
            if packet.haslayer(ICMP):
                local_layers_list.append("layer 4 (ICMP)")
                # self.layers.append(local_layers_list)

            self.layers.append(local_layers_list)
        # print(self.layers)

    def display_results(self):
        console = Console()
        table = Table(title="OSI Layer Breakdown")
        # console.print(table)

        table.add_column("Packet")
        table.add_column("Layer 2")
        table.add_column("Layer 3")
        table.add_column("Layer 4")

        for index, packet_layers in enumerate(self.layers, start=1):

            layer2 = next((l for l in packet_layers if "layer 2" in l), "N/A")
            layer3 = next((l for l in packet_layers if "layer 3" in l), "N/A")
            layer4 = next((l for l in packet_layers if "layer 4" in l), "N/A")

            table.add_row(str(index), layer2, layer3, layer4)

        console.print(table)
    def main(self):
        print(f"Name the file you wish to import?")
        file_name = input()
        full_path = self.find_file(file_name)

        self.importing_file(full_path)
        self.map_layers()
        self.display_results()
        # print(f"Successfully loaded {len(self.packets)} packets from {self.file_name}")


program = Main()
program.main()
