# Example Project to get started

We want to program a battery model and get data for a PV station.
With this and a constant demand, we want to model charging and
discharging of the battery and see, how often it hits its limits
for different sizings.

We will start off together, please make your own version individually
or as a group, that you can use and modify for your own project.

## First Steps

* First of all, each group creates a git repository, ideally already 
  linked to github.
* We start with an empty Python environment, and create an 
  environment.yaml or requirements.txt file to track our library dependencies.
* Let's also add a .gitignore file already, and a short Readme.md.
  Don't forget to already commit your changes.
* Now we want to start coding. For this I will create a Jupyter notebook
  (also add the requirements). Alternatively, you can also use a plain python.


## Battery Model

* We create a class called Battery
* Initialize the class with parameters as needed, eg. capacity_kwh, state_of_charge and efficiency.
* Add functions for charge and discharge.
* Test your model.
* If everything works, put the relevant code to a separate file src/battery.py and use an import for it.

## Get Data for PV

* Use the Intro Tutorial of pvlib: https://pvlib-python.readthedocs.io/en/stable/user_guide/introtutorial.html
* Use a PV system with realistic parameters and get data for a period of a year.
* Have a look at the data with pandas.
* Either generate a function to generate example PV data from the above code,
  or save the generated data to a file (data/pv2015.csv)

## Connect battery and PV

* Import the PV data and create a battery instance.
* Make a loop over time where you charge and discharge the battery.
  Start with a constant demand for discharge.
* Plot results, show how much time the battery was full or empty, leading to
  PV or demand cutoff.