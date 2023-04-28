# Balkonkraftwerk-Wizard

You are looking at the Backend code of **Balkonkraftwerk-Wizard**. A small app that is dedicated to inform and visualize users the aspects of Mini-PV-Systems. You can checkout the Client-Code as well at [Balkonkraftwerk-Wizard](https://github.com/ikke09/Balkonkraftwerk-Wizard/).

The Backend is a simple REST-API build with FastAPI. In provides some hardcoded informations and is a middleware for PVGIS and MaStR data.

The whole code is written in Python3.

## Setup project

1. Checkout repo
2. Change directory to repo
3. Enable VirtualEnvironment with `python -m venv .`
4. Activate venv `. venv/bin/activate`
5. Install dependencies `pip install -r ./requirements.txt`

After these steps, you should be able to run the backend via `python api.py` without any errors in the console. The Backend defaults to Port 8000.
