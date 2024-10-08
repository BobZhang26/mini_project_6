"""
extract a dataset from URL
"""
import requests
import os

def extract(
    url="https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Chennai%20rain/chennai_reservoir_rainfall.csv",
    filepath="rainfall.csv",
):
    with requests.get(url,timeout=5) as r:
        with open(filepath, "wb") as f:
            f.write(r.content)
    return filepath


if __name__ == "__main__":
    if os.path.exists('/Users/zhangbobby/Desktop/IDS706/mini_project_5'):
        os.chdir('/Users/zhangbobby/Desktop/IDS706/mini_project_5')
    else:
        print("Directory does not exist.")

    extract()
