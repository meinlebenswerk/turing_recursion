# Turing recursion

A toy project with the goal of running Conway's Game of Life on Rule 110.
The core idea is based on Matthew Cook's [paper](https://arxiv.org/pdf/0906.3248) on rule 110 computation, which shows that it's possible to encode arbitrary turing machines in rule 110.

Originally, this was born out of the idea of implementing conway's game of life directly in hardware, using a systolic array, which, while possible, becomes annoyingly complex because of the moore neighborhood GoL requires.
But 1D cellular automata are much simpler, basically implementable with a shift-register and minimal logic (or a high-speed implementation that uses some generate magic), but they're not particularly interesting on their own.
With the possibilities of universal computation, however, they start to become much more appealing again, and the idea for turing-recursion was born.

## Goals
These will be updated as the project progresses, but currently the outline is:

- [x] Implement Conway's Game of Life for a turing machine
- [ ] Implement a tag-system emulator and compiler for the turing machine based on Matthew Cook's paper
- [ ] Transform the tag-system into a cyclic tag-system along with an emulator
- [ ] Transform and emulate that cyclic tag-system into a starting configuration for Rule 110
- [ ] Implement helpers to display and visualize what's going on along the way
- [ ] Write a highspeed SystemVerilog implementation of Rule 110
- [ ] Make the Hardware implementation rule Game of Life on Rule 110, extract and display the state

## Running the project
As of now most of the interesting things are contained in ipython notebooks, within the `notebooks` directory.
Since this project uses [poetry](https://python-poetry.org/) for dependency management, getting up-and-running is as easy as setting up poetry, then running `poetry install` in the project root.
Note that this already install the ipython-kernel required to run the notebooks from VsCode.

