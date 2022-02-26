

# Belo_Lin_2012RFS

> This repo contains partial python replication of Belo, Lin 2012 RFS paper: The inventory growth spread. 
> Paper link [_here_](https://academic.oup.com/rfs/article-abstract/25/1/278/1571868). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Rep structure](#structure-of-the-replication)
* [Reference](#reference) <!-- * [Screenshots](#screenshots) -->
* [Setup](#setup) <!-- * [Usage](#usage) -->
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- The replication corresponds to empirical part (section one) of the paper
- Two stylized facts the data imply:
  - Real quantity: inventory growth is procyclical
  - Asset pricing: lower inventory growth firms have higher risk premium
- The purpose of this replication is to help familiarize myself with inventory related data, and issues coming along with the empirical choices
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Structure of the replication
- Code
  - running
  - output
  - computation
- Data
  - cpi
  - CRSP monthly (WRDs remote access)
  - Compustat annually (WRDs remote access)
- Output
  - latex table
    - summary statitics
    - one way sorted portfolio
    - two way sorted portfolio (TBA) 


## Reference
List the useful reference here:
- [Freda WRDs](https://www.fredasongdrechsler.com/home)
- [Fred inflation](https://fred.stlouisfed.org/series/FPCPITOTLZGUSA)
- [Latex table](https://en.wikibooks.org/wiki/LaTeX/Tables)


<!-- ## 
![Example screenshot](./Output/screenshot.png) -->
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
This replication only requires access to WRDs Compustat and CRSP, as well as their linktable. One can proceed step by step using the jupyter notebook. 
<!-- 
## Usage
How does one go about using it?
Provide various use cases and code examples here. -->

`running.ipynb`


## Project Status
Project is: _in progress_ 


## Room for Improvement

Room for improvement:
- Winsorizing condition is a bit more strict than original paper
- Inventory itself is pretty volatile
- The edition from to_latex() generated table to a table resembling the original paper takes some manual work

To do:
- Finish the two-way sorted portfolio analysis
- Try to play with the model calibration part if time allows


## Acknowledgements
- This project was an exercise relavent to my second year paper
- Any mistake is all mine
- Many thanks to the advise from [Frederico](https://sites.google.com/a/umn.edu/frederico-belo/)


## Contact
Created by [@Xinyu_Liu](https://www.insead.edu/phd/student-profiles/xinyu-liu) - feel free to contact me via email or [twitter](https://twitter.com/wentworth_liu_)!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
