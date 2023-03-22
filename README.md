# printing_list
takes all files in a folder and printes the names into a file to work with it in a seperate way

## 📐 How-To
The files inside the folder, you want to write into a *.txt file should have the same name convention. In other cases the file could fabricate wrong results.  
For example:  

📁 **FOLDER:**  
     -|--- "filename_key1xx0_key2xx.datatype"  
     -|--- "filename_key1xx1_key2xx.datatype"  
     -|--- "filename_key1xx2_key2xx.datatype"  
     -|...  
     -|- "filename_key1xx_key2NNN.datatype"  
  
### ℹ️ important Information
1. In case you want to remove a part of the path type in to the variable *PATH_REMOVE*
2. To give the script the name of the folder type the name into the variable *FOLDER*
3. specify the delimiter between folder name and a possible value behind, which should be added to the *FILENAME* type it into the *DELIMITER*
4. specify the datatype, which corresponds to the ending of the file, which is listed inside the folder to the variable *DATATYPE*
5. specify key 1 in *KEY_NAME_1*
6. specify key 1 in *KEY_NAME_1* -> up to now, you have to specify both key names!
7. specify or change the init value of the *KEY_VALUE_1* and *KEY_VALUE_2* depending, if the value in the *FOLDER* references to the *KEY_VALUE_1* or *KEY_VALUE_2*
8. specify the first lines of the file, in case a software reads and interprets that in to the variable *HEADER*
  
## 📄 Resulting File
The File is optimized for the usage of ADS (PathWave Advanced Design Software), so the header of the fits to the formate:

`BEGIN DSCRDATA`  
`INDEX file`  
`0 filename_key1xx0_key2xx.datatype`  
`1 filename_key1xx1_key2xx.datatype`   
`2 filename_key1xx2_key2xx.datatype`  
`  ...`  
`N filename_key1NNN_key2xx.datatype`  
`END`  


