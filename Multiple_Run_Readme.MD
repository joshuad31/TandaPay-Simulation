# Tandapay Simulation


## Simulation Logic and Program Flow

The program depends on three excel files being present in the folder with 
the Tandapay.py file: '1 System Database.xlsx', '2 User Database.xlsx', 
and '3 Matrix Database.xlsx'. Once detected, all values save for the row
and column titles will be cleared out for both the System and User Databases.

Install requirements:

`pip install -r requirements.txt`

To run the Tandapay simulation with the UI, type the command:

`python Tandapay.py`

To run the Tandapay simulation using the matrix of values, type the command:

`python Tandapay.py -m`

The simulation should take 10-20 seconds per simulation run. With the matrix
of values, this could take up to 8 hours depending on your system hardware. The 
test system used an 8-core 4.18 GHz processor with a Gen 3 M.2 NVME drive to 
achieve 6-7 hour runs.

The '1 System Database.xlsx' and the '2 User Database.xlsx' databases will be
reused each simulation run. The System Database represents the entire simulation
at the most recent execution and the User Database will represent the changes 
made as the simulation progresses to display the last Period Data values. The 
Matrix Database will be populated as the simulation progresses through the vectors
of values.

The original program was built using TKinter and has a bit of logic associated
with that UI, but the simulation itself starts with the `startAction` function. 
Because there is a significant number of variables passed from simulation 
function to simulation function, the simulation logic itself is under one 
Python function. These variables include all of the Environment Variables(EV),
Pricing Variables(PV) as well as both the System and User database spreadsheet 
values - this can amount to over one hundred variables. To simplify this,
the `assign_variables` function can be called which updates all of the EV, PV, 
period row integers, and System Record variables based on the Period Data 
Number (refer to the specc for Period Data). This will reset the System Record
Row based on the Period Data the simulation is in when called. With this 
`assign_variables` function, it is suggested to further modularize the simulation
where needed. More on suggested improvements under the 'Known Issues & Improvement
Suggestion' section.

The simulation can run two different ways. The Matrix version takes a matrix of 
EV and PV values and runs the simulation one vector at a time. The UI version
opens up a GUI so that the EV and PV values can be manually entered.

### Matrix Simulation

Included is a Python program called `ev_generator.py`. Information on how the matrix
is generated can be found in the Tandapay specc. This program produces a JSON file 
containing a matrix based on the number of different variables. When the Tandapay 
simulation is executed under the matrix version, the program looks for the 
`matrix.json` file to run the simulation one vector at a time and produces the 
overall results in the '3 Matrix Database.xlsx' file. At the time of writing, the 
different variables were known and so produces the '3 Matrix Database.xlsx' column 
values based on the current vector's EV and PV values. 

### UI Simulation 

    * UI functionality author *

## Know Issues & Improvement Suggestions

There are a few notable issues that need to be addressed. It appears that some
of the checksum functions located in the `startAction` function are sometimes 
inaccurate and, currently, it is unknown whether the checksum functions have 
issues or it's being fed incorrect values producing a failed checksum. These
issues generally surface running the matrix version. To help with this, the 
simulation program under the matrix version produces a file detailing out each
of the checksum failures, the Period Data, unequal checksums, and the vector
that caused the failure.

### Suggestions

It is suggested to reduce the dependencies and edge cases such as creating a 
formatted version of each of the three database excel sheets if none are present
with the program. Additionally, using the CSV module could improve performance.
Further modularization could help to isolate bugs as well as portions of the 
specc that may be producing unintended results. 