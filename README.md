# clarifai-custom-increment-train-python
image classify  based on clarifai python api ; with the capacity of custom incrementally trainning model
# about clarifai
abstract : Build smarter apps faster with Clarifai’s powerful visual recognition technology.(reference from official doc)
# demo environment:

```
python2.7.5; with module of :
    clarifai (2.0.14)
    PySocks (1.6.1)
    shadowsocks (2.8.2)
    SocksiPy-branch (1.1)
```

# File Structure
```
    EADME.md
    |-- test_clarifai.py (basic demo of clarifai)
    |-- test_clarifai2.py (*main code*: update images and concepts ;create or update incrementally the model;then train the model)
    |-- test_clarifai3.py (predict with the model trained above)
    |-- test_clean.py (for test clean the model)
    |-- test_update.py (for test update the model with specified concepts)
    |-- test_input.py (for print all of the input image info...later,I found the uploaded image info at official's [cms](https://preview.clarifai.com/#/apps/${app_id}/) including crud of the images)
    |-- test_image_clarifai_1 (the test case for general model; in other word ,for test_clarifai.py)
    |   |-- 1.jpg
    |   |-- 3.jpg
    |   |-- 6.jpg
    |   |-- 7.jpg
    |   |-- 8.jpg
    |   `-- metro-north.jpg
    |-- test_image_clarifai_2 (the test case for training model ;in other word ,for test_clarifai2.py)
    |   |-- atm1.jpg
    |   |-- atm2.jpg
    |   |-- atm3.jpg
    |   |-- fls1.jpg
    |   |-- fls2.jpg
    |   |-- fls3.jpg
    |   |-- xyy1.jpg
    |   |-- xyy2.jpg
    |   `-- xyy3.jpg
    |-- test_image_clarifai_3 (the test case for  model predict ;in other word ,for test_clarifai3.py)

    |   |-- atm4.jpg
    |   |-- atm5.jpg
    |   |-- fls4.jpg
    |   |-- fls5.jpg
    |   |-- fls6.jpg
    |   |-- fls7.jpg
    |   |-- xyy4.jpg
    |   `-- xyy5.jpg
    |-- test_dir_walk.py...etc  (middle crop for unit test; can be ignored )
```
# helpful and getting started link of clarifai:
```
    1. lastest version for download ,note *latest*!! : [install](https://sdk.clarifai.com/python/docs/latest/install.html) 
    2. api reference , also latest: [api reference](https://sdk.clarifai.com/python/docs/latest/clarifai.rest.html)
    3. application , find the app id and secret here : [your app id & app secret](https://developer-preview.clarifai.com/account/applications/)
    4. cms, management of your app/collection/image data;*pay attention to* the left pannel ,Unfolding will bring your eyes bright: [backend cms](https://preview.clarifai.com/#/apps/${app_id}/)
```

