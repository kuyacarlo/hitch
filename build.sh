#!/bin/bash
# Build SRPM and optionally push to COPR.
# Usage:
#   ./build.sh              # local mock rebuild
#   ./build.sh kuya-carlo/hitch  # build + submit to COPR

copr_name="$1"
set -e

spec="hitch.spec"
version=$(grep "^Version:" "$spec" | awk '{print $2}')

# Create source tarball with vendored deps
mkdir -p sources
tar czf "sources/hitch-${version}.tar.gz" \
  --transform "s,^,hitch-${version}/," \
  cmd internal main.go go.mod go.sum vendor testdata hitch.spec LICENSE Makefile .gitignore

# Build SRPM
mkdir -p rpms
mock --buildsrpm \
  --sources "$PWD/sources" \
  --spec "$PWD/$spec" \
  --resultdir "$PWD/rpms"

srpm=$(ls rpms/hitch-*.src.rpm 2>/dev/null | head -1)

if [ -z "$srpm" ]; then
  echo "ERROR: No SRPM produced"
  exit 1
fi

echo "Built SRPM: $srpm"

if [ -n "$copr_name" ]; then
  copr-cli build "$copr_name" "$srpm"
else
  mock --rebuild "$srpm" --resultdir "$PWD/rpms"
fi
