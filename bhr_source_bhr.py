#!/usr/bin/env python
from bhr_client.source_blocker import SourceBlocker
from bhr_client.rest import login_from_env, login
import csv
import os

PEER_HOST = os.getenv("BHR_PEER_HOST")
PEER_TOKEN = os.getenv("BHR_PEER_TOKEN")
PEER_MAPPING_FILE = os.getenv("BHR_PEER_SOURCE_MAPPING_FILE")

class PeerBlocker(SourceBlocker):
    source = 'peer'
    must_exist = False
    duration = "4h"

    def read_mapping_file(self):
        mapping = {}
        for upstream_source, my_source in csv.reader(open(PEER_MAPPING_FILE)):
            mapping[upstream_source] = my_source
        return mapping

    def get_records(self):
        blocks = []
        peer_client = login(PEER_HOST, PEER_TOKEN)
        source_mapping = self.read_mapping_file()
        for rec in peer_client.get_list():
            upstream_source = rec['source']
            my_source = source_mapping.get(upstream_source)
            if not my_source:
                continue
            blocks.append({
                'cidr': rec['cidr'],
                'why': rec['why'],
                'source': my_source,
                'autoscale': True,
            })
        return blocks

def main():
    client = login_from_env()

    s = PeerBlocker(client)
    s.run()

if __name__ == "__main__":
    main()
