QDW (Quattor Data Warehouse) Installation
=========================================

System Requirements
-------------------
Linux (Developed on Ubuntu 11.04 but should have a degree of backwards compatibility)
A collection of .json format quattor server profiles

Dependencies
------------
QDW has the following dependencies:

*   Python Library: pyes
*   Elastic Search
*   Python and its Standard Libraries
*   git
*   curl

Installation
------------
Along with the dependencies some settings in the elasticsearch.yml config file must be edited (eg./etc/elasticsearch/elasticsearch.yml)

    cluster.name: 'hostname of computer to ensure uniqueness'
    node.master: true
    node.data: true
    http.max_content_length: 600mb

First Time Setup
----------------
1.   Install
2.   Store the profiles to be analysed inside the 'Profiles' folder within the install directory. It must be empty to start with and is case sensitive.
3.   The first time that the program is run it may take some time (~30mins based on 1500 profiles of 300kB each), this first time setup can be initiated at any time however by running the program with no arguments.
