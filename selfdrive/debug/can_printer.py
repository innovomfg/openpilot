#!/usr/bin/env python3
import argparse
import binascii
import time
from collections import defaultdict

import cereal.messaging as messaging


def can_printer(bus, max_msg, addr, ascii_decode):
  logcan = messaging.sub_sock('can', addr=addr)

  start = time.monotonic()
  lp = time.monotonic()
  msgs = defaultdict(list)
  while 1:
    can_recv = messaging.drain_sock(logcan, wait_for_one=True)
    for x in can_recv:
      for y in x.can:
        if y.src == bus:
          msgs[y.address].append(y.dat)

    if time.monotonic() - lp > 0.1:
      dd = chr(27) + "[2J"
      dd += f"{time.monotonic() - start:5.2f}\n"
<<<<<<< HEAD
      for _addr in sorted(msgs.keys()):
        a = f"\"{msgs[_addr][-1].decode('ascii', 'backslashreplace')}\"" if ascii_decode else ""
        x = binascii.hexlify(msgs[_addr][-1]).decode('ascii')
        freq = len(msgs[_addr]) / (time.monotonic() - start)
        if max_msg is None or _addr < max_msg:
          dd += "%04X(%4d)(%6d)(%3dHz) %s %s\n" % (_addr, _addr, len(msgs[_addr]), freq, x.ljust(20), a)
=======
      for addr in sorted(msgs.keys()):
        a = f"\"{msgs[addr][-1].decode('ascii', 'backslashreplace')}\"" if ascii_decode else ""
        x = binascii.hexlify(msgs[addr][-1]).decode('ascii')
        freq = len(msgs[addr]) / (time.monotonic() - start)
        if max_msg is None or addr < max_msg:
          dd += "%04X(%4d)(%6d)(%3dHz) %s %s\n" % (addr, addr, len(msgs[addr]), freq, x.ljust(20), a)
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)
      print(dd)
      lp = time.monotonic()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="simple CAN data viewer",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument("--bus", type=int, help="CAN bus to print out", default=0)
  parser.add_argument("--max_msg", type=int, help="max addr")
  parser.add_argument("--ascii", action='store_true', help="decode as ascii")
  parser.add_argument("--addr", default="127.0.0.1")

  args = parser.parse_args()
  can_printer(args.bus, args.max_msg, args.addr, args.ascii)
