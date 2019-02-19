#!/bin/bash -e

PROJ_ROOT_DIR=$(git rev-parse --show-toplevel)
PROJ_BUILD_PATH=$PROJ_ROOT_DIR/build
PROJ_SRC_PATH=$PROJ_ROOT_DIR/src
PROJ_TOOL_PATH=$PROJ_ROOT_DIR/tools

# Removing build directory
if [ -d "$PROJ_BUILD_PATH" ]; then
	rm -rf $PROJ_BUILD_PATH/
fi

# Removing activate script
if [ -f "$PROJ_ROOT_PATH/activate" ]; then
	rm $PROJ_ROOT_PATH/activate
fi

