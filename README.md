# Server Config

## Introduction
A small python project to manage configuration as a service backed by a cloud storage for a client-server application.

The need and basic application is from my _game development_ experience. Some constants and definitions (cards, units, spells) needed to be changed remotely on the server, but they were required by the client as well in order to dysplay information for the user.

**The first implementation will use AWS S3 as storage**

The ideea  is to provide a package that can be used in any project with minimal dependencies, as part of a biger application or as a seprate service.

Here comes a list of things that would make my happy :)

Features:
 1. Config AWS
 1. CloudFront and Sign URLS
 1. Read data as JSON from S3
 1. Serve data API 
 1. Version data
 1. Bundle data in a zip that can be downloaded by a client
 1. Enviroments (dev, prod)
 1. Promote data different environements (dev -> prod)
 1. Example Service
 1. JSON Schema validation
 1. Scripts for validation of data
 1. Frontend
 1. Trigger data reload remotely


----------------------------
 ## Architecture
----------------------------

 ### Assumptions and limitiations

 The data will be kept only as json. The validity of the data is enforced using JSON Schema.

 For differents environments, it's assumed that **the same structure** is kept with a different **prefix**.

 Using dev and prod as the _named environments_, example of file structure in a bucket:
 *  dev/version.json
 
    dev/files/server_constants.json

    dev/files/units/faction1_units.json

    dev/files/units/faction2_units.json

*   prod/version.json
 
    prod/files/server_constants.json

    prod/files/units/faction1_units.json

    prod/files/units/faction2_units.json

**version.json is managed by this package**



---------------------------
## Config AWS

Having provided valid credentials of an aws account connect using BOTO, specify bucket

Config:
* aws credentials
* aws region
* aws S3 bucket
* version file name prefix (default is none) - to avoid clashing with user files
* environments
 

## Sign URLS
 
Configure CDN to serve files and hide from public S3 files.
Use restricted access and sign URLs

