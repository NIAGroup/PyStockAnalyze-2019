# PyStockAnalyze
Django web application that takes stock data, analyzes it and presents a graphical user interface.

## Environment Setup
1. Install Python 3.7.2 (Check off "Add Python 3.7 to PATH")
   > https://www.python.org/downloads/release/python-372/
2. Install Git Bash:
   > https://git-scm.com/downloads
3. Open Git Bash and navigate to home directory to create .bashrc file
   > ```touch ~/.bashrc```

   > Add the following code to the bashrc file
   > ```bash
   # Enable calling python executable
   alias python='winpty python.exe'
   
   # Setup proxy
   PROXY_OPT=--proxy=--proxy=http://...
   
   # Enable building environment through command
   alias buildenv='source $(git rev-parse --show-toplevel)/tools/build_env.sh'
   alias cleanenv='$(git rev-parse --show-toplevel)/tools/clean_env.sh'
   alias setproxy='PROXY_OPT=--proxy=http://...'
   alias clrproxy='PROXY_OPT='
   
   ```

4. Exit Git Bash and re-open it or run "source ~/.bashrc" to make the new commands available for execution while in git bash. The commands are to be used as follows:
   > * buildenv - Used to create the python virtual environment and install all dependencies
   > * cleanenv - Used to remove virtual environment build folder and exit environment if it's active

5. Clone repository:
   > ```git clone https://github.com/NIAGroup/PyStockAnalyze.git```

