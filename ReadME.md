Using the requirement.yaml file you should be able to download all the dependencies.
conda env create -f requirement.yml
In case this doesn't work, the following is the manual installation of the dependencies.

In order to use my program, first make sure you pip install the following.
pip install transforms torch.
pip install transformers.

Then using conda,
conda install -c conda-forge cmake
conda install -c conda-forge sentencepiece

github repository is https://github.com/BeginnerCoder99/project1/
so you can clone repository.
Make sure you have the AIprompt.txt file in the same directory as the executable.
It should create and write to AIoutput.txt 