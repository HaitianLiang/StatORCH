import argparse, os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--port',type=int,default=8000); args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]/'frontend'; os.chdir(root)
    print(f'Serving StatOrch frontend at http://127.0.0.1:{args.port}')
    ThreadingHTTPServer(('127.0.0.1',args.port),SimpleHTTPRequestHandler).serve_forever()
