# **move-fd**
_Scripting program to move files and folders._
## Starting
I recommend viewing the script help.
### A quick example:
- For Windows Users:
    ```
    python move-fd.py -h
    ```
    Open the '**cmd**' and try the following command:
    ```
    python move-fd.py -x "file_or_folder" -o %USERPROFILE%\Desktop
    ```
    If you prefer to use '**powershell**', try using the following command:
    ```
    python move-fd.py -x "file_or_folder" -o $ENV:userprofile\Desktop
    ```
- For Linux Users:
    ```
    python3 move-fd.py -h
    ```
    ```
    python3 move-fd.py -x "file_or_folder" -o ~/Desktop
    ```
**Note**: It is recommended to use the full path.

## LICENSE
move-fd is free software and may be redistributed under the terms specified in the [license]

<!-- [license]: https://github.com/AlejandroAlfredo/move-fd/blob/main/LICENSE -->