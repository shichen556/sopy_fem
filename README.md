<a id="readme-top"></a>

# sopy_fem

sopy_fem is an academic Python package for finite element analysis of 2D solids and structures. It is designed as a support tool for the Simulation and Optimization course of the Master in Interdisciplinary & Innovative Engineering at the Polytechnic University of Catalonia (UPC).





## Table of Contents
- [sopy_fem](#sopy_fem)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Local Machine](#local-machine)
  - [Google Colab](#google-colab)

- [Usage](#usage)
  - [Run the solver with a JSON data file](#solver)
  - [Get help and generate JSON example files](#help)

- [Available types](#examples)
  - [dynamics_FRAME02](#dynamics_frame02)
    - [Sample](#dynamics_frame02-sample)
    - [Custom file](#dynamics_frame02-custom-file)
      - [Problem data](#dynamics_frame02-problem-data)
      - [Results](#dynamics_frame02-results)

  - [dynamics_TRUSS02](#dynamics_truss02)
    - [Sample](#dynamics_truss02-sample)
    - [Custom file](#dynamics_truss02-custom-file)
      - [Problem data](#dynamics_truss02-problem-data)
      - [Results](#dynamics_truss02-results)

  - [electrical_BR02](#electrical_br02)
    - [Sample](#electrical_br02-sample)
    - [Custom file](#electrical_br02-custom-file)
      - [Problem data](#electrical_br02-problem-data)
      - [Results](#electrical_br02-results)

  - [mechanics_BR02](#mechanics_br02)
    - [Sample](#mechanics_br02-sample)
    - [Custom file](#mechanics_br02-custom-file)
      - [Problem data](#mechanics_br02-problem-data)
      - [Results](#mechanics_br02-results)
    
  - [mechanics_QU04](#mechanics_qu04)
    - [Sample](#mechanics_qu04-sample)
    - [Custom file](#mechanics_qu04-custom-file)
      - [Problem data](#mechanics_qu04-problem-data)
      - [Results](#mechanics_qu04-results)

  - [mechanics_TR03](#mechanics_tr03)
    - [Sample](#mechanics_tr03-sample)
    - [Custom file](#mechanics_tr03-custom-file)
      - [Problem data](#mechanics_tr03-problem-data)
      - [Results](#mechanics_tr03-results)

  - [structural_FRAME02](#structural_frame02)
    - [Sample](#structural_frame02-sample)
    - [Custom file](#structural_frame02-custom-file)
      - [Problem data](#structural_frame02-problem-data)
      - [Results](#structural_frame02-results)

  - [structural_TRUSS02](#structural_truss02)
    - [Sample](#structural_truss02-sample)
    - [Custom file](#structural_truss02-custom-file)
      - [Problem data](#structural_truss02-problem-data)
      - [Results](#structural_truss02-results)

  - [thermal_BR02](#thermal_br02)
    - [Sample](#thermal_br02-sample)
    - [Custom file](#thermal_br02-custom-file)
      - [Problem data](#thermal_br02-problem-data)
      - [Results](#thermal_br02-results)

- [Project Structure](#project-structure)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Features

- Supports analysis of 2D structural and solid problems.
- Includes JSON input examples for several problem types:
  - Structural dynamics of beams and trusses (`dynamics_FRAME02`, `dynamics_TRUSS02`)
  - Electrical systems (`electrical_BR02`)
  - Solid mechanics (`mechanics_BR02`, `mechanics_QU04`, `mechanics_TR03`)
  - Structural analysis (`structural_FRAME02`, `structural_TRUSS02`)
  - Thermal analysis (`thermal_BR02`)
- Provides help utilities to generate sample JSON input files via `sopy_fem_help`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Requirements

- Python 3.7 or newer
- Dependencies listed in `requirements.txt`

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Installation

### Local Machine

1. Clone the repository or download the project.
``` bash
git clone https://github.com/DanielDiCapua/sopy_fem.git
```
2. Install dependencies in your Python environment:

``` bash
pip install -r requirements.txt
```

3. Optionally install the package locally:

``` bash
pip install -e .
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Google Colab

1. **Install module**

``` bash
!pip install sopy_fem
```
2. **Import libraries**

``` python
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Usage

> [!NOTE]
> **Note**: For consistency, it's recommended to use **SI units**. 

### Run the solver with a JSON data file <a id="solver"></a>

The main execution module is `sopy_fem.sopy_fem_run`.

Example from Python:

``` python
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_BR02', outputFile='mechanics_bars.json')
sopy_fem_run('mechanics_bars.json')
```

You can also run `test_run.py` to execute an example:

``` bash
python test_run.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Get help and generate JSON example files <a id="help"></a>

The `sopy_fem.sopy_fem_help` module prints example contents or writes a JSON example file.

Example to print a sample JSON to the console:

``` python
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_BR02')
```

Example to save a sample JSON to disk:

``` python
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_BR02', outputFile='mechanics_BR02_example.json')
```

You can also run `test_help.py` from the command line:

``` bash
python test_help.py
```

And pass the example type as an argument:

``` bash
python test_help.py structural_TRUSS02
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Available example types <a id="examples"></a>

-  `dynamics_FRAME02`
-  `dynamics_TRUSS02`
-  `electrical_BR02`
-  `mechanics_BR02`
-  `mechanics_QU04`
-  `mechanics_TR03`
-  `structural_TRUSS02`
-  `structural_FRAME02`
-  `thermal_BR02`




<p align="right">(<a href="#readme-top">back to top</a>)</p>




### dynamics_FRAME02

Dynamic analysis of 2D frames. Considers **_inertia_**, **_damping_**, and **_dynamic force_**

#### Sample <a id="dynamics_frame02-sample"></a>
``` python
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('dynamics_FRAME02', outputFile='dynam_frame_example.json')
sopy_fem_run('dynam_frame_example.json')
```

#### Custom file <a id="dynamics_frame02-custom-file"></a>

##### Problem data <a id="dynamics_frame02-problem-data"></a>

The `dynam_frame_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structural Mechanics**)

- `AnalysisType`: Defines the analysis type (**Dynamic analysis**)

- `Dynamic_Analysis_Description`
  - `Num_Modes`: number of natural vibration mode.
  - `Num_increments`: number of time increments of the simulation. 
  - `DeltaT`: time  steps of the simulation. 
  - `Damping_ratio`: damping ratio for energy dissipation. 

- `Mesh`
  - `ElemType`: element type (**FRAME02**, 2 nodes per element)
  - `Nodes`: list of coordinate `{"x": ..., "y":...}` 
  - `Elements`: element kust with
    - `Connectivities`: nodal connectivity (1-based indices/starts with 1)
    - `MaterialId`: material index

- `Materials`
  - `Young`
  - `Density`
  - `Width`
  - `Height`

- `Constraints`
  - `Node`: constrained node
  - `Activation`: `[ux, uy, thetaθz]`
  - `Values`: Indicates value of displacements and rotation. 

- `Masses`
  - `Line_Mass`
    - `Node_ini`: Number of the starting node
    - `Node_end`: Number of the end node
    - `Mass_per_Length`

- `Dynamics_Loads`
  - `Harmonic_Point_Loads`
    - `Node`
    - `Amplitudes`
    - `Load_Frequency(Hz)`

- `Postprocess`
  - `Show_vibration_modes`
  - `Deformed_scale`
  - `Show_dynamics_evolution`
    - `Node`
    - `Result`: Whether **_Disp_x_**, **_Disp_y_** or **_Rotation_**. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="dynamics_frame02-results"></a>

The `dynam_frame_example.res.json` files is composed by:
- `Vibration_Mode_1 (Freq: )`
  - `Natural_Freq (Hz)`
  - `Displacements`
    - `Node`
    - `Disp_x`
    - `Disp_y`




### dynamics_TRUSS02

Dynamic analysis (vibrations) of trusses where there are only axial loads. Considers **_inertia_**, **_damping_**, and **_dynamic force_**.

#### Sample <a id="dynamics_truss02-sample"></a>

```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('dynamics_TRUSS02', outputFile='dynam_truss_example.json')
sopy_fem_run('dynam_truss_example.json')
```

#### Custom file <a id="dynamics_truss02-custom-file"></a>

##### Problem data <a id="dynamics_truss02-problem-data"></a>

The `dynam_truss_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structural Mechanics**)

- `AnalysisType`: Defines the analysis type (**Dynamic analysis**)

- `Dynamic_Analysis_Description`
  - `Num_Modes`: Number of natural vibration mode.
  - `Num_increments`: Number of increments of the simulation. 
  - `DeltaT`: Time interval of the simulation. 
  - `Damping_ratio`: Damping ratio describes the structure's capacity to dissipate energy. 

- `Mesh`
  - `ElemType`: Defines the element type (**TRUSS02** Truss with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs for each element
    - `Connectivities`
    - `MaterialId`

- `Materials`
  - Young Modulus
  - Density
  - Area

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain
  - `Activation`: Indicates for whether activate the restrictions for X, Y axis displacements. 
  - `Values`: Indicates value for displacements. 

- `Dynamics_Load`
  - `Harmonic_Loads`
    - `Node`
    - `Amplitudes`
    - `Load_Frequency(Hz)`

- `Postprocess`
  - `Show_vibration_modes`
  - `Deformed_scale`
  - `Show_dynamics_evolution`
    - `Node`
    - `Result`: Could be **_Disp_x_** or **_Disp_y_**. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="dynamics_truss02-results"></a>

The `dynam_truss_example.res.json` files is composed by:
- `Vibration_Mode_1 (Freq: )`
  - `Natural_Freq (Hz)`
  - `Displacements`
    - `Node`
    - `Disp_x`
    - `Disp_y`




### electrical_BR02 

Distribution of **_electrical potential_** or **_conduction_** in a linear medium (bar). 

#### Sample <a id="electrical_br02-sample"></a>

```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('electrical_BR02', outputFile='elect_example.json')
sopy_fem_run('elect_example.json')
```

#### Custom file <a id="electrical_br02-custom-file"></a>

##### Problem data <a id="electrical_br02-problem-data"></a>

The `elect_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Electrical**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**BAR02** bar with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs for each element
    - `Connectivities`
    - `MaterialId`

- `Materials`
  - Electrical Conductivity
  - Area

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain
  - `Activation`: Indicates for whether activate the restrictions constant voltage.  
  - `Values`: Indicates value for voltage. 

- `Postprocess`
  - `Show_voltage`
  - `Show_current_intensity`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="electrical_br02-results"></a>

The `elect_example.res.json` files is composed by:
- `Voltage`
  - `Node`
  - `Voltage`
- `ElemIntFluxes`
- `Reactions`
  - `Node`
  - `Current_Intensity`




### mechanics_BR02

Solid mechanics for bars with **_Tension_** or **_Compression_**.

#### Sample <a id="mechanics_br02-sample"></a>

```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_BR02', outputFile='mech_br_example.json')
sopy_fem_run('mech_br_example.json')
```

#### Custom file <a id="mechanics_br02-custom-file"></a>

##### Problem data <a id="mechanics_br02-problem-data"></a>

The `mech_br_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structual mechanics**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**BAR02** bar with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs for each element
    - `Connectivities`
    - `MaterialId`

- `Materials`
  - Young Modulus
  - Area

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain
  - `Activation`: Indicates for whether activate fixed support.  
  - `Values`: Indicates value for displacement. 

- `Load`
  - `Point_Loads`
    - `Node`
    - `Value`
  - `Line_Loads`
    - `Node_ini`
    - `Node_end`
    - `qx`

- `Postprocess`
  - `Show_displacements`
  - `Show_forces`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="mechanics_br02-results"></a>

The `elect_example.res.json` files is composed by:
- `Displacements`
  - `Node`
  - `Disp_x`
- `ElemIntForces`
- `Reactions`
  - `Node`
  - `Rx`
  - `Ry`




### mechanics_QU04

2D stress analysis using 4-node quadrilaterals (Q4). It is usually more accurate than TR03.

#### Sample <a id="mechanics_qu04-sample"></a>

```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_QU04', outputFile='mech_qu_example.json')
sopy_fem_run('mech_qu_example.json')
```

#### Custom file <a id="mechanics_qu04-custom-file"></a>

##### Problem data <a id="mechanics_qu04-problem-data"></a>

The `mech_qu_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structual mechanics**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**QU04** quadrilateral elements with 4 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs for each element
    - `Connectivities`
    - `MaterialId`

- `Materials`
  - Plane type
  - Young Modulus
  - Density
  - Poisson
  - Thickness

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain.
  - `Activation`: Indicates for whether activate constrain on X or Y axis. 
  - `Values`: Indicates value for X or Y displacements. 

- `Load`
  - `Line_Loads`
    - `Node_ini`
    - `Node_end`
    - `qy`
  - `Body_Loads`
    - `Elem`
    - `qy`

- `Postprocess`
  - `Show_displacements`
  - `Show_strains`
  - `Show_stresses`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="mechanics_qu04-results"></a>

The `mech_qu_example.res.json` files is composed by:
- `Displacements`
  - `Node`
  - `Disp_x`
  - `Disp_x`
- `Strains`
  - `Node`
  - `Epsilon_x`
  - `Epsilon_y`
  - `Gamma_xy`
- `Stresses`
  - `Node`
  - `Sigma_x`
  - `Sigma_y`
  - `Tau_xy`
- `Reactions`
  - `Node`
  - `Rx`
  - `Ry`




### mechanics_TR03
2D stress analysis using 3-node triangles (T3). Ideal for irregular meshes. 

#### Sample <a id="mechanics_tr03-sample"></a>

```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('mechanics_TR02', outputFile='mech_tr_example.json')
sopy_fem_run('mech_tr_example.json')
```

#### Custom file <a id="mechanics_tr03-custom-file"></a>

##### Problem data <a id="mechanics_tr03-problem-data"></a>

The `mech_tr_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structual mechanics**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**TR03** triangular elements with 3 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs for each element
    - `Connectivities`
    - `MaterialId`

- `Materials`
  - Plane type
  - Young Modulus
  - Poisson
  - Thickness

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain.
  - `Activation`: Indicates for whether activate constrain on X or Y axis. 
  - `Values`: Indicates value for X or Y displacements. 

- `Load`
  - `Point_Loads`
    - `Node`
    - `Values`

- `Postprocess`
  - `Show_displacements`
  - `Show_strains`
  - `Show_stresses`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="mechanics_tr03-results"></a>

The `mech_tr_example.res.json` files is composed by:
- `Displacements`
  - `Node`
  - `Disp_x`
  - `Disp_x`

- `Strains`
  - `Node`
  - `Epsilon_x`
  - `Epsilon_y`
  - `Gamma_xy`

- `Stresses`
  - `Node`
  - `Sigma_x`
  - `Sigma_y`
  - `Tau_xy`

- `Reactions`
  - `Node`
  - `Rx`
  - `Ry`




### structural_FRAME02
Static analysis of 2D frames. Calculates bending moments, shear and axial forces.

#### Sample <a id="structural_frame02-sample"></a>
```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('structural_FRAME02', outputFile='struct_frame_example.json')
sopy_fem_run('struct_frame_example.json')
```

#### Custom file <a id="structural_frame02-custom-file"></a>

##### Problem data <a id="structural_frame02-problem-data"></a>
The `struct_frame_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structural Mechanics**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**FRAME02** Frame with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`
    - Connectivities
    - Material id 

- `Materials`
  - Young Modulus
  - Area
  - Inertia

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain. 
  - `Activation`: Indicates for whether activate the restrictions for X, Y  axis displacements and rotations. 
  - `Values`: Indicates for value of displacements and rotation. 

- `Loads`
  - `Point_Loads`
    - `Node`
    - `Value`
  - `Line_Loads`
    - `Node_ini`
    - `Node_end`
    - `qy` 

- `Postprocess`
  - `Show_displacements`
  - `Show_forces`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="structural_frame02-results"></a>
The `struct_frame_example.res.json` files is composed by:
- `Displacements`
  - `Node`
  - `Disp_x`
  - `Disp_y`
  - `theta`

- `Reactions`
  - `Node`
  - `Rx`
  - `Ry`
  - `Mz`




### structural_TRUSS02
Static analysis of 2D trusses. The elements only work in **_tension_** or **_compression_**. 

#### Sample <a id="structural_truss02-sample"></a>
```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('structural_TRUSS02', outputFile='struct_truss_example.json')
sopy_fem_run('struct_truss_example.json')
```

#### Custom file <a id="structural_truss02-custom-file"></a>

##### Problem data <a id="structural_truss02-problem-data"></a>
The `struct_truss_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Structural Mechanics**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**TRUSS02** Truss with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs of values **Connectivities**, **Material id** for each element. 

- `Materials`
  - Young Modulus
  - Density
  - Area

- `Constraints`: Defines a list of triplets of
  - `Node`: Indicates which node you want to have a constrain. 
  - `Activation`: Indicates for whether activate the restrictions for X and Y axis displacements. 
  - `Values`: Indicates for value of displacements. 

- `Loads`
  - `Point_Loads`: Defines which `Node` and which `Value` of point load you want. 

- `Postprocess`
  - `Show_displacements`
  - `Show_deformed`
  - `Deformed_scale`
  - `Show_forces`
  - `Show_reactions` 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="structural_truss02-results"></a>
The `struct_truss_example.res.json` files is composed by:
- `Displacements`
  - `Node`
  - `Disp_x`
  - `Disp_y`

- `ElemIntForces`: Defines for internal force for each element.

- `Reactions`
  - `Node`
  - `Rx`
  - `Ry`




### thermal_BR02 
Heat transfer by conduction in 1D/2D bars governed by Fourier's law. The **_temperatures_** at the ends of the bar are set as **_constant_**. 

#### Sample <a id="thermal_br02-sample"></a>
```
from sopy_fem.sopy_fem_run import sopy_fem_run
from sopy_fem.sopy_fem_help import sopy_fem_help

sopy_fem_help('thermal_BR02', outputFile='thermal_example.json')
sopy_fem_run('thermal_example.json')
```

#### Custom file <a id="thermal_br02-custom-file"></a>

##### Problem data <a id="thermal_br02-problem-data"></a>
The `thermal_example.json` file is composed by:

- `ProblemType`: Defines the problem type (**Thermal**)

- `AnalysisType`: Defines the analysis type (**Static analysis**)

- `Mesh`
  - `ElemType`: Defines the element type (**BAR02**: Bar with 2 nodes per element)

  - `Nodes`: Defines a list of coordinate pairs of a node in the Cartesian plane. 

  - `Elements`: Defines a list of pairs of values **Connectivities**, **Material id** for each element.

- `Materials`
  - Thermal Conductivity
  - Area

- `Constraints`: Defines a list of triplets of values **Node**, **Activation** and **Values**. Where **Node** indicates which node you want to have a constrain, **Activation**, and **Values** indicates for value of temperatures. 

- `Postprocess`
  - `Show_temperatures`
  - `Show_themal_fluxes`
  - `Show_reactions`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

##### Results <a id="thermal_br02-results"></a>
The `struct_truss_example.res.json` files is composed by:
- `Temperatures`
  - `Node`
  - `Temp`

- `ElemIntFluxes`: Defines for internal heat flux for each element.
- `Reactions`
  - `Node`
  - `Flux`




## Project Structure

- `sopy_fem/assembly.py` — global matrix and vector assembly.
- `sopy_fem/read_data.py` — JSON input data reading.
- `sopy_fem/initialization.py` — data initialization and boundary conditions.
- `sopy_fem/solver.py` — equation solver.
- `sopy_fem/postprocess.py` — postprocessing and results.
- `sopy_fem/sopy_fem_run.py` — main execution flow.
- `sopy_fem/sopy_fem_help.py` — help functions and example generation.
- `sopy_fem/Examples/` — JSON example data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contribution

Any contributions are **greatly appreciated**

If you have a suggestion that would make this better, please fork the repo and create a pull request. 

## License

See the `LICENSE` file for license terms.

## Contact
Daniel Di Capua's mail: dicapua@cimne.upc.edu
