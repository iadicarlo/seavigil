#!/usr/bin/env bash
# Local launcher for the live tracker: starts the aisstream ingest and the map server
# together, then serves the map on http://localhost:PORT. Ctrl-C stops both.
#
#   tracker/run.sh           # port 8100
#   tracker/run.sh 8200      # custom port
#
# Needs AISSTREAM_KEY (free key at aisstream.io), read from .env at the repo root.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ -f .env ]; then set -a; . ./.env; set +a; fi
: "${AISSTREAM_KEY:?set AISSTREAM_KEY in .env (free key at aisstream.io)}"

PORT="${1:-8100}"
echo "starting aisstream ingest ..."
uv run --with websockets python tracker/ingest.py &
INGEST=$!
trap 'kill "$INGEST" 2>/dev/null || true' EXIT INT TERM

# give the socket a moment to connect and seed a few positions before the map opens
sleep 3
python3 tracker/server.py "$PORT"
