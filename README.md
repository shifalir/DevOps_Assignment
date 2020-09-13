# DevOps_Assignment
Please go through the DevOps_Assignment word documentfor the answers and explanation of the assignement.
The same is also available as an MD file Answers.md.

How to execute the docker script:
--------------------------------
To execute the pipeline please navigate to the Assignments/docker directory and execute the docker script with the command: 
    
  docker-compose up
 --  
    
How to execute the script to create a data pipeline:
----------------------------------------------------
1. To execute the data pipeline please navigate to the Assignments/data_pipeline directory and in there execute the mains.py lise so:

  python mains.py scripts
  --
“scripts” should be the first argument
    

2.Another way to run the data pipeline is:

python mains.py scripts script1_data_ingestion.py script2_data_transformation.py script3_data_vizualization.py   
-- 
 Here we provide a s arguments an order in which scripts are run.
First  argument must be  location of scripts(“scripts”) followed by the scripts to execute in the order of execution.


