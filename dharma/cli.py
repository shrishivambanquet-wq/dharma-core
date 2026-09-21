"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import argparse

from dharma.authority.authority_index import AuthorityIndex
from dharma.authority.search import AuthoritySearch
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def main():
    parser = argparse.ArgumentParser(prog="dharma")
    sub = parser.add_subparsers(dest="command")

    search = sub.add_parser("search")
    search.add_argument("query")

    args = parser.parse_args()

    if args.command == "search":
        idx = AuthorityIndex()
        idx.add(AuthorityNode(AuthorityKind.PERSON, "Paresh Somani"))
        idx.add(AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers"))

        results = AuthoritySearch(idx).text(args.query)

        for node in results:
            print(node.name)


if __name__ == "__main__":
    main()
