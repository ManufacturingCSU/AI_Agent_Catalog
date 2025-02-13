# Agents

## image_extractor_from_files  

This agent can extract images from the following files:
- Microsoft Office files
    - Microsoft Word (docx)  
    - Microsoft Excel (xlsx)
    - Microsoft PowerPoint (pptx)   

- Images
    - png
    - jpeg
    - jpg

- PDFs
    - coming soon


### How to use the agent  

currently, the agent works from command line where you call the agent and pass in the path of the file or the URL

**Example**
1. passing in a URL from the root folder 
```text
python -m backend.agents.image_extractor_from_files https://raw.githubusercontent.com/Coding-Forge/Fabric/main/images/admin-portal-settings.png
```
2. passing in a local file from the root folder
```text
python -m backend.agents.image_extractor_from_files ./files/myworddoc.docx
```

### Python packages
you can create a virtual environment and install packages from the `requirements.txt` file or if using conda you can create an environment using the `environment.yaml` file