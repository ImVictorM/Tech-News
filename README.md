# Tech News 📰

## Project Context 💡
This project consists in practicing web scraping on the [Trybe's blog](https://blog.betrybe.com/?_gl=1*1tivy9k*_ga*MjEzMzE1MDMzNS4xNjc1MDM3MDkw*_ga_JRYMZ1LMBF*MTY4NTM4MjI0Ni4xMTcuMS4xNjg1MzgyODk3LjQ2LjAuMA..).

### Acquired Knowledge 📖
In this project, I was able to:
- Apply web scraping technics;
- Extract data from HTML content;
- Maintain the extracted data on a NoSQL database.


## Main Technologies 🧰
<table>
    <thead>
        <tr>
            <th>Python</th>
            <th>Pytest</th>
            <th>Requests</th>
            <th>Parsel</th>
            <th>Pymongo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
               <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" 
                       alt="python" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://docs.pytest.org/en/7.3.x/" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png" 
                       alt="pytest" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://pypi.org/project/requests/" target="_blank">
                    <img
                         src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"
                         alt="requests"
                         width="40"
                         height="40"
                    />
                </a>
            </td>
               <td align="center">
                <a href="https://pypi.org/project/parsel/" target="_blank" rel="noreferrer"> 
                    <img 
                         src="https://static.vecteezy.com/system/resources/thumbnails/019/518/427/small/404-error-icon-for-your-website-mobile-presentation-and-logo-design-free-vector.jpg" 
                         alt="parsel" 
                         width="40" 
                         height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://pymongo.readthedocs.io/en/stable/" target="_blank" rel="noreferrer"> 
                    <img 
                         src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" 
                         alt="mongodb" 
                         width="40" 
                         height="40"
                    /> 
                </a>
            </td>
        </tr>
    </tbody>
</table>

## Running the application ⚙️

1. Clone the repository and enter it
```
git clone git@github.com:ImVictorM/Tech-News.git && cd Tech-News
```

<details>
<summary><h4>🐋 Running with docker</h4></summary>

2. Get the containers running
```
docker-compose up -d
```

3. Enter the app container
```
docker exec -it tech_news bash
```

4. Install the main package
```
pip install .
```

5. Init the app
```
tech-news-analyzer
```
    

</details>

<details>
<summary><h4>🖥️ Running locally</h4></summary>

> You must have mongodb installed

2. Create the virtual environment
```
python3 -m venv .venv && source .venv/bin/activate
```

3. Install the dependencies
```
python3 -m pip install -r dev-requirements.txt
```

4. Install the main package
```
pip install .
```

5. Init the app
```
tech-news-analyzer
```

</details>


## Testing 🛠️
To run all tests:
```
python3 -m pytest
```
Running only one test file:
```
python3 -m pytest {test_file_path}.py
```
