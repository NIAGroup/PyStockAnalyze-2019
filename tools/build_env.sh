#!/bin/bash -e


echo "[build] Creating project environment variables"
PROJ_ROOT_DIR=$(git rev-parse --show-toplevel)
PROJ_BUILD_PATH=$PROJ_ROOT_DIR/build
PROJ_SRC_PATH=$PROJ_ROOT_DIR/src
PROJ_TOOL_PATH=$PROJ_ROOT_DIR/tools

PROJ_VENV_NAME=pydjango-build-env
PROJ_VENV_PATH=$PROJ_BUILD_PATH/$PROJ_VENV_NAME
PROJ_ACTENV_PATH=$PROJ_VENV_PATH/Scripts/activate

# Create activate script pointer
alias activate='source $PROJ_ACTENV_PATH'
alias cleanenv='rm $PROJ_BUILD_PATH/* -rf; rm $PROJ_ROOT_PATH/activate; deactivate > /dev/null'

if [ ! -d $PROJ_VENV_PATH ]; then
	echo "[build] Creating python virtual environment"
	python -m venv $PROJ_VENV_PATH
	# Install dependencies into environment
	echo "[build] Instsalling dependencies"
	activate
	python -m pip install --upgrade pip
	pip install -r $PROJ_TOOL_PATH/requirements.txt $PROXY_OPT
else
	echo "[build] Python virtual environment already exists"
fi


