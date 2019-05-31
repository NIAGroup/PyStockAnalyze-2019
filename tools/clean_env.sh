#!/bin/bash -e

PROJ_ROOT_DIR=$(git rev-parse --show-toplevel)
PROJ_BUILD_PATH=$PROJ_ROOT_DIR/build
PROJ_SRC_PATH=$PROJ_ROOT_DIR/src
PROJ_TOOL_PATH=$PROJ_ROOT_DIR/tools

if [ ! -z "$VIRTUAL_ENV" ]; then
	echo "[clean] Exiting virtual environment"
	$PROJ_BUILD_PATH/pydjango-build-env/Scripts/deactivate.bat
fi

if [ -d "$PROJ_BUILD_PATH" ]; then
	echo "[clean] Removing build directory"
	rm -rf $PROJ_BUILD_PATH/
fi

