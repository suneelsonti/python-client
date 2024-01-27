# Dummy Python Client

This Python client is a dummy app for exploring the Software Catalog of Backstage. You'll need the [NodeJS server](https://github.com/heraldofsolace/nodejs-server-server).

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Getting Started

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BlogServiceApi* | [**api_v1_articles_get**](docs/BlogServiceApi.md#api_v1_articles_get) | **GET** /api/v1/articles | 
*BlogServiceApi* | [**api_v1_articles_post**](docs/BlogServiceApi.md#api_v1_articles_post) | **POST** /api/v1/articles | 


## Documentation For Models

 - [Article](docs/Article.md)
 - [ArticlesList](docs/ArticlesList.md)
 - [CreateArticleRequest](docs/CreateArticleRequest.md)
 - [ReturnAllArticles](docs/ReturnAllArticles.md)


## Documentation For Authorization

 All endpoints do not require authorization.


