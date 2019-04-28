# Demos : Alpha Vantage Basic
The purpose of this folder is to contain isolated django projects that demonstrate some core capability.

To run a demo, navigate to that directory and follow the instructions provided in its **README.md**.

_The code site can be started within the */src/demos/alphavantage_basic* directory.
This directory can be thought of as your *top level directory*_

`python manage.py runserver`

The site can be found in your browser at:
http://127.0.0.1:8000/home

## Key Elements in the  demo 

- Basic UI w/ dropdowns & buttons
- AJAX calls to trigger alphantage code and return it the UI dynmically (w/o reloading the page)
- Dynamic html views using jquery
- MaterializeCSS styling inclusion for site formatting


1. To create an app, the following line was used:

`python manage.py startapp name_of_app`

2. Once you app is created, the following directories will be created along with it:

<p class='tab'>&emsp;name_of_app/</p>
<p class='tab'>&emsp;&emsp;__init__.py</p>
<p class='tab'>&emsp;&emsp;admin.py</p>
<p class='tab'>&emsp;&emsp;apps.py</p>
<p class='tab'>&emsp;&emsp;migrations/</p>
<p class='tab'>&emsp;&emsp;&emsp; __init__.py</p>
<p class='tab'>&emsp;&emsp;models.py</p> 
<p class='tab'>&emsp;&emsp;tests.py</p>
<p class='tab'>&emsp;&emsp;views.py</p>





3. the urls.py file must be created using :
`touch urls.py`

4. you will also need to create directories for reference file:
	- templates _(will used to hold html files)_
	- static _(will used to hold image, video, and css files)_
	- scripts _(will be used to hold javascript & python files)_
