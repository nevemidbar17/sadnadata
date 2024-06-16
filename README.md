# Data sadna v2 
## Repo Structure
### Exercises
There are 3 folders containing the exercises and solutions
* A - easiest, everyone must pass.
* B - main questions
* C - enrichment
### Dataset
#### There are 4 datasets in the sadna:
* brazil_exports_from_2018.csv - The main dataset used at A and B.
* brazil_exports_only_{2018,2019,2020}.csv - 3 datasets used at C.

The Dataset is in a Google Drive link because they are too heavy to upload to the repo, The link is at `files.txt`.
### limited_python
limited_python is the environment to create the docker image.

You should create 2 images, when doing A and B run the command mentioned at the readme in the folder.

When doing exercise C you should rename `limit_resources_threads.py` to `limit_resources.py` and rebuild the image.

### Running files
The repo comes with 2 files, `main.py` and `script.py`, you can use the files to write code and use it.

Using only `script.py` is recommended.

## Migration to bissnet
When migrating to the Biss net you should burn the repository + the datasets to disks.
### Creating a docker images
Create 2 images and upload them to the nexus
* First image - under the name `limited_python` with the tag `v1`
* Second image - delete `limit_resources.py` and rename `limit_resources_threads.py` to `limit_resources.py`, then create a second image under the name `limited_python` with the tag `v2`
### Productionize
* Create 3 Sections for the workshop: A, B, and C.
  * For each section split the questions in the text file into different questions and upload the dedicated patbas.
* In section A create a setup question giving all the files for the environment:
  * docker-compose.yml, main.py, script.py add somewhere the command `docker-compose up --force-recreate` indicating that this is how to run the code.
  * delete the code in `script.py`
## Presentation
### Opening talk
* When the sadna is being run you should talk with the student for 10 minutes explaining how to use the environment, and its limits and answer questions.
* Explain the struggle (low resources, big csv)
* **DON'T** say how many questions there are
### Big Data Principals
Save the presentation and present it to the development megama.
## How to run your code?
1. `cd` to this folder
2. Create a `main.py` module (you can make imports from it to other modules)
3. Run `docker-compose up --force-recreate` This will run the code in your `main`.
