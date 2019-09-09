# 
Initial version of the api

## Development setup

### Prerequisites
Install Docker

### Build the docker image and start the server

```
make img
make up
```
Visit http://127.0.0.1:8000/ in your browser
The initial superuser is admin/admin
# Points
### -->When you run your project first time python compiles all your *.py code in bytecode compiles files,*.pyc.
### How to Clean up the .pyc compiles file ? 
Create a file .bash_profile in your home directory
Add this alias at the end of .bash_profile as follows.
```
~/.bash_profile
alias delpyc="find . -name \"*.pyc\" -delete"
```
#### Now to clean the python-compiled files, go to project directory and type the following command in the teminal.
````delpyc````

#### How to include libraries in python file as follows. 
```
# -*coding: UTF-8 -*-
# System libraries
import os
import re
from datetime import datetime

# Third-part libraries
import boto
from PIL import Image

# Django modules
from django.db import modules
from django.conf import settings

# Django apps
from cms.modules import Page

# Current-app modules
from . import app_settings
```
