#!/bin/bash -e
PROJ_ROOT_DIR=$(git rev-parse --show-toplevel)
PROJ_LOCALENV_TMPDIR=$PROJ_ROOT_DIR/build/localenv_temp
PROJ_LOCALENV_DIR=$PROJ_ROOT_DIR/src/pysdjango/pysdjango/localenv

# Move unsaved versions of files in localenv folder to build folder temporarily
mkdir $PROJ_LOCALENV_TMPDIR
mv $PROJ_LOCALENV_DIR/*.py $PROJ_LOCALENV_TMPDIR

# Pull from remote origin
git pull

# Move files back into localenv folder
mv $PROJ_LOCALENV_TMPDIR/*.py $PROJ_LOCALENV_DIR
rm $PROJ_LOCALENV_TMPDIR -rf
